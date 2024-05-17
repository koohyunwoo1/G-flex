<template>
  <div>
    <h1>{{ store.logIn_username }}님 안녕하세요 !</h1>

    <div class="container">
      <div class="search-container">
        <input type="text" v-model="searchTerm" placeholder="영화를 한번 찾아보세요 !" class="search-input">
        <button @click="search" class="search-button">
          <span role="img" aria-label="search" class="search-icon">🔍</span>
        </button>
      </div>
    </div>

    <h1 class="h1">{{ store.logIn_username }}님 이런 영화는 어떠세요 ?</h1>
    <div class="movie-img">
      <div v-if="movies" class="container-img">
        <div v-for="(movie, index) in movies" :key="index" class="movie-item">
          <RouterLink :to="{name: 'MovieDetailView', params: {id: movie.id}}">
            <!-- {{ movie }} -->
            <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
          </RouterLink>
        </div>
      </div>
      <p v-else>No movies available</p>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const movies = ref(null)
const store = useMovieStore();
const router = useRouter();
const searchTerm = ref('');

const search = () => {
  if (searchTerm.value.trim() !== '') {
    router.push({ name: 'SearchView', query: { q: searchTerm.value } });
  }
}


const homemovies = function() {
  axios({
    method:'get',
    url : `${store.API_URL}/api/v1/movies/`,
    params: {
      movies: movies.value
    },

    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    movies.value = res.data
  })
  .catch(err => {
    console.err('error 발생')
  })
}

onMounted(()=> {
  homemovies()
})


</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

h1 {
  text-align: center;
  font-size: 20px;
}

.h1 {
  margin-top: 200px;
}
.container-img {
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-container {
  margin-top: 20px;
  background-color: #333;
  width: 350px;
  padding: 10px 20px;
  border-radius: 25px;
}

.search-input {
  background-color: #eee;
  border: none;
  border-radius: 15px;
  padding: 12px 12px;
  margin-right: 10px;
  width: 200px;
}

.search-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.search-icon {
  font-size: 24px;
}

.movie-img {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.movie-item {
  margin: 10px;
  transition: transform 0.3s ease; 
}

.movie-item:hover {
  transform: translate(0, -10px); 
}

.movie-image {
  width: 400px;
}
</style>
