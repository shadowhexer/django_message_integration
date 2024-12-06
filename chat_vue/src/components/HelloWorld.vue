<script setup lang="ts">
import { ref, onMounted } from 'vue';
import API from '@/services/api';

const message = ref('');

onMounted(async () => {
  try {
    const response = await API.get('chat/');
    console.log(response)
    message.value = response.data;
  } catch (error) {
    console.error(error);
  }
})

defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3 class="text-white">{{ message }}</h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
