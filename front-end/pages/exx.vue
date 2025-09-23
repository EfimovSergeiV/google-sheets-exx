<script setup>
  import ChartSimple from '@/components/charts/ChartSimple.vue'
  import BubbleChart from '@/components/charts/BubbleChart.vue'
  import MultiAxisLineChart from '@/components/charts/MultiAxisLineChart.vue'

  import AnimateBubbleChart from '@/components/charts/AnimateBubbleChart.vue'
  import AnimateChartSimple from '@/components/charts/AnimateChartSimple.vue'
  import AnimateMultiAxisLineChart from '@/components/charts/AnimateMultiAxisLineChart.vue'
  import AnimateProgressiveLineChart from '@/components/charts/AnimateProgressiveLineChart.vue'
  import AnimateWatchChart from '@/components/charts/AnimateWatchChart.vue'



  const copyToClipboardCMD = (cmd) => {
    navigator.clipboard.writeText(cmd)
      .then(() => {
        alert('Команда скопирована в буфер обмена!')
      })
      .catch(err => {
        console.error('Ошибка копирования:', err)
        alert('Не удалось скопировать команду')
      })
  }


  const copyToClipboard = async (filename) => {
    try {
      const res = await fetch(`https://raw.githubusercontent.com/EfimovSergeiV/meinewelt/main/mw-nuxt-2/${filename}.vue`)
      if (!res.ok) throw new Error('Файл не найден')
      const text = await res.text()

      await navigator.clipboard.writeText(text)
      alert('Код скопирован в буфер обмена!')
    } catch (err) {
      console.error('Ошибка копирования:', err)
      alert('Не удалось скопировать файл')
    }
  }
</script>


<template>
  <div class="container mx-auto p-4">
    <div class="">
      <div class="mb-6 grid grid-cols-1 gap-2">
        <p class="text-white text-xl">Chart.js</p>

        
      </div>


    </div>


  </div>
</template>