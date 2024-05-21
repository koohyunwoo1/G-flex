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

  <div class="container">
    <h1>무드</h1>
    <div>
      <div v-if="moods">
        <span v-for="(mood, index) in moods" :key="index">
          <label :class="{ 'selected': selectedMoods.includes(mood.pk)}" @click="toggleMood(mood.pk)">
            {{ mood.name }}
          </label>
        </span>
      </div>
      <p v-else>No moods available</p>
    </div>
  </div>

  <div style="margin-right: 50px;">
    <div class="button-container">
      <button class="button" @click="fetchMovies" :disabled="selectedGenres.length === 0 && selectedMoods.length === 0">Go</button>
    </div>
  </div>
  

  <div>
    <div v-if="movies.length">
      <h2 style="margin-left: 50px;">선택된 장르 또는 무드의 영화</h2>
      <div class="movie-img">
        <div v-for="(movie, index) in movies.slice(0, 5)" :key="index" class="movie-item">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
            <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image"/>
          </RouterLink>
        </div>
      </div>
    </div>


    <div v-if="showNoMoviesMessage">
      <div style="margin-left: 50px;">
        <h3>선택하신 장르나 무드에 해당하는 영화를 찾지 못하였습니다.</h3>
      </div>
    </div>    
  </div>
  
  <RouterView/> 
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/modules/genres_and_moods'
import { RouterLink, RouterView } from 'vue-router'


const store = useMovieStore()
const movies = ref([])

const genres = ref([])
const selectedGenres = ref([])

const moods = ref([])
const selectedMoods = ref([])

// Go 버튼을 클릭하여 영화를 검색하고 나서 메시지를 표시할지 여부를 나타내는 변수
const showNoMoviesMessage = ref(false)

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

const moodslist = () => {
  axios.get(`${store.API_URL}/api/v1/movies/mood/`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(res => {
    moods.value = res.data;
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

const toggleMood = (moodPk) => {
  if (selectedMoods.value.includes(moodPk)) {
    selectedMoods.value = selectedMoods.value.filter(pk => pk !== moodPk);
  } else if (selectedMoods.value.length < 2) {
    selectedMoods.value.push(moodPk);
  }
}

const fetchMovies = () => {
  if (selectedGenres.value.length === 0 && selectedMoods.value.length === 0) return;

  // 선택된 장르와 무드 PK를 query string으로 변환
  const queryString = new URLSearchParams();
  selectedGenres.value.forEach(genrePk => {
    queryString.append('genre_pk', genrePk);
  });
  selectedMoods.value.forEach(moodPk => {
    queryString.append('mood_pk', moodPk);
  });

  // API 호출 시 query string을 함께 전달
  axios.get(`${store.API_URL}/api/v1/movies/filter/?${queryString.toString()}`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(response => {
    movies.value = response.data;
    // 검색 결과가 없을 경우 메시지 표시
    showNoMoviesMessage.value = movies.value.length === 0;
    // 태그 초기화
    selectedGenres.value = [];
    selectedMoods.value = [];
  })
  .catch(err => {
    console.error(err);
  });
}

genreslist()
moodslist()
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
  margin-left: 50px;
  margin-top: 150px;
}

.button-container {
  text-align: right;
}


.movie-img {
  margin-top: 50px;
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
  width: 300px;
  border-radius: 15px;
}
</style>
