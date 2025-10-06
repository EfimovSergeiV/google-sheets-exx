<script setup>
  const config = useRuntimeConfig()


  const mms = await $fetch(`${ config.public.baseURL }m/all/`, { method: 'GET' }).catch( () => {
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

      
      <div class="grid grid-cols-5 gap-4">
        <div v-for="mm in Object.keys(mms)" :key="mm" class="">
          
          <div v-for="(data, pk) in mms[mm]" :key="data" class="">
            <div class="w-64 text-xs"><p>{{ pk }}. {{ data }}</p></div>
          </div>
          
        </div>        
      </div>


    </div>


  </div>
</template>