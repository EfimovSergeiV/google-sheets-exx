<script setup>
  const config = useRuntimeConfig()


  const m1 = await $fetch(`${ config.public.baseURL }m/1`, { method: 'GET' }).catch( () => {
    return [
          {
              "err": "Нет данных",
          },
      ]
  }
)

</script>


<template>
  <div class="container mx-auto p-4">
    <div class="text-gray-100">
      <div class="mb-6 grid grid-cols-1 gap-2">
        <p class="text-white text-xl">M1-5</p>
      </div>

      <div class="">
        <p>{{ m1 }}</p>
      </div>

    </div>


  </div>
</template>