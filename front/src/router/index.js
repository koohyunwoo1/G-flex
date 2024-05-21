import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import GenreView from '@/views/GenreView.vue'

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
  ]
})

import { useMovieStore } from '@/stores/movie'

router.beforeEach((to, from, next) => {
  const store = useMovieStore()

  const authRequiredPages = [
    'ProfileView',
    'GenreView',
    'GenreNotFoundView',
    'MovieDetailView',  
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
