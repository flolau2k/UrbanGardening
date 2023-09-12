/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,vue}'],
  theme: {
    extend: {
      colors: {
        darkBlack: '#181818',
        mindaro: '#d9ed92ff',
        lightGreen: '#b5e48cff',
        lightGreen2: '#99d98cff',
        kindagreen: '#76c893ff',
        greenBluish: '#52b69aff',
        greenishBlue: '#34a0a4ff',
        lightBlue: '#168aadff',
        blue: '#1a759fff',
        darkBlue: '#1e6091ff',
        darkestBlue: '#184e77ff'
      }
    }
  },
  plugins: []
}
