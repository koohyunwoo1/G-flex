import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import GenreView from '@/views/GenreView.vue'
import GenreSearchView from '@/views/GenreSearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/search',
      name: 'SearchView',
      component: SearchView
    },
    {
      path: '/notfound',
      name: 'NotFound',
      component: NotFoundView
    },
    {
      // path:'/:movieId',
      // path: '/articles/:id',
      path: '/moviedetail',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/genre',
      name: 'GenreView',
      component: GenreView
    },
    {
      path: '/genresearch',
      name: 'GenreSearchView',
      component: GenreSearchView
    },

  ]
})

import { useMovieStore } from '@/stores/movie'


router.beforeEach((to, from) => {
  const store = useMovieStore()

  if (to.name === 'ProfileView' && store.isLogin === false) {
    window.alert('로그인 하세요.')
    return { name: 'LogInView'}
  }


  if((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'HomeView' }
  }
})


export default router
