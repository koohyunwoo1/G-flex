<template>
  <div class="login-container">
    <h1>로그인 페이지</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="form-group">
        <label for="username">아이디</label>
        <input type="text" v-model.trim="username" id="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="password">비밀번호</label>
        <input type="password" v-model.trim="password" id="password" class="form-control">
      </div>
      <div class="form-group">
        <input type="submit" value="로그인" class="btn btn-primary">
      </div>
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
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 150px;
  border-radius: 8px;
  font-family: Arial, sans-serif;
}

.login-container h1 {
  text-align: center;
  color: white;
}

.login-form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: orange;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  font-size: 16px;
  background-color: #fff;
  color: #495057;
}

.btn {
  display: block;
  margin-top: 30px;
  margin-left: 300px;
  width: 30%;
  padding: 10px;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  text-align: center;
  background-color: orange;
}

.btn:hover {
  background-color: red;
}
</style>
