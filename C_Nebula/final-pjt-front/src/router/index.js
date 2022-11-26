import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SearchView from '../views/SearchView.vue'
import RecommendationView from '../views/RecommendationView.vue'
import MovieDetailView from '../views/MovieDetailView'
import ProfileView from '../views/ProfileView.vue'
import JournalView from '../views/JournalView.vue'
import JournalCreateView from '../views/JournalCreateView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import JournalDetailView from '@/views/JournalDetailView'
import UpdateJournalView from '@/views/UpdateJournalView'
import ChangePasswordForm from '@/views/ChangePasswordForm'
import ProfileUpdateView from '@/views/ProfileUpdateView'
import store from '../store'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/recommendation',
    name: 'recommendation',
    component: RecommendationView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '/movies/:movie_id',
    name: 'movieDetail',
    component: MovieDetailView
  },
  
  {
    path: '/profile/:user_id',
    name: 'profile',
    component: ProfileView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '/journal/',
    name: 'journalView',
    component: JournalView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
        to
      } else {
        next()
      }
  }
},
  {
    path: '/journal/create',
    name: 'journalCreateView',
    component: JournalCreateView
  },
  {
    path: '/accounts/signup',
    name: 'signUp',
    component: SignUpView
  },
  {
    path: '/accounts/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/journal/:journal_id/detail',
    name: 'journalDetail',
    component: JournalDetailView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '/journal/:journal_id/update',
    name: 'updateJournalView',
    component: UpdateJournalView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '/accounts/changepassword',
    name: 'ChangePassword',
    component: ChangePasswordForm,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/accounts/updateprofile',
    name: 'profileUpdateView',
    component: ProfileUpdateView,
    beforeEnter: function(to, from, next) {
      if (!store.state.token) {
        alert('로그인이 필요합니다!')
      } else {
        next()
      }
    }
  },
  {
    path: '*',
    redirect: '/404'
  }


]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
