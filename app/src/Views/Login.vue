<template>
    <div id="login">
        <form method="post" @submit.prevent="login()">
            <input type="text" placeholder="username" v-model="username">
            <input type="password" placeholder="password" v-model="password">
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

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
            let payload = {
                username: this.username,
                password: this.password
            }
            axios.post('/api/authenticate/login', payload)
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
