/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    colors: {
      'white': '#ffffff',
      'light': '#f4f0e5',
      'color': '#b8cfa3',
      'dark-green': '#394132',
      'black': '#303030',
      'accent': '#a62f03',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    spacing: {
      'Headline-1': '5.852rem',
      'Headline-2': '4.18rem',
      'Headline-3': '2.5rem',
      'Subheadline': '1.67rem',
      'Text': '1.33rem',
      'Caption': '1rem'
    },
  },
  plugins: [],
};
