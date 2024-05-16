<template>
  <div>
    <h1>
      로그인페이지
    </h1>
    <form>
      <div>
        <label for="username">username : </label>
        <input type="text">
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password">
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const username = ref(null)
const password = ref(null)
const store = useMovieStore()

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>