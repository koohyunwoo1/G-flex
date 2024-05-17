import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useMovieStore = defineStore('Movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  // const movies = ref([])


  const router = useRouter()
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
      router.push({ name: 'HomeView' })
    })
    .catch((error) => {
      console.log('로그인 실패:', error)
    })
  }

  const logOut = function() {
    token.value = null
    router.push({ name: 'HomeView' })
  }

  return { signUp, API_URL, logIn, logOut, token, isLogin }
}, { persist: true })
