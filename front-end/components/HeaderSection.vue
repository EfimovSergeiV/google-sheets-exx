<script setup>
  const route = useRoute()
  const config = useRuntimeConfig()

  const wsUrl = `${ config.public.baseURL }time`;
  const nowDateTime = ref("00.00.0000 00:00:00")
  let socket = null;

  const connectWebSocket = () => {
    socket = new WebSocket(wsUrl);

    socket.onopen = () => {
      console.log("WebSocket соединение установлено");
    };

    socket.onmessage = (event) => {
      try {
        nowDateTime.value = event.data
      } catch (e) {
        console.error("Ошибка парсинга:", e);
      }
    };

    socket.onclose = () => {
      console.log("WebSocket закрыт, переподключение...");
      setTimeout(connectWebSocket, 1000);
    };
  };

  onMounted(() => connectWebSocket());
  onBeforeUnmount(() => socket?.close());

</script>



<template>
  <div class="container mx-auto px-4">
    <div class="flex flex-row items-center w-full justify-between py-4 text-gray-100 dark:text-gray-100">
      
      <div class="flex gap-4">
        <nuxt-link :to="{ name: 'index' }">
          <p class="font-semibold">BETA</p>
        </nuxt-link>
        <p>{{ nowDateTime }}</p>
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