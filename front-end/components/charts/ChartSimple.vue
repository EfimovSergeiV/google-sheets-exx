<script setup>
  import { Bar } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
  } from 'chart.js'

  // Регистрируем модули Chart.js
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

  // Простые данные
  const chartData = {
    labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    datasets: [
      {
        label: 'Значения',
        backgroundColor: '#3b82f6',
        data: [10, 20, 15, 30, 25, 35, 40],
      }
    ]
  }
</script>


<template>
  <div class="">
    

    <div class="border-b">
      <p class="text-black/80 text-sm">Simple chart</p>
    </div>
    <div class="">
      <Bar :data="chartData" />      
    </div>


  </div>
</template>