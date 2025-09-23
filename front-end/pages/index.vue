<script setup>
  const config = useRuntimeConfig()


  const skills = await $fetch(`${ config.public.baseURL }bl/skills/`, { method: 'GET' }).catch( () => {
    return [
          {
              "id": 1,
              "name": "GNU/Linux",
              "skill": true
          },
          {
              "id": 2,
              "name": "Debian",
              "skill": true
          },
          {
              "id": 3,
              "name": "Python",
              "skill": true
          },
          {
              "id": 4,
              "name": "Django",
              "skill": true
          },
          {
              "id": 5,
              "name": "FastAPI",
              "skill": true
          },
          {
              "id": 6,
              "name": "JavaScript",
              "skill": true
          },
          {
              "id": 7,
              "name": "VueJS",
              "skill": true
          },
          {
              "id": 8,
              "name": "NuxtJS",
              "skill": true
          },
          {
              "id": 9,
              "name": "TailwindCSS",
              "skill": true
          }
      ]
  }
)

</script>


<template>
  <div class="container mx-auto px-8">
    
    <div class="text-gray-100 dark:text-gray-100">

      index page

    </div>

  </div>
</template>