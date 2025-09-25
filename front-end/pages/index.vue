<script setup>
  const config = useRuntimeConfig()


  const data = await $fetch(`${ config.public.baseURL }heroes/`, { method: 'GET' }).catch( () => {
    return [
          {
              "err": "Нет данных",
          },
      ]
  }
)

</script>


<template>
  <div class="container mx-auto px-4">
    
    <div class="text-gray-100 dark:text-gray-100">

      <p class="pb-4">index:</p>





    </div>

  </div>
</template>