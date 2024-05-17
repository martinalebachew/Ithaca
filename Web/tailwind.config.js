const config = {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],

  plugins: [require('flowbite/plugin')],

  darkMode: 'selector',

  theme: {
    extend: {
      colors: {
        // flowbite-svelte
        primary: {
          50: '#8DAA31',
          100: '#8DAA31',
          200: '#8DAA31',
          300: '#8DAA31',
          400: '#8DAA31',
          500: '#8DAA31',
          600: '#8DAA31',
          700: '#8DAA31',
          800: '#8DAA31',
          900: '#8DAA31'
        }
      }
    }
  }
};

module.exports = config;