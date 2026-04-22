
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./core/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        gold: '#C8A97E',
        dark: '#1E1E1E',
      }
    },
  },
  plugins: [],
}
