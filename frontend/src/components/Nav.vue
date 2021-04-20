<template>
    <div id="nav">
      <div id="nav-left" class="nav-section">
        <router-link to="/">SM</router-link>
      </div>
      <div id="nav-right" class="nav-section" v-if="user">
        <a href="" @click.prevent="logout()">LOG OUT</a>
      </div>
    </div>
</template>

<script>
export default {
  
  computed: {

    user() {
      return this.$store.state.user
    }
  },

  methods: {
    logout() {
      this.$store.dispatch('logout')
        .then(response => {
          if (response)
            this.$router.push('/')
        })
    }
  }
}
</script>