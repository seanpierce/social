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
    },

    DELETE_POST: (state, post_id) => {
      let index = state.feed.findIndex(post => post.id === post_id)
      state.feed.splice(index, 1)
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
    },

    deletePost({ commit }, post_id) {
      commit('DELETE_POST', post_id)
    }
  },

  modules: {
  }

})
