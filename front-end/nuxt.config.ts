import cfg from "./conf"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-06-18',
  devtools: { enabled: false },

  vite: {
    server: {
      allowedHosts: ['mw.ru'],
    }
  },

  app: {
    head: {
      title: 'mw.RU',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ],
    },

    pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/scripts',
    '@tresjs/nuxt',
  ],
  css: [
    '~/assets/css/tailwind.css',
    '~/assets/css/main.css',
    // '@mdi/font/css/materialdesignicons.min.css',
  ],

  tres: {
    glsl: true,
  },

  appConfig: {
    // you don't need to include this: only for testing purposes
    buildDate: new Date().toISOString(),
  },
  
  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || cfg.BASE_URL,
      wsURL: process.env.BASE_URL || cfg.WS_URL,
    },
  },
})