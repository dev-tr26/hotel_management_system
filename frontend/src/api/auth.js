const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/authentication/";

export const authService = {
  login: async (email, password) => {
    const response = await fetch(`${API_URL}login/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error("Invalid email or password");
    }

    const data = await response.json();
    localStorage.setItem("token", data.access); // Store JWT token
  },

  isAuthenticated: () => {
    return !!localStorage.getItem("token"); // Check if token exists
  },

  logout: () => {
    localStorage.removeItem("token"); // Clear token on logout
  },
};
