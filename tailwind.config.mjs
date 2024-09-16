/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        textColor: {
          light: "#394132",
          dark: "#A7BF8F",
        },
        mainColor: {
          light: "#005600",
          dark: "#394132",
        },
      },
    },
  },
  plugins: [],
};
