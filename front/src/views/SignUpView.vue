<template>
  <div>
    <h1>회원가입</h1>
    <h3>회원정보를 입력해주세요.</h3>
    <form @submit.prevent="signUp">
      <div>
        <label for="username"></label>
        <input placeholder="아이디를 입력해주세요." type="text">
      </div>
      <div>
        <label for="password1"></label>
        <input placeholder="비밀번호를 입력하세요." type="text">
      </div>
      <div>
        <label for="password2"></label>
        <input placeholder="비밀번호를 다시 한 번 입력하세요" type="text">
      </div>
      <br>
      <div>
        <input type="submit" value="SignUp">
      </div>
    </form>

  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const store = useMovieStore()

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}


</script>

<style scoped>

</style>