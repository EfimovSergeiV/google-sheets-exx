<script setup>
  const route = useRoute()



</script>



<template>
  <div class="container mx-auto px-4">
    <div class="flex flex-row items-center w-full justify-between py-4 text-gray-100 dark:text-gray-100">
      
      <div class="">
        <nuxt-link :to="{ name: 'index' }">
          <p>Index</p>       
        </nuxt-link>
      </div>

      <div class="flex flex-row items-center gap-2 md:gap-4 ">
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
</template>