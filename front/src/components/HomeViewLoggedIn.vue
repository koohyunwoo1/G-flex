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

    <h1 class="h1">G-Flex가 추천드리는 영화</h1>
    <div class="movie-img">
      <div v-if="movies && movies.length" class="container-img">
        <div v-for="(movie, index) in movies" :key="index" class="movie-item">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
            <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
          </RouterLink>
        </div>
      </div>
      <p v-else>No movies available</p>
    </div>

      <div class="movie-img center" style="margin-top: 250px;">
        <h3 v-if="exactMatches && exactMatches.length">검색 결과</h3>
        <div v-if="exactMatches && exactMatches.length" class="container-img">
          <div>
          </div>
          <div v-for="(movie, index) in exactMatches" :key="index" class="movie-item">
            <div>
              <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
                <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
              </RouterLink>
            </div>
          </div>
        </div>
        <p v-else>No exact matches found</p>
      </div>

      <div class="movie-img center">
        <h3 v-if="recommendedMovies && recommendedMovies.length">비슷한 작품</h3>
        <div v-if="recommendedMovies && recommendedMovies.length" class="container-img">
          <div>
          </div>
          <div v-for="(movie, index) in recommendedMovies" :key="index" class="movie-item">
            <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
              <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
            </RouterLink>
          </div>
        </div>
        <p v-else>No recommendati1ns available</p>
      </div>
      
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'


const movies = ref(null)
const exactMatches = ref([])
const recommendedMovies = ref([])
const store = useMovieStore()
const router = useRouter()
const searchTerm = ref('')


const search = async () => {
  if (searchTerm.value.trim() !== '') {
    try {
      const response = await axios.get(`${store.API_URL}/api/v1/movies/${searchTerm.value}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      });

      const allResults = response.data
      exactMatches.value = allResults.filter(movie => movie.title.includes(searchTerm.value))
      recommendedMovies.value = allResults.filter(movie => !movie.title.includes(searchTerm.value))

      if (exactMatches.value.length === 0) {
        router.push({ name: 'NotFoundView' })
      } else {
        console.log('Exact matches:', exactMatches.value)
        if (recommendedMovies.value.length > 0) {
          console.log('Recommended movies:', recommendedMovies.value)
        } else {
          console.log('No recommendations available.')
        }
      }
    } catch (error) {
      console.error('Error occurred while searching:', error)
    }
  }
}

const homemovies = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/movies/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    movies.value = response.data
  } catch (error) {
    console.error('Error occurred while fetching movies:', error)
  }
};

onMounted(() => {
  homemovies()
});

</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

h1 {
  text-align: center;
}

.h1 {
  margin-top: 200px;
}

.container-img {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
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
  transform: scale(0.9);
  transition: transform 0.3s ease-in-out; 
}


.movie-item:hover {
  transform: scale(1); 
  filter: brightness(1.5); 
}

.movie-image {
  width: 400px;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

h3 {
  background-color: #80CEE1;
  color: white;
  padding: 8px 16px;
  border-radius: 15px;
  border: solid 1px gray;
}
</style>
