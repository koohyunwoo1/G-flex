<template>
  <div>

    <div v-if="movie" >
        <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
        <p>제목 : {{ movie.title }}</p>
        <p v-if="movie.actors.length > 0">배우 : {{ movie.actors.map(actor => actor.name).join(', ') }}</p>
        <p>줄거리 : {{ movie.overview }}</p>
        <p>상영시간 : {{ movie.runtime }}분</p>
        <p v-if="movie.genres.length > 0">장르 : {{ movie.genres.map(genre => genre.name).join(', ') }}</p>

    </div>
    <p v-else>No movies available</p>
    
    <div>
      <textarea v-model="newCommentContent" placeholder="댓글을 입력하세요" @keyup.enter="createCommentOnEnter"></textarea>
      <button @click="createComment">댓글 작성</button>
    </div>

    <div v-if="comments.length > 0">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.user.username }}: {{ comment.content }}</p>
        </li>
      </ul>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = useMovieStore()
const route = useRoute()
const movieId = route.params.id

const movie = ref(null)


const comments = ref([])
const newCommentContent = ref('')

const movies_information = function() {

  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/${movieId}/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    movie.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

const fetchComments = function() {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/${movieId}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    comments.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

const createComment = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${movieId}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: newCommentContent.value
    }
  })
  .then((response) => {
    comments.value = response.data
    newCommentContent.value = ''
  })
  .catch((error) => {
    console.log(error)
  })
}

const createCommentOnEnter = (event) => {
  if (event.key === 'Enter') {
    createComment();
  }
}

onMounted(()=> {
  movies_information()
  fetchComments()

})
  
</script>

<style scoped>

</style>