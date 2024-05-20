import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
// import SearchView from '@/views/SearchView.vue'
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
      path: '/notfound',
      name: 'NotFoundView',
      component: NotFoundView
    },
    {
      path: '/movies/:id',
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

router.beforeEach((to, from, next) => {
  const store = useMovieStore()

  const authRequiredPages = [
    'ProfileView',
    'GenreSearchView',
    'GenreView',
    'GenreNotFoundView',
    'MovieDetailView',
    // 'SearchView'
  ]

  if (authRequiredPages.includes(to.name) && !store.isLogin) {
    window.alert('로그인 하세요.')
    return next({ name: 'LogInView' })
  }

  const guestOnlyPages = ['SignUpView', 'LogInView']

  if (guestOnlyPages.includes(to.name) && store.isLogin) {
    window.alert('이미 로그인 했습니다.')
    return next({ name: 'HomeView' })
  }

  next() 
})


export default router
