import React, { useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import { useTheme } from "./context/ThemeContext.jsx";
import "./App.css";
import Navbar from "./pages/Component/Navbar/Navbar.jsx";
import Home from "./pages/home/home.jsx";
import About from "./pages/About_us/About.jsx";
import Room from "./pages/Room/Room.jsx";
import Contact from "./pages/contact_us/contact.jsx";
// import Help from "./pages/Help/help.jsx";
import Book from "./pages/Book-1/book.jsx";
import Info from "./hotel_info/information/info.jsx";
import Rules from "./hotel_info/rules/rules.jsx";
import Login from "./pages/Component/auth/login/login.jsx";
import Register from "./pages/Component/auth/register/register.jsx";
import Freewifi from "./Services/Free-wifi/Free_wifi.jsx";
import Spa from "./Services/Luxury spa/spa.jsx";
import Pool from "./Services/Swimming-pool/pool.jsx";
import Bar from "./Services/Bars/bar.jsx";
import Fitness from "./Services/Fitness_center/fitness.jsx";
import Movie from "./Services/Movie_theater/movie.jsx";
import Footer from "./pages/Component/Footer/Footer.jsx";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

function App() {
  const { isDarkMode } = useTheme(); // Removed unused `toggleDarkMode`

  // Apply dark-mode class to body globally
  useEffect(() => {
    document.body.classList.toggle("dark-mode", isDarkMode);
  }, [isDarkMode]);

  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/room" element={<Room />} />
        <Route path="/contact" element={<Contact />} />
        {/* <Route path="/help" element={<Help />} /> */}
        <Route path="/book1" element={<Book />} />
        <Route path="/info" element={<Info />} />
        <Route path="/rules" element={<Rules />} />
        <Route path="/free-wifi" element={<Freewifi />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/spa" element={<Spa />} />
        <Route path="/pool" element={<Pool />} />
        <Route path="/bar" element={<Bar />} />
        <Route path="/movie" element={<Movie />} />
        <Route path="/fitness" element={<Fitness />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
