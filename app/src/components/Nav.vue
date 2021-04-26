<template>
    <div id="nav">
        <routerLink to="/">Plex</routerLink>
        <div class="nav-right" v-if="user">
            <a href='' @click.prevent="logout()">Log out
            </a>
        </div>
    </div>
</template>

<script>
import api from '../api'

export default {
    
    computed: {
        user() {
            return this.$store.state.user
        }
    },

    methods: {

        logout() {
            api.logout()
                .then(response => {
                    console.log('User logged out', response)
                    this.$store.dispatch('setUser', null)
                    this.$router.push('/login/')
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>