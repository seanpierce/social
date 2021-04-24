import Vue from 'vue'
import VueRouter from 'vue-router'
import Test from '../Views/Test'
import Hello from '../Views/Hello' 

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Test',
        component: Test
    },
    {
        path: '/hello',
        name: 'Hello',
        component: Hello
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router