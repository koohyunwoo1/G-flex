<template>
  <div>
    <div>
      <div class="profile-container" style="display: flex; justify-content: space-between; align-items: center;">
        <div class="profile-header" style="margin-left: 150px;">
          <div>
            <h2>{{ store.logIn_username }}님의 프로필</h2>
          </div>
        </div>
        
        
        <div class="profile-header" style="margin-right: 150px;">
          <h2>좋아요 한 영화 : {{ likedMovies.length }}개</h2>
          
        </div>
        
      </div>
      
    </div>

    <div style="margin: 100px;">
      <h3 style="margin-left: 50px;">{{ store.logIn_username }}님께서 좋아하는 영화 !</h3>
      <div v-if="likedMovies.length === 0">
        <p style="margin-left: 50px;">좋아하는 영화가 없습니다.</p>
      </div>
      <div v-else>
        <span v-for="movie in likedMovies" :key="movie.id" style="margin-left: 20px;">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
          <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" style="width: 300px;" class="MovieCard">
          </RouterLink>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

const likedMovies = ref([])
const comments = ref([])
console.log(comments)


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
}

.MovieCard:hover {
  transform: scale(1);
  filter: brightness(1.5);
}

.profile-container {
  display: flex;
  justify-content: left;
  align-items: left;
  margin-top: 80px;
}

.profile-header {
  width: auto;
  border: solid 1px gray;
  border-radius: 25px;
  padding: 15px;
  text-align: center;
}

</style>