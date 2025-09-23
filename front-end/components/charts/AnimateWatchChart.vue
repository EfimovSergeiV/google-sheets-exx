<script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  import { Line } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    LineElement,
    PointElement,
    LinearScale,
    Title,
    Tooltip,
    Legend,
    CategoryScale
  } from 'chart.js'

  ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale)

  // Хранилище точек
  const labels = ref([])
  const values = ref([])

  // Инициализация с 10 пустыми точками, чтобы график сразу был построен
  for (let i = 0; i < 100; i++) {
    labels.value.push('')
    values.value.push(null)
  }

  const chartData = ref({
    labels: [...labels.value],
    datasets: [
      {
        label: 'Live Data',
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        data: [...values.value],
        // tension: 0.1,
        borderWidth: 1,
        // pointRadius: 1
      }
    ]
  })

  const chartOptions = {
    responsive: true,
    animation: false,
    // animation: {
    //   duration: 50,
    //   easing: 'linear',
    //   delay: (context) => {
    //     return context.dataIndex * 5;
    //   },
    // },
    scales: {
      x: { title: { display: true, text: 'Time' } },
      y: { min: 0, max: 500, title: { display: true, text: 'Value' } }
    }
  }

  let ws = null
  let sendInterval = null

  onMounted(() => {
    ws = new WebSocket('wss://api.meinewelt.ru/ws')

    ws.onopen = () => {
      console.log('Connected to WebSocket')

      sendInterval = setInterval(() => {
        if (ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify({ chart: 'watch' }))
        }
      }, 100)
    }

    ws.onmessage = (event) => {
      try {
        const point = JSON.parse(event.data)
        if (point.x && point.y !== undefined) {
          const timeLabel = new Date(point.x).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })

          labels.value.push(timeLabel)
          values.value.push(point.y)

          // Храним только последние 20 точек
          if (labels.value.length > 20) {
            labels.value.shift()
            values.value.shift()
          }

          // Создаём новый объект, чтобы Chart.js обновил график
          chartData.value = {
            labels: [...labels.value],
            datasets: [
              {
                label: 'Live Data',
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                data: [...values.value],
                tension: 0.1,
                pointRadius: 2
              }
            ]
          }
        }
      } catch (e) {
        console.error('Ошибка обработки WS данных:', e)
      }
    }

    ws.onclose = () => {
      console.log('WebSocket disconnected')
      clearInterval(sendInterval)
    }
  })

  onBeforeUnmount(() => {
    if (ws) ws.close()
    if (sendInterval) clearInterval(sendInterval)
  })
</script>

<template>
  <div>
    <div class="border-b">
      <p class="text-black/80 text-sm">Live data</p>
    </div>
    <div>
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>
