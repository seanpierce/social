import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    user: null,
    feed: []
  },

  mutations: {

    SET_USER: (state, user) => {
      state.user = user
      state.feed = []
    },

    SET_FEED: (state, posts) => {
      state.feed.push(...posts)
    },

    INSERT_POST: (state, post) => {
      state.feed.unshift(post)
    }
  },

  actions: {

    setUser({ commit }, user) {
      commit('SET_USER', user)
    },

    setFeed({ commit }, posts) {
      commit('SET_FEED', posts)
    },

    insertPost({ commit }, post) {
      commit('INSERT_POST', post)
    }
  },

  modules: {
  }

})
