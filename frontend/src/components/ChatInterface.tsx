import React, { useState, useRef, useEffect } from "react";

type Message = {
  sender: "user" | "bot";
  text: string;
};

export default function EcommerceSalesChatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const chatMessagesRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatMessagesRef.current) {
      chatMessagesRef.current.scrollTop = chatMessagesRef.current.scrollHeight;
    }
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { sender: "user", text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await fetch("http://localhost:5001/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();
      if (data.messages) {
        const botMessages = data.messages.map((msg: string) => ({
          sender: "bot",
          text: msg,
        }));
        setMessages((prevMessages) => [...prevMessages, ...botMessages]);
      }
    } catch (error) {
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: "bot", text: "Error connecting to the chatbot. Please try again." },
      ]);
    }

    setInput("");
  };

  return (
    <>
      <button className="chat-button" onClick={() => setIsOpen(true)}>
        🤖
        💬
      </button>
      {isOpen && (
        <div className="chat-modal">
          <div className="chat-header">
            <div>Ecommerce Sales Chatbot</div>
            <button className="close-button" onClick={() => setIsOpen(false)}>
               ❌
            </button>
          </div>
          <div className="chat-container">
            <div className="chat-messages" ref={chatMessagesRef}>
              {messages.map((msg, index) => (
                <div key={index} className={`chat-message ${msg.sender}`}>
                  {msg.text}
                </div>
              ))}
            </div>
          </div>
          <div className="chat-input-container">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === "Enter" && sendMessage()}
              className="chat-input"
              placeholder="Type your message..."
            />
            <button onClick={sendMessage} className="chat-send-button">
             📨
            </button>
          </div>
        </div>
      )}
    </>
  );
}
