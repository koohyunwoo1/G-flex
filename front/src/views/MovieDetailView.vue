<template>
  <div>

    <div v-if="movie">
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
        <li v-for="comment in comments" :key="comment.pk">
          <p>{{ comment.user.username }}: {{ comment.content }}</p>
          <template v-if="comment.pk !== editedCommentId">
            <button @click="deleteComment(comment.pk)">삭제</button>
            <button @click="toggleEdit(comment)">수정</button>
          </template>
          <div v-if="comment.pk === editedCommentId">
            <textarea v-model="editedCommentContent"></textarea>
            <button @click="updateComment">수정 완료</button>
            <button @click="cancelEdit">취소</button>
          </div>
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
const editedCommentId = ref(null) // 현재 수정 중인 댓글의 ID
const editedCommentContent = ref('') // 수정할 댓글의 내용

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

const deleteComment = function(commentPk) {
  axios({
    method : 'delete',
    url: `${store.API_URL}/api/v1/movies/${movieId}/comments/${commentPk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then(() => {
    // 성공적으로 삭제된 경우, 화면에서 해당 댓글을 제거합니다.
    const index = comments.value.findIndex(comment => comment.pk === commentPk);
    if (index !== -1) {
      comments.value.splice(index, 1);
    }
  })
  .catch((error) => {
    console.log(error)
  })
}

const toggleEdit = function(comment) {
  // 수정할 댓글의 내용을 입력란에 표시하고 수정 입력란을 보여주거나 감춥니다.
  if (editedCommentId.value === comment.pk) {
    cancelEdit();
  } else {
    editedCommentId.value = comment.pk
    editedCommentContent.value = comment.content
  }
}

const cancelEdit = function() {
  // 수정을 취소하면 수정 입력란을 숨깁니다.
  editedCommentId.value = null
  editedCommentContent.value = ''
}

const updateComment = function() {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/movies/${movieId}/comments/${editedCommentId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      content: editedCommentContent.value
    }
  })
  .then(() => {
    // 댓글을 성공적으로 업데이트한 경우, 수정 입력란을 숨기고 댓글 목록을 다시 불러옵니다.
    editedCommentId.value = null
    editedCommentContent.value = ''
    fetchComments()
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

onMounted(() => {
  movies_information()
  fetchComments()
})
</script>

<style scoped>
</style>
