import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Register from "./components/Register";
import Login from "./components/Login";
import ChatInterface from "./components/ChatInterface";
import "./App.css"
import "./components/register.css"

const App = () => {
  return (
    <Router>
      <div className="container">
        <h1>Welcome to E-Commerce Sales Chatbot</h1>
        <div className="bot-icon">
        <img src="src/assets/bot.png" height={100} width={100}></img>
        </div>
        <Routes>
          <Route path="/" element={<Navigate to="/register" />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/chat" element={<ChatInterface />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
