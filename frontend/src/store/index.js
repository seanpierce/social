import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({

  state: {
    user: null,
    isAuthenticated: false,
    jwt: localStorage.getItem('token')
  },

  mutations: {

    SET_USER: (state, user, isAuthenticated) => {
      state.user = user
      state.isAuthenticated = isAuthenticated
    },

    SET_TOKEN: (state, token) => {
      localStorage.setItem('token', token)
      state.jwt = token
    },

    REMOVE_TOKEN: (state) => {
      localStorage.removeItem('token')
      state.jwt = null
    }
  },

  actions: {

    login({ commit }, credentials) {
      let payload = {
        ...credentials
      }
      return new Promise((resolve, reject) => {
        axios.post(process.env.VUE_APP_API_BASE_URL + 'authenticate/login', payload)
          .then(response => {
            commit('SET_USER', response.data)
            resolve(true)
          })
          .catch(error => {
            console.error('Login error: ', error.response)
            commit('SET_USER', null)
            reject(false)
          })
      })
    },

    logout({ commit }) {
      return new Promise((resolve, reject) => {
        axios.post(process.env.VUE_APP_API_BASE_URL + 'authenticate/logout')
          .then(() => {
            commit('SET_USER', null)
            resolve(true)
          })
          .catch(error => {
            console.error('Logout error: ', error.response)
            reject(false)
          })
      })
    },
  },
})
