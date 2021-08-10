<template>
    <div id="nav">
        <a href='' @click.prevent="toggleSideNav()" class="nav-toggle">
            &equiv; &#10550; <span class="username">My Spoil Club</span>
        </a>

        <div id="sidenav" :class="{ 'open' : showSideNav }">
            <a href='' class="closebtn" @click.prevent="toggleSideNav()">&times;</a>
            <routerLink to="/">Club</routerLink>
            <routerLink to="/profile">Profile</routerLink>
            <routerLink to="/friends">Friends</routerLink>
            <hr>
            <a href='' @click.prevent="logout()">Log out :(</a>            
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
                    this.toggleSideNav()
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>