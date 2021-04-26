<template>
    <div id="login">
        <form method="post" @submit.prevent="login()">

            <div class="input-group">
                <input type="text" placeholder="username" v-model="username">
            </div>

            <div class="input-group">
                <input type="password" placeholder="password" v-model="password">
            </div>

            <div class="input-group">
                <button type="submit">Login</button>
            </div>
        </form>
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
