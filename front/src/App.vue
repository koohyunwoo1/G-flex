<template>
  <div>
    <div class="navbar">
      <div>
        <RouterLink :to="{ name: 'Gflex' }" class="logo">
          G-Flex
        </RouterLink> 
      </div>
      <div class="right-links">
        <RouterLink :to="{ name: 'GenreView' }">
          <button v-if="store.isLogin">
            <b>
            G 플리
            </b>
          </button>
        </RouterLink>
        <template v-if="!store.isLogin">
          <RouterLink :to="{ name: 'LogInView' }">
            <button>
              <b>
                로그인
              </b>
            </button>
          </RouterLink> 
          <RouterLink :to="{ name: 'SignUpView' }">
            <button>
              <b>
                회원가입
              </b>
            </button>
          </RouterLink>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'HomeView' }">
            <button>
              <b>
                Search
              </b>
            </button>
          </RouterLink> 
          <RouterLink :to="{ name: 'ProfileView' }">
          <button>
            <b>
              마이페이지
            </b>
          </button>
        </RouterLink> 
          <RouterLink :to="{ name: 'HomeView' }">
            <button @click="logOut" style="margin-right: 30px;">
              <b>
                로그아웃
              </b>
            </button>
          </RouterLink> 
        </template>
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
  background-image: url('assets/back_img10.jpg');
  background-size: cover;
  background-attachment: fixed;
  color: #ffffff;
  height: 100vh;
}

button {
  background-color: transparent;
  color: white;
  border-radius: 10px;
  border: 0.5px solid #87CEEB;
  width: 90px;
  height: 40px;
  cursor: pointer;
}

button:hover {
  background-color: #80d6ff;
}

.logo {
  font-size: 40px;
  color: white;
  text-decoration: none;
  font-family: fantasy;
  margin-left: 20px;
  color: skyblue;
}
</style>
