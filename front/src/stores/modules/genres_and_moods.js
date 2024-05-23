import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('Movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const genres = ref([])
  const moods = ref([])

  const genretags = function() {
    axios({
      method:'get',
      url: `${API_URL}/api/v1/genre/`,
      headers:{
      Authorization: `Token ${token.value}`
      }
    })
    .then((response)=> {
      genres.value=response.data
    })
    .catch(err=> {
      console.log(err);
    })
  }

  const moodtags = function() {
    axios({
      method:'get',
      url: `${API_URL}/api/v1/mood/`,
      headers:{
      Authorization: `Token ${token.value}`
      }
    })
    .then((response)=> {
      moods.value=response.data
    })
    .catch(err=> {
      console.log(err);
    })
  }

  return { API_URL, token, genres, genretags, moods, moodtags }
}, { persist: true })
