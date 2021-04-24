import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import guard from './guards'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/feed',
    name: 'Feed',
    component: () => import('@/views/Feed.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/views/Profile.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  guard(to, from, next)
})

export default router
