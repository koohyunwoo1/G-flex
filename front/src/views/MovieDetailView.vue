<template>
  <div>
MovieDetail
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = useMovieStore()
const route = useRoute()
const movieId = route.params.movie.id

const movies_detail = ref(null)

axios({
  method:'get',
  url: `${store.API_URL}/api/v1/movies/${movieId}/`
})
.then((response) => {
  movies_detail.value = response.data
})
.catch((error) => {
  console.log(error)
})

</script>

<style scoped>

</style>