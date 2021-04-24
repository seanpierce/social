<template>
    <div id="login">
        <h1>Login</h1>

        <form method="post" @submit.prevent="login()">
            <input type="text" placeholder="username" v-model="username">
            <input type="password" placeholder="password" v-model="password">
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
                })
                .catch(error => {
                    console.log(error.response)
                })
        }

    }

}
</script>
