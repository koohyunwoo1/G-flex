<template>
  <div>
    <h1>마이 페이지</h1>

    <div>
      <h3>좋아요를 누른 영화</h3>
    </div>

    <div>
      <h3>최근 검색한 영화</h3>
      <ul>
        <!-- 검색 결과를 표시 -->
        <li v-for="movie in exactMatches" :key="movie.pk">
          <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
            <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
            <div class="movie-info">
              <h2>{{ movie.title }}</h2>
              <!-- 영화 정보 추가 -->
            </div>
          </RouterLink>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

// exactMatches를 props로 받습니다.
const props = defineProps(['exactMatches']);
</script>

<style scoped>
/* 스타일링 */
</style>