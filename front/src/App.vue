<template>
  <div>
    <div class="navbar">
      <div>
        <RouterLink :to="{ name: 'HomeView' }" class="logo">
          G-Flex
        </RouterLink> 
      </div>
      <div class="right-links">
        <RouterLink :to="{ name: 'GenreView' }">
          <button v-if="store.isLogin">
            G플리
          </button>
        </RouterLink>
        <template v-if="!store.isLogin">
          <RouterLink :to="{ name: 'LogInView' }">
            <button>
              로그인
            </button>
          </RouterLink> 
          <RouterLink :to="{ name: 'SignUpView' }">
            <button>
              회원가입
            </button>
          </RouterLink>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'HomeView' }">
            <button @click="logOut">
              로그아웃
            </button>
          </RouterLink> 
        </template>
        <RouterLink :to="{ name: 'ProfileView' }">
          <button  v-if="store.isLogin">
            마이페이지
          </button>
        </RouterLink> 
      </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from './stores/movie'

const store = useMovieStore()

const logOut = function() {
  store.logOut()
}
</script>

<style>
.navbar {
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
}

.right-links {
  display: flex;
  gap: 15px;
}

body {
  background-color: #000000;
  color: #ffffff;
  height: 100vh;
}

button {
  background-color: orange;
  color: #ffffff;
  border-radius: 10px;
  border: none;
  width: 80px;
  height: 40px;
  cursor: pointer;
}

button:hover {
  background-color: red;
}

.logo {
  font-size: 36px;
  color: white;
  text-decoration: none;
  font-family: fantasy;
  margin-left: 20px;
}
</style>
