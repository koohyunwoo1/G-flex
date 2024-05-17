<template>
  <h1>{{ store.logIn_username }}님 안녕하세요 !</h1>
  <div class="container">
    <div class="search-container">
      <input type="text" v-model="searchTerm" placeholder="영화를 한번 찾아보세요 !" class="search-input">
      <button @click="search" class="search-button">
        <span role="img" aria-label="search" class="search-icon">🔍</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore();
const router = useRouter();
const searchTerm = ref('');

const search = () => {
  if (searchTerm.value.trim() !== '') {
    router.push({ name: 'SearchView', query: { q: searchTerm.value } });
  }
}
</script>

<style scoped>

h1 {
  text-align: center;
}
.container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-container {
  margin-top: 100px;
  background-color: #333;
  width: 350px;
  padding: 10px 20px;
  border-radius: 25px;
}

.search-input {
  background-color: #eee;
  border: none;
  border-radius: 15px;
  padding: 12px 12px;
  margin-right: 10px;
  width: 200px;
}

.search-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.search-icon {
  font-size: 24px;
}

</style>
