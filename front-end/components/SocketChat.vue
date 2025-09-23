<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

// const wsUrl = "ws://127.0.0.1:8000/chat";
const wsUrl = "wss://api.meinewelt.ru/chat";

const messages = ref([]); // массив сообщений [{text, time}]
const message = ref("");
let socket = null;

const connectionID = ref(null);

const connectWebSocket = () => {
  socket = new WebSocket(wsUrl);

  socket.onopen = () => {
    console.log("WebSocket соединение установлено");
  };

  socket.onmessage = (event) => {

    try {
      const data = JSON.parse(event.data)

      // Проверяем, есть ли connection_id
      if (data.connection_id) {
        connectionID.value = data.connection_id;
      } else {
        if (Array.isArray(data)) {
          messages.value = data;
        } else {
          messages.value.push(data);

          // Ограничиваем количество сообщений до 6 последних
          if (messages.value.length > 5) {
            messages.value.shift();
          }
        }        
      }

      /// Если массив объектов, тогда message = data, иначе message.push(data)


    } catch (e) {
      console.error("Ошибка парсинга:", e);
    }
  };

  socket.onclose = () => {
    console.log("WebSocket закрыт, переподключение...");
    setTimeout(connectWebSocket, 1000);
  };
};

const sendMessage = () => {
  if (socket && socket.readyState === WebSocket.OPEN && message.value.trim()) {
    socket.send(message.value);
    message.value = "";
  }
};

onMounted(() => connectWebSocket());
onBeforeUnmount(() => socket?.close());
</script>

<template>
  <div class="">
    <div class="flex items-center justify-center">

    <div class="grid grid-cols-1 gap-4">

      <!-- Список сообщений -->
      <div class="">
        <div class="rounded-lg shadow-inner mb-4 grid grid-cols-1 gap-2">

          <!-- Отображаем только 3 последних -->
          <div v-for="(msg, i) in messages" :key="i" class="">
            <!-- проверяем кратность двум -->
             <div v-if="connectionID === msg.client_id" class="flex justify-end">
              <div class="mb-2 p-2 rounded-lg bg-blue-100/50 w-[500px]">
                <div class="flex items-center justify-between border-b border-gray-300/50 pb-1 mb-1">
                  <div class="text-xs text-gray-300">{{ msg.client_id }}</div>
                  <div class="text-xs text-gray-300 font-semibold">{{ msg.time }}</div>
                </div>

                <div class="text-white text-sm">{{ msg.text }}</div>
              </div>                 
             </div>
             <div v-else>
              <div class="mb-2 p-2 rounded-lg bg-green-100/50 w-[500px]">
                <div class="flex items-center justify-between border-b border-gray-300/50 pb-1 mb-1">
                  <div class="text-xs text-gray-300">{{ msg.client_id }}</div>
                  <div class="text-xs text-gray-300 font-semibold">{{ msg.time }}</div>
                </div>
                <div class="text-white text-sm">{{ msg.text }}</div>
              </div>
             </div>
          </div>

        </div>        
      </div>


      <!-- Поле ввода -->
      <div class=" ">
        <div>
          <p class="text-white text-xs pb-1">con_id: {{ connectionID }}</p>
          <textarea
            v-model="message"
            rows="3"
            class="px-4 py-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 w-full md:w-[600px] bg-white/60"
            placeholder="Напишите сообщение..."
            @keydown.enter.exact.prevent="sendMessage"
          />    
        </div>
        <div>
          <button
            class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            @click="sendMessage"
          >
            Отправить
          </button>          
        </div>


      </div>

    </div>


    </div>

  </div>
</template>
