<template>
  <div>
    <div v-if="movie" class="movie-container">
      <img class="movie-poster" :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title">
      <div class="movie-info">
        <hr>
        <div style="display: flex; align-items: center;">
          <p style="font-size: 50px; margin-top:30px; margin-bottom: 30px;">{{ movie.title }}</p>
          <label style="font-size: 20px; margin-left: 30px;" @click="handleLikeClick">
            <span v-if="likeCount > likeCount2" style="color: red;">❤️</span>
            <span v-else>🤍</span> 
            좋아요 : {{ likeCount }}
          </label>
        </div>  
        <p v-if="movie.actors.length > 0">배우 : {{ movie.actors.map(actor => actor.name).join(', ') }}</p>
        <p v-if="movie.genres.length > 0">장르 : {{ movie.genres.map(genre => genre.name).join(', ') }}</p>
        <p>상영시간 : {{ movie.runtime }}분</p>
        <p style="font-size: 15px;">줄거리 : {{ movie.overview }}</p>
        <hr>  
        
        <div>
          <div class="like-comments-section">
            <div class="comment-input">
              <textarea v-model="newCommentContent" placeholder="감상평을 작성해 주세요." @keyup.enter="createCommentOnEnter" style="font-size: 15px; padding-left: 15px; line-height: 35px;height: 35px;"></textarea>
              <button @click="createComment" style="width: 60px; height: 50px;">작성</button>
              <div style="text-align: right; margin-left: 10px; margin-top: 10px;">{{ getCurrentCharacterCount() }}/{{ commentMaxLength }}</div>
            </div>
          </div>
          
          <div v-if="comments.length > 0">
            <div v-for="comment in comments" :key="comment.pk">
              <div v-if="comment.pk !== editedCommentId">
                <p style="font-size: 15px; font-weight: bolder;">{{ comment.user.username }}</p>
                <div style="display: flex; align-items: center; justify-content: space-between;">
                  <p style="font-size: 15px;">{{ comment.content }}</p>
                  <hr>
                  
                  <div v-if="comment.user.username === store.logIn_username">
                    <template v-if="comment.pk !== editedCommentId">
                      <button style="width: 50px; margin-right: 10px;" @click="toggleEdit(comment)">수정</button>
                      <button style="width: 50px;" @click="deleteComment(comment.pk)">삭제</button>
                    </template>
                    
                    <div v-if="comment.pk === editedCommentId">
                      <textarea v-model="editedCommentContent"></textarea>
                      <button @click="updateComment">수정 완료</button>
                      <button @click="cancelEdit">취소</button> 
                    </div>
                  </div>
                </div>
              </div>            
              <div v-else>
                <p style="font-size: 15px; font-weight: bolder;">{{ comment.user.username }}</p>
                <div style="display: flex; align-items: center; justify-content: space-between;">
                  <textarea v-model="editedCommentContent" style="flex: 1; padding: 10px; font-size: 15px;"></textarea>
                  <div style="display: flex; gap: 10px; align-items: center;">
                    <div style="text-align: right; margin-left: 10px; margin-top: 10px;">{{ getCurrentCharacterCount2() }}/{{ commentMaxLength }}</div>
                    <button style="width: 80px;" @click="updateComment">수정 완료</button>
                    <button style="width: 50px;" @click="cancelEdit">취소</button>
                  </div>
                </div>
              </div>
              <hr>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-else>No movies available</p>
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

const isLiked = ref(false) // 좋아요 상태
const likeCount = ref(0) // 좋아요 수
const likeCount2 = ref(0)
const commentMaxLength = 100; 


const handleLikeClick = function() {
  if (!isLiked.value) { // 이미 좋아요를 눌렀으면 무시
    toggleLike();
  } 
}

const toggleLike = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/movies/${movieId}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(response)
    likeCount.value = response.data.like_users.length;
    likeCount2.value = response.data.liee_users.length;
    likeCount += 1
  })
  .catch((error) => {
    console.log(error)
  })
}


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
    // isLiked.value = response.data.like_users.includes(store.user.pk);
    likeCount.value = response.data.like_users.length;
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
    console.log(response)
    comments.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

const createComment = function() {
  if (newCommentContent.value.length > commentMaxLength) {
    alert('설정하신 제한 글자수 100글자를 초과하였습니다.') 
    return; 
  }
  
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
    console.log(comments)
  })
  .catch((error) => {
    console.log(error)
  })
}

// 현재 입력된 글자 수를 반환하는 함수
const getCurrentCharacterCount = () => {
  return newCommentContent.value.length;
}
const getCurrentCharacterCount2 = () => {
  return editedCommentContent.value.length;
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
    // 성공적으로 삭제된 경우, 화면에서 해당 댓글을 제거
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
  if (editedCommentContent.value.length > commentMaxLength) {
    alert('설정하신 제한 글자수 100글자를 초과하였습니다.') 
    return;
  }

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
    editedCommentId.value = null
    editedCommentContent.value = ''
    fetchComments()
  })
  .catch((error) => {
    console.log(error)
  })

  getCurrentCharacterCount2();
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
.movie-container {
  margin-left: 250px;
  margin-right: 250px;
  margin-top: 100px;
  display: flex;
  align-items: flex-start; 
}

.movie-poster {
  transform: scale(1);
  transition: transform 0.3s ease-in-out;
  border-radius: 30px;
  width: 400px; 
  margin-right: 20px; 
  margin-left: 20px;
}

.movie-poster:hover {
  transform: scale(1.1);
  filter: brightness(1.5);
}

.movie-info {
  margin-left: 50px;
  flex: 1; 
  font-size: 20px;
}


.like-comments-section {
  /* margin-left: 30px; */
  margin-top: 20px;
}


.comment-input {
  display: flex;
  align-items: center;
}

.comment-input button {
  margin-top: 30px;
  display: flex;
  align-items: center;
}

.comment-input textarea {
  padding-top: 8px;
  width: 800px;
  height: 40px;
  font-size: 15px;
  border-radius: 10px;
  resize: none;
  color: black;
  border: none;
  border-bottom: 2px solid #0000007e;
  outline: none;
  margin-right: 10px;
  display: inline-block;

}

.comment-input button {
  margin-top: 0;
  display: inline-block;

}

label {
  padding: 8px 16px;
  background-color: transparent;
  cursor: pointer;
  border-radius: 15px;
  border: solid 1px gray;
}


textarea {
  padding-top: 8px;
  width: 300px;
  height: 20px;
  font-size: 15px;
  border-radius: 10px;
  resize: none;
  color: black;
  border: none;
  border-bottom: 2px solid #0000007e;
  outline: none;
  /* margin-left: 250px; */
}

</style>