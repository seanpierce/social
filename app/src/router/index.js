import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../Views/Home'
import Profile from '../Views/Profile' 
import Login from '../Views/Login'
import SignUp from '../Views/SignUp'
import { validateSession } from './guards'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        beforeEnter: (to, from, next) => {
            validateSession(to, from, next)
        }
    },
    {
        path: '/profile/:username',
        name: 'Profile',
        component: Profile,
        beforeEnter: (to, from, next) => {
            validateSession(to, from, next)
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/sign-up',
        name: 'Sign Up',
        component: SignUp
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router