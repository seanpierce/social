import Vue from 'vue'
import VueRouter from 'vue-router'
import Test from '../Views/Test'
import Hello from '../Views/Hello' 
import Login from '../Views/Login'
import guards from './guards'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Test',
        component: Test,
        beforeEnter: (to, from, next) => {
            guards.checkSession(to, from, next)
        }
    },
    {
        path: '/hello',
        name: 'Hello',
        component: Hello
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router