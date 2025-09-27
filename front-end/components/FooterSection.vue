<script setup>
  const route = useRoute()

  // const date = useAppConfig().buildDate
  //  const { $pwa } = useNuxtApp() 
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
            <nuxt-link v-if="route.name === 'sht'" :to="{ name: 'sht' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">CHT</nuxt-link>
            <nuxt-link v-else :to="{ name: 'sht' }" class="font-semibold italic uppercase text-xs md:text-lg">SHT</nuxt-link>
          </div>
          <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
          <div class="">
            <nuxt-link v-if="route.name === 'm1-5'" :to="{ name: 'm1-5' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
            <nuxt-link v-else :to="{ name: 'm1-5' }" class="font-semibold italic uppercase text-xs md:text-lg">M1-5</nuxt-link>
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