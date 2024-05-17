<template>
  <div>
    <p>{{ username }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import axios from 'axios';

const store = useMovieStore();
const username = ref(null);

const getProfile = function() {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/profile/${store.username}`
  })
  .then((res) => {
    username.value = res.data.username
  })
  .catch(error => {
    console.log(error)
  })
}

</script>

<style scoped>
/* 스타일을 추가할 수 있습니다. */
</style>
