<script setup>
  // eslint-disable-next-line no-unused-vars, vue/require-prop-types
  const props = defineProps(['skills',])


</script>

<template>
  <div class="flex flex-wrap gap-4 text-white dark:text-white">
    
    <div v-for="skill in skills" :key="skill.id" class="">
      <div class="bg-cyan-900/70 border border-cyan-500/50 rounded-full px-6 py-1">
        <p>{{ skill.name }}</p>
      </div>
    </div>

  </div>

</template>