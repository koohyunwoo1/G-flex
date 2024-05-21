<template>
  <div>
    <h1>검색 결과가 없습니다.</h1>
    <p class="p">다른 검색어로 다시 시도해주세요.</p>
    <RouterLink to="/">홈으로 돌아가기</RouterLink>
    <div style="text-align: center; margin-top: 50px;">
      <p>인기 있는 검색어를 추천해드릴게요.</p>
      <p>가디언즈 오브 갤럭시</p>
      <p>어벤져스: 엔드게임</p> 
      <p>어벤져스</p>
      <p>범죄도시</p>
      <p></p>
    </div>
  </div>
</template>

<script setup>  
import { RouterLink } from 'vue-router';
</script>

<style scoped>
h1{
  text-align: center;
  margin-top: 150px;
}

.p {
  margin-top: 50px;
  text-align: center;
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
</style>
