<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <h3>회원정보를 입력해주세요.</h3>
    <form @submit.prevent="signUp">
      <div class="form-group">
        <label for="username">아이디</label>
        <input v-model="username" placeholder="아이디를 입력해주세요." type="text" id="username" name="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="password1">비밀번호</label>
        <input v-model="password1" placeholder="비밀번호를 입력해주세요." type="password" id="password1" name="password1" class="form-control">
      </div>
      <div class="form-group">
        <label for="password2">비밀번호 확인</label>
        <input v-model="password2" placeholder="비밀번호를 다시 한 번 입력해주세요." type="password" id="password2" name="password2" class="form-control">
      </div>
      <br>
      <div class="form-group">
        <input type="submit" value="Sign Up" class="btn btn-primary">
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
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 150px;
  border-radius: 8px;
  font-family: Arial, sans-serif;
}

.signup-container h1 {
  text-align: center;
  color: white;
}

.signup-container h3 {
  text-align: center;
  color: white;
}

.form-group {
  margin-bottom: 15px;
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
