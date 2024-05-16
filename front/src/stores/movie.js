import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useMovieStore = defineStore('Movie', () => {
  const API_URL = 'http://127.0.0.1:8000'

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: {
        username: username,
        password1: password1,
        password2: password2,
      }
    })
    .then((response) => {
      console.log('회원가입 성공 !')
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        console.log('로그인 성공')
        token.value = response.data.key
        router.push({ name : 'HomeView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }


  return {signUp, logIn, API_URL}
},
{ persist: true }
)
