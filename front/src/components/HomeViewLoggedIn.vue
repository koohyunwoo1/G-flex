<template>
  <div class="fade-in">
    <h1 style="text-align: center;">{{ store.logIn_username }}님 안녕하세요 !</h1>

    <div class="container">
      <div class="search-container" style="text-align: center;">
        <input type="text" v-model="searchTerm" placeholder="영화를 찾아보세요!" class="search-input" @keyup.enter="createCommentOnEnter">
        <button @click="search" class="search-button">
          <p aria-label="search" class="search-icon">🔍</p>
          <!-- <span role="img" aria-label="search" class="search-icon">🔍</span> -->
        </button>
      </div>
    </div>
    
    <!-- 이건 검색하면 밑에 검색어 뜨게하는 코드? -->
    <!-- <div v-if="exactMatches && exactMatches.length" class="search-results">
      <div class="search-results-list">
        <p v-for="(movie, index) in exactMatches" :key="index" class="search-result-item">{{ movie.title }}</p>
      </div>
    </div> -->

      <h2 class="h2">G-Flex가 추천드리는 영화</h2>
      <Carousel :itemsToShow="5.3" :wrapAround="true" :autoplay="2500">
        <Slide v-for="movie in movies" :key="movie.id">
          <div class="carousel__slide">
            <div class="movie-img">
              <div class="movie-item">
                <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id }}">
                  <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image">
                </RouterLink>
              </div>
            </div>
          </div>
        </Slide>
        <template #addons>
          <Navigation />
        </template>
      </Carousel>
        
      <div>
        <div class="center" style="margin-top: 250px;">
          <h3 v-if="exactMatches && exactMatches.length">검색 결과</h3>
          <div v-if="exactMatches && exactMatches.length" class="container-img">
            <div v-for="(movie, index) in exactMatches" :key="index" class="movie-item">
              <div>
                <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
                  <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image2">
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
        
        <div class="center">
          <h3 v-if="recommendedMovies && recommendedMovies.length">비슷한 작품</h3>
          <div v-if="recommendedMovies && recommendedMovies.length" class="container-img">
            <div v-for="(movie, index) in recommendedMovies" :key="index" class="movie-item">
              <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.pk }}">
                <img :src="'http://image.tmdb.org/t/p/w500' + movie.poster_path" :alt="movie.title" class="movie-image2">
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
        
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { defineComponent } from 'vue'
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'



defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
})


const movies = ref(null)
const exactMatches = ref([])
const recommendedMovies = ref([])
const store = useMovieStore()
const router = useRouter()
const searchTerm = ref('')


const search = async () => {
  if (searchTerm.value.trim() !== '') {
    try {
      const response = await axios.get(`${store.API_URL}/api/v1/movies/${searchTerm.value}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      });
      
      const allResults = response.data
      exactMatches.value = allResults.filter(movie => movie.title.includes(searchTerm.value))
      recommendedMovies.value = allResults.filter(movie => !movie.title.includes(searchTerm.value))
      
      if (exactMatches.value.length === 0) {
        router.push({ name: 'NotFoundView' })
      } else {
        console.log('Exact matches:', exactMatches.value)
        if (recommendedMovies.value.length > 0) {
          console.log('Recommended movies:', recommendedMovies.value)
        } else {
          console.log('No recommendations available.')
        }
        scrollExactMatchesIntoView()
        
      }
    } catch (error) {
      console.error('Error occurred while searching:', error)
    }
  }
}

const homemovies = async () => {
  try { 
    const response = await axios.get(`${store.API_URL}/api/v1/movies/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    movies.value = response.data
  } catch (error) {
    console.error('Error occurred while fetching movies:', error)
  }
};



const createCommentOnEnter = (event) => {
  if (event.key === 'Enter') {
    search();
  }
}

const scrollExactMatchesIntoView = () => {
  const centerElement = document.querySelector('.container-img');
  if (centerElement) {
    centerElement.scrollIntoView({ behavior: 'smooth'});
  } else {
    setTimeout(scrollExactMatchesIntoView, 10)
  }
}

onMounted(() => {
  homemovies()
});

</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}

h2 {
  text-align: center;
}

.h2 {
  margin-top: 50px;
}

.container-img {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.search-container {
  margin-top: 20px;
  background-color: #333;
  width: 600px;
  padding: 10px 15px;
  border-radius: 25px;
  display: flex;
  align-items: center;
  /* justify-content: center; */
}
.search-input {
  background-color: #eee;
  border: none;
  border-radius: 15px;
  padding: 12px 12px;
  /* margin-right: 10px; */
  width: 600px;
  font-size: 15px;
  /* justify-content: left; */
}

.search-button {
  background-color: transparent;
  border: none;
  width: 60px;
  cursor: pointer;
  display: flex;
  align-items: center; /* Center icon vertically */
  padding: 12px 0px 12px 6px; /* Match the padding of the input */
}

.search-icon {
  font-size: 29px;
  margin-left: 10px;
}



.movie-img {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.movie-item {
  margin: 10px;
  transform: scale(0.9);
  transition: transform 0.3s ease-in-out; 
}


.movie-item:hover {
  transform: scale(1); 
  filter: brightness(1.5); 
}

.movie-image {
  width: 400px;
  border-radius: 15px;
}

.movie-image2 {
  width: 300px;
  border-radius: 15px;
  /* opacity: 0; */
}
.center {
  display: flex; 
  justify-content: center; 
  align-items: center; 
  flex-direction: column;
}



.carousel__slide {
  opacity: 0.9;
  transform: rotateY(-1deg) scale(0.9);
}
.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1.1);
}

.fade-in {
      animation: fadeInAnimation 1s ease-in forwards;
  }
  
  @keyframes fadeInAnimation {
      from {
          opacity: 0;
      }
      to {
          opacity: 1;
      }
  }


</style>
