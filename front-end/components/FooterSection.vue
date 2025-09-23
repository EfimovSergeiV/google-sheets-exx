<script setup>
  // If you want to use it in setup, import from the nuxtApp.
  const { $pwa } = useNuxtApp()
  const route = useRoute()
  const date = useAppConfig().buildDate
  // const toast = useToast()


</script>


<template>
  <div class="text-gray-100 dark:text-gray-100">
    <div class="py-2 min-h-32 flex flex-col items-center justify-end">

      <div class="container mx-auto px-8">


        <div class="flex flex-row items-center justify-center gap-4 py-2">
          <div>
            <nuxt-link v-if="route.name === 'index'" :to="{ name: 'index' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">INX</nuxt-link>
            <nuxt-link v-else :to="{ name: 'index' }" class="font-semibold italic uppercase text-xs md:text-lg">INX</nuxt-link>
          </div>
          <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
          <div class="">
            <nuxt-link v-if="route.name === 'cht'" :to="{ name: 'cht' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">CHT</nuxt-link>
            <nuxt-link v-else :to="{ name: 'cht' }" class="font-semibold italic uppercase text-xs md:text-lg">CHT</nuxt-link>
          </div>
          <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
          <div class="">
            <nuxt-link v-if="route.name === 'exx'" :to="{ name: 'exx' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
            <nuxt-link v-else :to="{ name: 'exx' }" class="font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
          </div>
          <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
          <div class="">
            <nuxt-link v-if="route.name === 'abt'" :to="{ name: 'abt' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">ABT</nuxt-link>
            <nuxt-link v-else :to="{ name: 'abt' }" class="font-semibold italic uppercase text-xs md:text-lg">ABT</nuxt-link>
          </div>
        </div>





      </div>
    </div>

  </div>
</template>