<template>
    <div id="login">
        <img class="logo" src="/assets/img/sr-logo.png"/>

        <form method="post" @submit.prevent="login()">

            <div class="input-group">
                <input type="text"
                    placeholder="username"
                    v-model="username">
            </div>

            <div class="input-group">
                <input type="password"
                    placeholder="password"
                    v-model="password">
            </div>

            <div class="input-group">
                <button type="submit">Login</button>
            </div>

        </form>

        <div class="input-group">
            <router-link to="/sign-up" tag="button">Sign Up</router-link>
        </div>
    </div>
</template>

<script>
import api from '../api'

export default {
    name: 'Login',

    data() {
        return {
            username: null,
            password: null
        }
    },

    methods: {

        login() {
            api.login(this.username, this.password)
                .then(response => {
                    console.log(response.data)
                    let user = response.data
                    this.$store.dispatch('setUser', user)
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error.response)
                })
        }

    }

}
</script>
