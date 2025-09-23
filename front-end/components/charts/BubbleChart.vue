<script setup>
  import { Bubble } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    PointElement,
    LinearScale
  } from 'chart.js'

  ChartJS.register(Title, Tooltip, Legend, PointElement, LinearScale)

  const chartData = {
    datasets: [
      {
        label: 'Label 1',
        data: [
          { x: 20, y: 30, r: 15 },
          { x: 40, y: 10, r: 10 },
          { x: 80, y: 80, r: 10 },
          { x: 15, y: 25, r: 8 },
          { x: 35, y: 5, r: 12 },
          { x: 25, y: 35, r: 7 }
        ],
        backgroundColor: 'rgba(255, 99, 132, 0.5)'
      },
      {
        label: 'Label 2',
        data: [
          { x: 12, y: 30, r: 15 },
          { x: 20, y: 20, r: 10 },
          { x: 30, y: 40, r: 10 },
          { x: 50, y: 60, r: 8 },
          { x: 70, y: 70, r: 12 },
          { x: 90, y: 90, r: 7 }
        ],
        backgroundColor: 'rgba(54, 162, 235, 0.5)'
      },
    ]
  }

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top'
      },
      title: {
        display: true,
        text: 'Пример Bubble Chart'
      }
    }
  }

</script>


<template>
  <div class="">


    <div class="border-b">
      <p class="text-black/80 text-sm">Bubble chart</p>
    </div>
    <div class="">
      <Bubble :data="chartData" :options="chartOptions" />
    </div>

  </div>
</template>