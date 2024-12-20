import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./register.css"

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate(); // Hook for navigation

  const handleRegister = async () => {
    console.log({ name, email, password });

    try {
      const response = await fetch("http://localhost:5001/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });

      const data = await response.json();
      console.log("Response Data:", data);

      if (response.status === 400) {
        setMessage(data.message || "Registration failed");
      } else {
        setMessage("Registration successful!");
        setTimeout(() => {
          navigate("/chat"); // Redirect to the chat interface
        }, 1500); // Add a slight delay to show the success message
      }
    } catch (err) {
      setMessage("An error occurred");
      console.error("Error:", err);
    }
  };

  return (
    <div className="register-container">
      <h2>Register 👨🏻‍💻</h2>
      {message && <p className="message">{message}</p>}
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}
