<template>
  <div>
    <div class="navbar">
      <RouterLink :to="{ name: 'HomeView' }" class="logo">
        G-Flex
      </RouterLink> 
      <div class="right-links">
        <RouterLink :to="{ name: 'GenreView' }">
        <button>
          G플리
        </button>
      </RouterLink>
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
        <RouterLink :to="{ name: 'ProfileView' }">
          <button>
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
</script>

<style>
.navbar {
  /* padding-left: 30%; */
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
  color: #ffffff; /* 글자색을 흰색으로 설정 */
  height: 100vh; /* 화면 전체 높이로 설정 */
}

button {
  background-color: orange;
  color: #ffffff;
  border-radius: 10px;
  border: none;
  width: 80px;
  height: 40px;
}

.logo {
  font-size: 36px; 
  color: white;
  text-decoration: none; 
  font-family: fantasy
}

</style>
