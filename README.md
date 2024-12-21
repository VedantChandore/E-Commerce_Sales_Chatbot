
---

# **Project Title**  
E-COMMERCE SALES CHATBOT 

## **Table of Contents**  
- [About the Project](#about-the-project)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup and Installation](#setup-and-installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  
- [API Endpoints (if applicable)](#api-endpoints)   
- [License](#license)  

---

## **About the Project**  

This project is an AI-powered E-Commerce Chatbot designed to provide a seamless and interactive shopping experience. The chatbot allows users to search for products, manage their cart, and complete checkout through natural language conversations. 
It integrates Rasa for conversational AI, Flask for backend operations, and SQLite for dynamic database management.
The chatbot enables users to interact naturally by searching for products based on names or categories. 
It fetches product details, including name, price, and description, directly from the database, ensuring up-to-date and accurate information. Additionally, it recommends trending products to users, enhancing the shopping experience with personalized suggestions.
A robust cart management system allows users to add items to their cart, view their cart contents with detailed pricing, and clear the cart when needed. The checkout functionality confirms the order and prepares for integration with future payment processing systems.
The chatbot’s backend dynamically executes database queries to handle large inventories and ensure real-time updates for user actions. Its modular architecture makes it suitable for integration into larger e-commerce platforms, with the flexibility to incorporate additional features like user authentication and payment gateways.
This project showcases the potential of conversational AI in transforming e-commerce by offering an efficient, user-friendly, and intelligent shopping assistant.

### **Problem Statement**  

In today's fast-paced digital era, e-commerce platforms have become the cornerstone of modern shopping. However, users often face challenges such as: 
1. **Difficulty in Navigation**: Browsing through vast product catalogs to find the desired item can be time-consuming and overwhelming.
2. **Limited Interactivity**: Traditional e-commerce platforms lack personalized and conversational assistance, leading to a less engaging shopping experience.
3. **Inefficient Cart Management**: Managing items in the cart, retrieving product information, and completing purchases can be cumbersome without intuitive tools.
4. **High Drop-off Rates**: Due to lack of instant support and personalized recommendations, users may abandon their shopping journey before completing a purchase.
These challenges highlight the need for an intelligent solution that simplifies the shopping experience, provides personalized assistance, and enhances user engagement in real-time. 
This calls for the integration of conversational AI to revolutionize how users interact with e-commerce platforms.

### **Solution**  

Our project addresses the challenges of modern e-commerce by integrating a conversational AI chatbot with a dynamic backend, creating an intelligent and interactive shopping experience for users. 
The solution leverages a Flask-based backend with SQLite database integration and Rasa's natural language understanding (NLU) capabilities to offer seamless product discovery, efficient cart management, and personalized assistance.
#### Approach:  
1. **Conversational Interaction**:  
   We implemented a conversational chatbot powered by Rasa, enabling users to interact naturally through text.
   This eliminates the need for traditional search mechanisms and makes the shopping experience more intuitive.
3. **Contextual Understanding**:  
   By using intent recognition and entity extraction, the chatbot understands user queries in context.
   Whether a user wants to search for a specific product, inquire about details, or manage their cart, the system processes the request dynamically.
5. **Dynamic Database Queries**:  
   The backend connects to an SQLite database containing extensive product data.
   When users search or request information, the system dynamically fetches relevant records, ensuring that the response is always accurate and up-to-date.
7. **Personalized Assistance**:  
   The solution adapts to user preferences, offering personalized product recommendations based on trending items or the user's previous interactions.
   This ensures that users receive suggestions tailored to their needs, enhancing engagement.
9. **Efficient Cart Management**:  
   The chatbot simplifies cart operations like adding, viewing, or clearing items.
   By integrating structured database queries, it ensures the cart reflects real-time updates, allowing users to manage purchases effortlessly.
11. **Streamlined Checkout**:  
   The system ensures a hassle-free checkout process. Once the user finalizes their cart, the chatbot provides clear instructions and confirmation, fostering trust and reducing drop-off rates.

By combining conversational AI with robust backend functionality, our project creates an innovative e-commerce platform where users can shop with ease, find products faster, and engage in a personalized shopping experience, addressing the challenges of traditional online stores.

---

## **Features**   

#### Core Features:  
1. **Conversational AI Chatbot**  
   - Interact naturally with users to provide product recommendations, details, and assistance.  
   - Supports intents like greeting, product search, cart management, and checkout.  

2. **Dynamic Product Search**  
   - Allows users to search for products by name or category through natural language input.  
   - Retrieves real-time results from the integrated database.  

3. **Product Information Retrieval**  
   - Provides detailed descriptions and specifications of products upon request.  

4. **Personalized Product Recommendations**  
   - Suggests trending and popular products based on dynamic queries to the database.  

5. **Cart Management**  
   - Enables users to add, view, or clear items in their shopping cart seamlessly.  
   - Ensures real-time synchronization with the backend database.  

6. **Streamlined Checkout Process**  
   - Assists users in completing their purchases with a conversational flow.  

#### Unique Aspects:  
1. **Integration with SQLite Database**  
   - The chatbot dynamically fetches data for over 100 products, ensuring accurate and up-to-date responses.  

2. **Context-Aware Conversations**  
   - The system understands user intent and maintains context, making interactions fluid and relevant.  

3. **Scalable Backend Architecture**  
   - The Flask-based backend is lightweight yet robust, supporting scalability for future enhancements.  

4. **Focus on User Experience**  
   - The project emphasizes ease of use through a natural and interactive shopping interface, reducing friction in the e-commerce journey.  

5. **Seamless Dynamic Execution**  
   - All functionalities, from product search to checkout, are executed dynamically, adapting to the ever-changing inventory and user needs.  

---

## **Tech Stack**  
 
## **Tech Stack**  

- **Frontend**:  
  - **React.js**: A JavaScript library used for building the user interface, providing a responsive and dynamic experience for users.  
  - **TypeScript**: A superset of JavaScript that enables static typing, improving code quality and maintainability.  

- **Backend**:  
  - **Flask**: A lightweight web framework for Python, used for creating RESTful APIs and handling requests between the frontend and backend.  
  - **SQLite**: A self-contained, serverless SQL database engine used for managing and storing product inventory and user data.  

- **Authentication**:  
  - **JWT (JSON Web Tokens)**: Used for implementing secure user authentication. JWT allows for token-based authentication, ensuring that user sessions are securely managed.  

- **Chatbot Logic**:  
  - **Rasa**: An open-source conversational AI platform used for building the core logic of the chatbot, including natural language understanding (NLU) and dialogue management. Rasa enables efficient query handling and response generation based on user inputs.  

- **Other**:  
  - Various libraries and tools for managing RESTful APIs, handling HTTP requests, and enabling smooth integration between the frontend, backend, and chatbot system.  

This tech stack provides a robust solution for creating an interactive, secure, and efficient e-commerce sales chatbot,
with an easy-to-use frontend, a secure backend, and advanced chatbot logic for user interactions.

---

## **Setup and Installation**  
### **Prerequisites**  
[Backend]
Python 3.6 to 3.8
Flask framework and required packages
```bash  
   pip install flask cors requests sqlite3 jwt bcrypt
   ```  
SQLite Database and required tables
```bash  
   CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL);
   ```
```bash  
   CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT NOT NULL
);

   ```
```bash  
   CREATE TABLE cart (id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
price REAL NOT NULL);
);

   ```
[Chatbot]

```bash  
   pip install rasa
   ```  
```bash  
   rasa train
   ```
```bash  
   rasa run actions
   ```
```bash  
   rasa shell
   ```

## **Usage**  
Sample Chat or Training Data
[nlu.yml]
``` bash
  nlu:
- intent: greet
  examples: |
    - hey
    - hello
    - hi
    - hello there
    - good morning
    - good evening
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon

- intent: goodbye
  examples: |
    - cu
    - good by
    - cee you later
    - good night
    - bye
    - goodbye
    - have a nice day
    - see you around
    - bye bye
    - see you later

- intent: affirm
  examples: |
    - yes
    - y
    - indeed
    - of course
    - that sounds good
    - correct

- intent: deny
  examples: |
    - no
    - n
    - never
    - I don't think so
    - don't like that
    - no way
    - not really

- intent: search_product
  examples: |
    - Find me a [laptop](product)
    - Show me a [camera](product)
    - I need a [drone](product)
    - I'm looking for a [tablet](product)
    - Do you have a [phone](product)?
    - Search for a [TV](product)
    - Show me a [watch](product)
    - Find me some [headphones](product)
    - I want a [speaker](product)
    - Search for [earbuds](product)


- intent: get_product_info
  examples: |
    - Tell me more about this [Laptop Stand](product)
    - What are the features of [Phone](product)?
    - Can you give me details on [Camera](product)?
    - I want to know more about [Tablet](product)
    - Describe the [Headphones](product)
    - What's special about [Keyboard](product)?

- intent: recommend_products
  examples: |
      - Show me trending products
      - What are your bestsellers?
      - Recommend some items
      - Suggest popular products
      - What are the latest items?
      - Can you recommend something for me?
      - Show me the best products
      - Give me some product recommendations

- intent: add_to_cart
  examples: |
    - Add this to my cart
    - I want to buy this
    - Put this in my shopping cart
    - Add [product](product) to my cart
    - I'd like to purchase this [product](product)
    - Buy this item

- intent: view_cart
  examples: |
    - Show me my cart
    - What's in my shopping cart?
    - View my cart
    - I want to see what I've added
    - Show my items
    - What have I selected so far?

- intent: checkout
  examples: |
    - I'm ready to checkout
    - Proceed to payment
    - I want to pay now
    - Checkout my items
    - Complete my purchase
    - Finalize my order

- intent: clear_cart
  examples: |
    - Clear my cart
    - Remove all items from the cart
    - Empty the cart
    - Delete everything in my cart
    - I want to clear my cart
    - Clear the shopping cart
    - Empty my shopping cart
    - Remove all products from my cart
    - Reset the cart
    - Clear everything
  ```

---




---

## **API Endpoints (if applicable)**  

```plaintext  
POST /api/register - Register new user
POST /api/chat - Chatbot interface
```  

---


---

## **License**  
Mention the license your project uses (e.g., MIT License).  

---


---
