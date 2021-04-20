import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    user: null
  },

  mutations: {

    SET_USER: (state, user) => {
      state.user = user
    },
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
