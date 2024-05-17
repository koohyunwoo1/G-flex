<template>
  <div class="container">
      <h1>장르</h1>

    <div>
      <div v-if="genres">
        <span v-for="(genre, index) in genres" :key="index">
          <label :class="{ 'selected': selectedGenres.includes(genre.pk)}" @click="toggleGenre(genre.pk)">
            {{ genre.name }}
          </label>
        </span>
      </div>
      <p v-else>No genres available</p>
    </div>



      <h1 style="margin-top: 80px;">무드</h1>

    <div>
      <div v-if="moods">
        <span v-for="(mood, index) in moods" :key="index">
          <label :class="{ 'selected': selectedMoods.includes(mood.id) }" @click="toggleMood(mood.id)">
            {{ mood.name }}
          </label>
        </span>
      </div>
      <p v-else>No moods available</p>
    </div>
  </div>

  <RouterLink :to=" { name: 'GenreSearchView' }">
    <div class="button-container">
      <button class="button">Go</button>
    </div>
  </RouterLink>

  <RouterView/>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/modules/genres_and_moods'
import { RouterLink, RouterView } from 'vue-router'

const store = useMovieStore()
const genres = ref([])
const selectedGenres = ref([])
const moods = ref([])
const selectedMoods = ref([])

const genreslist = function() {
  axios.get(`${store.API_URL}/api/v1/movies/genre/`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(res => {
    genres.value = res.data;
    console.log(genres)
  })
  .catch(err => {
    console.error(err)
  });
}

const moodtags = function() {
  axios.get(`${store.API_URL}/api/v1/movies/mood/`, {
    headers: { Authorization: `Token ${store.token}` }
  })
  .then(res => {
    moods.value = res.data
    console.log(moods)
  })
  .catch(err => {
    console.error(err)
  });
}

const toggleGenre = (genrePk) => {
  if (selectedGenres.value.includes(genrePk)) {
    selectedGenres.value = selectedGenres.value.filter(pk => pk !== genrePk);
  } else {
    selectedGenres.value.push(genrePk)
  }
}

const toggleMood = (moodId) => {
  if (selectedMoods.value.includes(moodId)) {
    selectedMoods.value = selectedMoods.value.filter(id => id !== moodId);
  } else {
    selectedMoods.value.push(moodId)
  }
}

onMounted(() => {
  genreslist()
  moodtags()
})
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
