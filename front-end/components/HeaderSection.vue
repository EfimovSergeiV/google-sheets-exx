<script setup>
  const route = useRoute()

  // const config = useRuntimeConfig()
  // const data = await $fetch(`${ config.public.baseURL }heroes/`

  const wsUrl = "ws://127.0.0.1:8000/time";
  // const wsUrl = "wss://api.meinewelt.ru/chat";

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
  <div class="container mx-auto px-4">
    <div class="flex flex-row items-center w-full justify-between py-4 text-gray-100 dark:text-gray-100">
      
      <div class="">
        <nuxt-link :to="{ name: 'index' }">
          <p>BETA</p>       
        </nuxt-link>
      </div>

      <div class="flex flex-row items-center gap-2 md:gap-4 ">
        <div>
          <nuxt-link v-if="route.name === 'index'" :to="{ name: 'index' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">INX</nuxt-link>
          <nuxt-link v-else :to="{ name: 'index' }" class="font-semibold italic uppercase text-xs md:text-lg">INX</nuxt-link>
        </div>
        <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
        <div class="">
          <nuxt-link v-if="route.name === 'cht'" :to="{ name: 'cht' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">CHT</nuxt-link>
          <nuxt-link v-else :to="{ name: 'cht' }" class="font-semibold italic uppercase text-xs md:text-lg">CHT</nuxt-link>
        </div>
        <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
        <div class="">
          <nuxt-link v-if="route.name === 'exx'" :to="{ name: 'exx' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
          <nuxt-link v-else :to="{ name: 'exx' }" class="font-semibold italic uppercase text-xs md:text-lg">EXX</nuxt-link>
        </div>
        <p class="font-semibold italic uppercase text-sm md:text-2xl">/</p>
        <div class="">
          <nuxt-link v-if="route.name === 'abt'" :to="{ name: 'abt' }" class="text-red-700 font-semibold italic uppercase text-xs md:text-lg">ABT</nuxt-link>
          <nuxt-link v-else :to="{ name: 'abt' }" class="font-semibold italic uppercase text-xs md:text-lg">ABT</nuxt-link>
        </div>
      </div>

    </div>
  </div>
</template>