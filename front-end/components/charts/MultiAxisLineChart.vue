

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js'

ChartJS.register(
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
)

const chartData = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Dataset 1 (Левая ось)',
      data: [100, 200, 150, 300, 250, 400, 350, 400, 450, 500, 600, 700, 800],
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      yAxisID: 'y',
    },
    {
      label: 'Dataset 2 (Правая ось)',
      data: [10, 30, 50, 20, 60, 90, 70],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.5)',
      yAxisID: 'y1',
    }
  ]
}

const chartOptions = {
  responsive: true,
  maintainAspectRatio: true, // чтобы размеры работали через CSS
  interaction: {
    mode: 'index',
    intersect: false,
  },
  stacked: false,
  plugins: {
    title: {
      display: true,
      text: 'Multi-Axis Line Chart',
    },
    legend: {
      position: 'top'
    }
  },
  scales: {
    y: {
      type: 'linear',
      display: true,
      position: 'left',
    },
    y1: {
      type: 'linear',
      display: true,
      position: 'right',
      grid: {
        drawOnChartArea: false,
      }
    }
  }
}
</script>

<template>
  <div>
    <div class="border-b">
      <p class="text-black/80 text-sm">Multi-Axis Line Chart</p>
    </div>
    <div class="h-full">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<!-- <style scoped>
.chart-container {
  width: 420px;
  height: 300px;
}
</style> -->
