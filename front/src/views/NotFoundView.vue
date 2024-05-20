<template>
  <div>
    <div class="image-container">
      <img src="/assets/404_2.png" alt="img">
    </div>
    <h1>검색 결과가 없습니다.</h1>
    <p>다른 검색어로 다시 시도해주세요.</p>
    <RouterLink to="/">홈으로 돌아가기</RouterLink>
  </div>
</template>

<script setup>  
import { RouterLink } from 'vue-router';
</script>

<style scoped>
h1, p {
  text-align: center;
  margin-top: 20px;
}

a {
  display: block;
  text-align: center;
  margin-top: 30px;
  color: #42b983;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.image-container {
  display: flex;
  justify-content: center;
}

img {
  width: 600px;
}
</style>
