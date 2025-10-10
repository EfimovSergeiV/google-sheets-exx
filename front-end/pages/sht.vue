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


        <div v-if="data.length > 0" class="relative overflow-y-auto h-[600px] overflow-x-auto">
          <table class="w-full text-left text-gray-500 dark:text-gray-400">
              <thead class="text-gray-700 uppercase dark:text-gray-400 sticky top-0">
                  <tr class="bg-gray-800 border border-gray-500 hover:bg-gray-600">
                    <th v-for="key in Object.keys(data[0])" :key="key" scope="col" class="px-6 py-3 text-gray-200 text-xs">
                      <p class="text-sm">{{ data[0][key] }}</p>
                    </th>
                  </tr>
              </thead>
              <tbody class="">

                <tr v-for="item in data.slice(1)" :key="item.id" class=" dark:bg-gray-800 border border-gray-500 hover:bg-gray-600">
                  <th v-for="value in  Object.keys(data[0])" :key="value" scope="row" class="px-6 py-4 text-gray-100 text-xs">
                    <p class="text-xs  min-w-[150px]">{{ item[value] }}</p>
                  </th>
                </tr>
              </tbody>
          </table>
      </div>

      <div v-else class="flex items-center justify-center">
        <p class="">Нет данных</p>
      </div>


    </div>

  </div>
</template>