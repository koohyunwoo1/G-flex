<template>
  <div>
    <HomeViewLoggedIn v-if="isLogin" />
    <HomeViewLoggedOut v-else />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie';
import HomeViewLoggedIn from '@/components/HomeViewLoggedIn.vue';
import HomeViewLoggedOut from '@/components/HomeViewLoggedOut.vue';


const store = useMovieStore();
const isLogin = computed(() => store.isLogin);
</script>

<style scoped>

</style>