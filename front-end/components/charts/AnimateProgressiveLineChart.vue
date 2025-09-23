<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
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
  CategoryScale
)

const chartData = ref({
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Dataset 1',
      data: [100, 200, 150, 300, 250, 400, 350],
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      yAxisID: 'y',
    },
    {
      label: 'Dataset 2',
      data: [10, 30, 50, 20, 60, 90, 70],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.5)',
      yAxisID: 'y',
    },
  ],
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
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
      position: 'top',
    },
  },
  interaction: {
    intersect: false,
  },
  scales: {
    y: {
      type: 'linear',
      display: true,
      position: 'left',
    },
  },
  animation: {
    duration: 2000,
    easing: 'linear',
    delay: (context) => {
      return context.dataIndex * 300;
    },
  },
}

const chartRef = ref(null)

const wsState = ref('')

const wsUrl = `wss://api.meinewelt.ru/ws`
let socket = null

const debug = ref('')

function connectWebSocket() {
  socket = new WebSocket(wsUrl)

  socket.onopen = () => {
    wsState.value = 'connected'
  }

  socket.onmessage = (event) => {
    try {
      const newData = JSON.parse(event.data)

      if (Array.isArray(newData) && newData[0]?.data) {
        const chartInstance = chartRef.value?.chart
        if (chartInstance) {
          chartInstance.data.datasets = newData
          debug.value = newData
          chartInstance.update()
        }
      }
    } catch (e) {
      console.error('Ошибка парсинга данных', e)
    }
  }

  socket.onclose = () => {
    console.log('Соединение закрыто, переподключение...')
    setTimeout(connectWebSocket, 1000)
  }
}

setInterval(() => {
  if (socket?.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({ chart: 'multiline' }))
  }
}, 3000)

onMounted(connectWebSocket)
onUnmounted(() => socket?.close())
</script>


<template>
  <div>
    <div class="border-b">
      <p class="text-black/80 text-sm">Multi-Axis Line chart 2</p>
    </div>
    <div class="h-full">
      <Line ref="chartRef" :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>
