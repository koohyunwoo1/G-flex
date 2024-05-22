<template>
  <div>
    <h1>검색 결과가 없습니다.</h1>
    <p class="p">다른 검색어로 다시 시도해주세요.</p>
    <RouterLink to="/Home">홈으로 돌아가기</RouterLink>
    <div style="text-align: center; margin-top: 50px;">
      <p>인기 있는 검색어를 추천해드릴게요.</p>
      <div v-for="movie in randomMovies" :key="movie.id">
        <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
          <p>{{ movie.title }}</p>
        </RouterLink>
      </div>
      <p></p>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'

const movies = ref([])
const store = useMovieStore()
const router = useRouter()

const homemovies = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/movies/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    movies.value = response.data
  } catch (error) {
    console.error('영화 데이터를 가져오는 도중 오류가 발생했습니다:', error)
  }
};

const getRandomMovies = () => {
  const shuffledMovies = movies.value.sort(() => 0.5 - Math.random())
  return shuffledMovies.slice(0, 4)
}

const randomMovies = computed(() => getRandomMovies())

onMounted(() => {
  homemovies()
});

</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 150px;
}

.p {
  margin-top: 50px;
  text-align: center;
}

a {
  display: block;
  text-align: center;
  margin-top: 30px;
  color: #42b983;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
