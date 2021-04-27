<template>
    <div id="nav">
        <a href='' @click.prevent="toggleSideNav()">
            &#9776; Plex
        </a>
        <div class="nav-right" v-if="user">
            <a href='' @click.prevent="logout()">Log out</a>
        </div>

        <div id="sidenav" :class="{ 'open' : showSideNav }">
            <a href='' class="closebtn" @click.prevent="toggleSideNav()">&times;</a>
            <routerLink to="/">Feed</routerLink>
            <routerLink to="/profile/">Profile</routerLink>
            <routerLink to="/friends/">Friends</routerLink>
        </div>
    </div>
</template>

<script>
import api from '../api'

export default {

    props: {
        showSideNav: {
            type: Boolean,
            default: false
        },
        toggleSideNav: {
            type: Function
        }
    },
    
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