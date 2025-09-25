<script setup>
  const config = useRuntimeConfig()


//   const data = await $fetch(`${ config.public.baseURL }heroes/`, { method: 'GET' }).catch( () => {
//     return [
//           {
//               "err": "Нет данных",
//           },
//       ]
//   }
// )

const loadSheets = () => {
  $fetch(`${ config.public.baseURL }load_sheets/`, { method: 'GET' }).catch( () => { return [{"err": "Нет данных",},]})
}

const writeSheets = () => {
  $fetch(`${ config.public.baseURL }write_sheets/`, { method: 'GET' }).catch( () => { return [{"err": "Нет данных",},]})
}

</script>


<template>
  <div class="container mx-auto px-4">
    
    <div class="text-gray-100 dark:text-gray-100">

      <p class="pb-4">index:</p>



      <div class="flex gap-4">
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none" @click="loadSheets()">Скачать в файл</button>
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none" @click="writeSheets()">Сохранить в БД</button>
      </div>



    </div>

  </div>
</template>