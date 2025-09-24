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

      <p class="pb-4">table data:</p>


        <div class="relative overflow-x-auto mt-8">
          <table class="w-full text-left text-gray-500 dark:text-gray-400">
              <thead class="text-gray-700 uppercase  dark:text-gray-400">
                  <tr class="bg-gray-800 border border-gray-500 hover:bg-gray-600">
                    <th v-for="key in [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC']" :key="key" scope="col" class="px-6 py-3 text-gray-200 text-xs">
                      <p class="text-sm">{{ data[0][key] }}</p>
                    </th>
                  </tr>
              </thead>
              <tbody>

                <tr v-for="item in data.slice(1)" :key="item.id" class=" dark:bg-gray-800 border border-gray-500 hover:bg-gray-600">
                  <th v-for="value in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC']" :key="value" scope="row" class="px-6 py-4 text-gray-100 w-[400px] text-xs">
                    <p class="text-xs">{{ item[value] }}</p>
                  </th>
                </tr>
              </tbody>
          </table>
      </div>


    </div>

  </div>
</template>