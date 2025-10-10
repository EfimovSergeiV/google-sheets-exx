<script setup>
  const config = useRuntimeConfig()

  // Actions
  const loadSheets = () => {
    $fetch(`${ config.public.baseURL }load_sheets/`, { method: 'GET' }).catch( () => { return [{"err": "Нет данных",},]})
  }
  const writeSheets = () => {
    $fetch(`${ config.public.baseURL }write_sheets/`, { method: 'GET' }).catch( () => { return [{"err": "Нет данных",},]})
  }


  // Get data
  const sourceTable = await $fetch(`${ config.public.baseURL }heroes/`, { method: 'GET' }).catch( () => {
    return [
          {
              "err": "Нет данных",
          },
      ]
    }
  )

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
  <div class="container mx-auto px-4">
    
    <div class="mb-2">
      <div class="flex gap-4 text-gray-100 dark:text-gray-100">
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none" @click="loadSheets()">Загрузка данных</button>
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none" @click="writeSheets()">Записать в БД</button>
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none">Распланировать</button>
        <button class="bg-blue-700 active:bg-blue-800 border border-cyan-600 active:border-cyan-500 text-white px-6 py-2 transition-all duration-100 select-none">Отправить</button>
      </div>
    </div>



    <div class="text-gray-100">
      
      <div class="text-gray-100 dark:text-gray-100 mb-6">
        <div v-if="sourceTable.length > 0" class="relative overflow-y-auto h-[300px] overflow-x-auto">
          <table class="w-full text-left text-gray-500 dark:text-gray-400">
              <thead class="text-gray-700 uppercase dark:text-gray-400 sticky top-0">
                  <tr class="bg-gray-800 border border-gray-500 hover:bg-gray-600">
                    <th v-for="key in Object.keys(sourceTable[0])" :key="key" scope="col" class="px-6 py-3 text-gray-200 text-xs">
                      <p class="text-sm">({{ key }}) {{ sourceTable[0][key] }}</p>
                    </th>
                  </tr>
              </thead>
              <tbody class="">

                <tr v-for="item in sourceTable.slice(1)" :key="item.id" class=" dark:bg-gray-800 border border-gray-500 hover:bg-gray-600">
                  <th v-for="value in  Object.keys(sourceTable[0])" :key="value" scope="row" class="px-6 py-4 text-gray-100 text-xs">
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
      
      
      
      <div class="mb-6 grid grid-cols-1 gap-2">
        <p class="text-white text-xl">M:</p>
      </div>


      <div class="grid grid-cols-5 gap-4">
        <div v-for="mm in Object.keys(mms)" :key="mm" class="">
          <div class="grid grid-cols-1 gap-2">
            <div v-for="(data, pk) in mms[mm]" :key="data" class="">
              <div class="w-64 text-xs"><p>{{ pk }}. {{ data }}</p></div>
            </div>            
          </div>
        </div>        
      </div>


    </div>

  </div>
</template>