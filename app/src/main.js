import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import './styles/index.scss'

new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')