/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        Turquoise: ["Turquoise", "Crimson Text", "sans-serif"],
        "Plus-Jakarte-Sans": ["Plus Jakarte Sans", "Arima", "serif"],
      },
      colors: {
        white: "#ffffff",
        light: "#f4f0e5",
        color: "#b8cfa3",
        "dark-green": "#394132",
        "true-black": "#000",
        black: "#303030",
        accent: "#a62f03",
      },
    },
  },
  plugins: [],
};
