<script setup>
  const ctx = useNuxtApp()



  const firstButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('FIRST_BUTTON')
    }
  }

  const secondButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('SECOND_BUTTON')
    }
  }

  const thirdButton = () => {
    if (import.meta.client) {
      ctx.$metrika.reachGoal('THIRD_BUTTON')
    }
  }

  const latestButton = ref("")
  const counterButton = ref(null)
  const changeLatest = (latest) => {
    if ( latestButton.value === latest ) {
      counterButton.value = counterButton.value + 1
    } else {
      latestButton.value = latest
      counterButton.value = null     
    }
  }

</script>

<template>
  <div class="container mx-auto px-4 py-8">

    <p class="text-white text-2xl font-bold mb-4">About Page</p>
    <p class="text-white text-xl">This is the about page content.</p>

  </div>
</template>