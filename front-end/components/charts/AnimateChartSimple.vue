<script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import { Bar } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
  } from 'chart.js'

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


  const chartData = ref({
    labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    datasets: [
      {
        label: 'Продажи',
        backgroundColor: '#3b82f6',
        data: [10, 20, 15, 30, 25, 35, 40]
      }
    ]
  })

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        min: 0,
        max: 300,
        ticks: {
          stepSize: 10
        }
      }
    }
  }


  const chartRef = ref(null)

  const wsState = ref('')

  const wsUrl = `wss://api.meinewelt.ru/ws`
  let socket = null

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
            chartInstance.data.datasets[0].data = newData[0].data
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
      socket.send(JSON.stringify({ chart: 'bar' }))
    }
  }, 3000)

  onMounted(connectWebSocket)
  onUnmounted(() => socket?.close())


</script>


<template>
  <div class="flex flex-col justify-between h-full">

    <div class="border-b">
      <p class="text-black/80 text-sm">Simple chart</p>
    </div>
    <div class="">
      <Bar ref="chartRef" :data="chartData" :options="chartOptions" />      
    </div>

  </div>
</template>