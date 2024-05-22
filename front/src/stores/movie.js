import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

export const useMovieStore = defineStore('Movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const logIn_username = ref('')
  // const movies = ref([])

  const movies = ref([])
  const router = useRouter()
  const route = useRoute()
  const isLogin = computed(() => token.value !== null)


  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      router.push({ name: 'LogInView' })
    })
    .catch((error) => {
      console.log('회원가입 실패:', error.response.data)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
    .then((response) => {
      console.log('로그인 성공')
      console.log(response.data)
      token.value = response.data.key
      logIn_username.value = username
      console.log(logIn_username)
      router.push({ name: 'HomeView' })
    })
    .catch((error) => {
      console.log('로그인 실패:', error)
      alert('로그인 실패')
    })
  }

  const logOut = function() {
    token.value = null
    router.push({ name: 'HomeView' })
  }

  // 로그인 후 홈 페이지에 3가지 영화를 띄워주는 역할
  const homemovies = function() {
    axios({
      method:'get',
      url: `${API_URL}/api/v1/movies/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((response)=> {
      movies.value = response.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const movieId = route.params.id
  const movie = ref([])

  const movies_information = function() {

    axios({
      method:'get',
      url: `${store.API_URL}/api/v1/movies/${movieId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      movie.value = response.data
      isLiked.value = response.data.like_users.includes(store.user.pk);
      likeCount.value = response.data.like_users.length;
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { signUp, API_URL, logIn, logOut, token, isLogin, logIn_username, movies, homemovies, movieId, movie, movies_information}
}, { persist: true })
