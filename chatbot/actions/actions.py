from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3

DATABASE_PATH = "/Users/vedant/Desktop/ecommerce_salesbot/backend/inventory.db"

# Utility function to connect to the database
def db_connect():
    return sqlite3.connect(DATABASE_PATH)

# Utility function to fetch products based on name or category
def fetch_products(query: str) -> List[tuple]:
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, price, description FROM products WHERE name LIKE ? OR category LIKE ?",
        (f"%{query}%", f"%{query}%")
    )
    products = cursor.fetchall()
    conn.close()
    return products


# Utility function to execute SQL commands
def execute_query(query: str, params: tuple = ()):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

# Utility function to check if a product exists in the database
def product_exists(product_name: str) -> bool:
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM products WHERE name = ?", (product_name,))
    product = cursor.fetchone()
    conn.close()
    return product is not None

# Action to recommend products
class ActionRecommendProducts(Action):
    def name(self) -> Text:
        return "action_recommend_products"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        products = execute_query("SELECT name, price, description FROM products LIMIT 5")
        
        if products:
            dispatcher.utter_message(text="Here are some trending products:")
            for product in products:
                dispatcher.utter_message(
                    text=f"- {product[0]} (₹{product[1]}): {product[2]}"
                )
        else:
            dispatcher.utter_message(text="No products available at the moment.")
        return []

# Action to search for a product
class ActionSearchProduct(Action):
    def name(self) -> Text:
        return "action_search_product"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product") or tracker.get_slot("category")

        if product_name:
            products = fetch_products(product_name)
            if products:
                dispatcher.utter_message(text=f"Here are the results for '{product_name}':")
                for product in products:
                    dispatcher.utter_message(
                        text=f"- {product[0]} (₹{product[1]}): {product[2]}"
                    )
            else:
                dispatcher.utter_message(text=f"No results found for '{product_name}'.")
        else:
            dispatcher.utter_message(text="Please specify the product or category you are looking for.")

        # Reset the product/category slot
        return [SlotSet("product", None), SlotSet("category", None)]

# Action to get product details
class ActionGetProductInfo(Action):
    def name(self) -> Text:
        return "action_get_product_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the product slot value dynamically
        product_name = tracker.get_slot("product")
        print(f"Debug: Received product slot value - {product_name}")  # Debugging

        if not product_name:
            dispatcher.utter_message(
                text="Could you please specify the product you'd like more information about?"
            )
            return []

        # Fetch the exact product details dynamically from the database
        try:
            conn = db_connect()  # Assuming db_connect() is defined to connect to the database
            cursor = conn.cursor()

            # Use a case-insensitive search and handle partial matches for the product
            cursor.execute(
                "SELECT name, description FROM products WHERE LOWER(name) LIKE LOWER(?) LIMIT 1",
                (f"%{product_name}%",)
            )
            product = cursor.fetchone()
            conn.close()

            # If the product is found, respond with its details
            if product:
                dispatcher.utter_message(
                    text=f"Here is more information about '{product_name}': {product[1]}"
                )
            else:
                dispatcher.utter_message(
                    text=f"Sorry, no details are available for '{product_name}'. Please try again with a different product name."
                )

        except Exception as e:
            print(f"Debug: Exception occurred - {e}")  # Debugging exception
            dispatcher.utter_message(
                text="An error occurred while fetching product details. Please try again later."
            )

        return []

# Action to add a product to the cart
class ActionAddToCart(Action):
    def name(self) -> Text:
        return "action_add_to_cart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")
        if product_name:
            if product_exists(product_name):
                execute_query(
                    "INSERT INTO cart (product_name, quantity, price) "
                    "SELECT name, 1, price FROM products WHERE name = ?",
                    (product_name,)
                )
                dispatcher.utter_message(text=f"{product_name} has been added to your cart.")
            else:
                dispatcher.utter_message(text=f"'{product_name}' is not available.")
        else:
            dispatcher.utter_message(text="Please specify the product to add to your cart.")
        return []

# Action to view cart
class ActionViewCart(Action):
    def name(self) -> Text:
        return "action_view_cart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cart_items = execute_query("SELECT product_name, quantity, price FROM cart")

        if cart_items:
            cart_summary = "Your cart contains:\n"
            total_price = 0

            for item in cart_items:
                product_name, quantity, price = item
                cart_summary += f"- {product_name}: {quantity} x ₹{price} = ₹{quantity * price}\n"
                total_price += quantity * price

            cart_summary += f"\nTotal: ₹{total_price}"
            dispatcher.utter_message(text=cart_summary)
        else:
            dispatcher.utter_message(text="Your cart is empty.")
        return []

# Action to clear cart
class ActionClearCart(Action):
    def name(self) -> Text:
        return "action_clear_cart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        execute_query("DELETE FROM cart")
        dispatcher.utter_message(text="Your cart has been cleared.")
        return []

# Action to checkout
class ActionCheckout(Action):
    def name(self) -> Text:
        return "action_checkout"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cart_items = execute_query("SELECT product_name, quantity, price FROM cart")

        if cart_items:
            execute_query("DELETE FROM cart")  # Clear the cart after checkout
            dispatcher.utter_message(text="Your cart has been checked out successfully! You will receive an email confirmation shortly.")
        else:
            dispatcher.utter_message(text="Your cart is empty.")
        return []
