<template>
  <div>
    <h1>회원가입</h1>
    <h3>회원정보를 입력해주세요.</h3>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">아이디</label>
        <input v-model="username" placeholder="아이디를 입력해주세요." type="text" id="username" name="username">
      </div>
      <div>
        <label for="password1">비밀번호</label>
        <input v-model="password1" placeholder="비밀번호를 입력하세요." type="password" id="password1" name="password1">
      </div>
      <div>
        <label for="password2">비밀번호 확인</label>
        <input v-model="password2" placeholder="비밀번호를 다시 한 번 입력하세요" type="password" id="password2" name="password2">
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

const username = ref('')
const password1 = ref('')
const password2 = ref('')

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
