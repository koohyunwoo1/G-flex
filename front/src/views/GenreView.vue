<template>
  <div class="container">
    <h1>장르</h1>
    <div>
      <div v-if="genres">
        <span v-for="(genre, index) in genres" :key="index">
          <label :class="{ 'selected': selectedGenres.includes(genre.pk)}" @click="selectGenre(genre.pk)">
            {{ genre.name }}
          </label>
        </span>
      </div>
      <p v-else>No genres available</p>
    </div>
  </div>

  <div>
    <div class="button-container">
      <button class="button" @click="fetchMovies" :disabled="selectedGenres.length === 0">Go</button>
    </div>
  </div>

  <div v-if="movies.length">
    <h2>선택된 장르의 영화</h2>
    <div class="movies-container">
      <div v-for="(movie, index) in movies.slice(0, 5)" :key="index" class="movie-item">
        <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-poster" />
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
  <RouterView/>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/modules/genres_and_moods'

const store = useMovieStore()
const genres = ref([])
const selectedGenres = ref([])
const movies = ref([])

const genreslist = () => {
  axios.get(`${store.API_URL}/api/v1/movies/genre/`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(res => {
    genres.value = res.data;
  })
  .catch(err => {
    console.error(err)
  });
}

const selectGenre = (genrePk) => {
  if (selectedGenres.value.includes(genrePk)) {
    selectedGenres.value = selectedGenres.value.filter(pk => pk !== genrePk);
  } else {
    selectedGenres.value.push(genrePk);
  }
}

const fetchMovies = () => {
  if (selectedGenres.value.length === 0) return;

  const promises = selectedGenres.value.map(genrePk => {
    return axios.get(`${store.API_URL}/api/v1/movies/genre/${genrePk}/`, {
      headers: { Authorization: `Token ${store.token}` }
    });
  });

  Promise.all(promises)
    .then(responses => {
      const mergedMovies = responses.flatMap(response => response.data.movies);
      movies.value = mergedMovies;
    })
    .catch(err => {
      console.error(err);
    });
}

genreslist()
</script>

<style scoped>
label {
  padding: 8px 16px;
  margin: 5px;
  border: none;
  background-color: transparent;
  cursor: pointer;
  max-width: fit-content;
  border-radius: 5px;
  border: solid 1px gray;
}

.button {
  margin-top: 50px;
}

.selected {
  background-color: #BBD0E9;
}

.container {
  margin-top: 100px;
}

.button-container {
  text-align: right;
}
</style>
