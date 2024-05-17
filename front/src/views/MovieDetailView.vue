<template>
  <div>

    <div v-if="movie" >
        <p>{{ movie.title }}</p>
        <p>{{ movie.overview }}</p>
        <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">

    </div>
    <p v-else>No movies available</p>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = useMovieStore()
const route = useRoute()
const movieId = route.params.id

const movie = ref(null)

const movies_information = function() {

  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/${movieId}/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    movie.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

onMounted(()=> {
  movies_information()
})
  
</script>

<style scoped>

</style>