import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import '@/styles/index.scss'

Vue.config.productionTip = false

window.axios = require('axios')

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
