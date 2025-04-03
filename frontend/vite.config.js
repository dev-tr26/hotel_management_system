import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,   // Ensure it's running on this port
    open: true,   // Automatically opens the page when you run npm start
  }
});
