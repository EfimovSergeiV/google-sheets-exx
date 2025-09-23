module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
  ],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': ['Play-Regular', 'ui-serif', 'Arial', 'sans-serif',],
      'serif': ['Play-Regular', 'ui-serif', 'Arial', 'sans-serif',],
      'mono': ['Play-Regular', 'ui-serif', 'Arial', 'sans-serif',],
      'display': ['Play-Regular', 'ui-serif', 'Arial', 'sans-serif',],
      'body': ['Play-Regular', 'ui-serif', 'Arial', 'sans-serif',],

    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
