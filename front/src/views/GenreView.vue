<template>
  <div>
    <h1>장르 or 무드 선택하는 페이지</h1>
    <div>
      <div v-if="genres">
        <div v-for="(genre, index) in genres" :key="index">
          <button>{{ genre.name }}</button>
        </div>
      </div>
      <p v-else>No movies available</p>
    </div>

    <div>
      <div v-if="moods">
        <div v-for="(mood, index) in moods" :key="index">
          <button>{{ mood.name }}</button>
        </div>
      </div>
      <p v-else>No movies available</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/modules/genres_and_moods';

const store = useMovieStore()
const router = useRouter()

const genres = ref(null)

const genreslist = function() {
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/genre/`,
    params: {
      genres: genres.value
    },

    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    genres.value = res.data
  })
  .catch(err => {
    console.log('error 상황 발생')
  })
}

const moods = ref(null)

const moodtags = function() {
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/mood/`,
    params: {
      moods: moods.value
    },

    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    moods.value = res.data
  })
  .catch(err => {
    console.log('error 상황 발생')
  })
}

onMounted(()=> {
  genreslist(),
  moodtags()
})

</script>

<style scoped>

</style>