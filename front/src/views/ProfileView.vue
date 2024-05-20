<template>
  <div>
    <div style="margin: 100px;">
      <h3>{{ store.logIn_username }}님께서 좋아하시는 영화 !</h3>
      <div v-if="likedMovies.length === 0">
        <p>좋아하는 영화가 없습니다.</p>
      </div>
      <div v-else>
        <span v-for="movie in likedMovies" :key="movie.id" style="margin-left: 20px;">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
          <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" style="width: 400px;" class="MovieCard">
          </RouterLink>
        </span>
      </div>
    </div>

    <div style="margin: 100px;">
      <h3>{{ store.logIn_username }}님께서 최근 검색하신 영화 !</h3>
      <ul>
        <!-- 검색 결과를 표시
        <li v-for="movie in exactMatches" :key="movie.pk">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
            <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
            <div class="movie-info">
              <h2>{{ movie.title }}</h2>
              영화 정보 추가
            </div>
          </RouterLink>
        </li> -->
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

const likedMovies = ref([])

onMounted(() => {
  getProfile()
})

const getProfile = function() {
  axios({
    method :'get',
    url: `${store.API_URL}/api/v1/profile/${store.logIn_username}`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then((response) => {
    likedMovies.value = response.data.like_movies;
  })
  .catch((error) => {
    console.log(error)
  })
}
</script>

<style scoped>
.MovieCard {
  transform: scale(0.9);
  transition: transform 0.3s ease-in-out;
  /* filter: brightness(0.5); */
}

.MovieCard:hover {
  transform: scale(1);
  filter: brightness(1.5);
}
</style>