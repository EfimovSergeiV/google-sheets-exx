<script setup>
  // const config = useRuntimeConfig()

  // If you want to use it in setup, import from the nuxtApp.
  // const { $pwa } = useNuxtApp()
  // const date = useAppConfig().buildDate
  // const toast = useToast()


</script>

<template>
  <div class="bg-fixed bg-no-repeat bg-cover bg-center min-h-screen bg-gray-700">

    <div class="">
      <div class="min-h-screen flex flex-col justify-between">
        <HeaderSection />
        <slot />
        <FooterSection />
      </div>
    </div>
    
  </div>
</template>