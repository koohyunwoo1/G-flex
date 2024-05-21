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
          <label :class="{ 'selected': selectedMood === mood.pk}" @click="toggleMood(mood.pk)">
            {{ mood.name }}
          </label>
        </span>
      </div>
      <p v-else>No moods available</p>
    </div>
  </div>

  <div>
    <div class="button-container">
      <button class="button" @click="fetchMovies" :disabled="selectedGenres.length === 0 && !selectedMood">Go</button>
    </div>
  </div>

  <div v-if="movies.length">
    <h2>선택된 장르 또는 무드의 영화</h2>
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
const movies = ref([])

const genres = ref([])
const selectedGenres = ref([])

const moods = ref([])
const selectedMood = ref(null)

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
  if (selectedMood.value === moodPk) {
    selectedMood.value = null; // Deselect if already selected
  } else {
    selectedMood.value = moodPk;
  }
}

const fetchMovies = () => {
  if (selectedGenres.value.length === 0 && !selectedMood.value) return;

  // 선택된 장르와 무드 PK를 query string으로 변환
  const queryString = new URLSearchParams();
  selectedGenres.value.forEach(genrePk => {
    queryString.append('genre_pk', genrePk);
  });
  if (selectedMood.value) {
    queryString.append('mood_pk', selectedMood.value);
  }

  // API 호출 시 query string을 함께 전달
  axios.get(`${store.API_URL}/api/v1/movies/filter/?${queryString.toString()}`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(response => {
    movies.value = response.data;
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
  margin-top: 100px;
}

.button-container {
  text-align: right;
}
</style>
