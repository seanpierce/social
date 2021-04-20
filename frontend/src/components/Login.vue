<template>
    <div id="login">
        <h2>Login</h2>
        <form @submit.prevent="login()" method="post">
            <div class="input-wrap">
                <input 
                    type="text"
                    v-model="username"
                    placeholder="username">
            </div>

            <div class="input-wrap">
                <input 
                    type="password"
                    v-model="password"
                    placeholder="password">
            </div>

            <div class="input-wrap error" v-if="error">
                Unable to log you in. Please check your credentials and try again.
            </div>

            <div class="input-wrap">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {

    data() {
        return {
            username: null,
            password: null,
            error: false
        }
    },

    methods: {

        login() {
            this.error = false
            let credentials = {
                username: this.username,
                password: this.password
            }
            this.$store.dispatch('login', credentials)
                .then(response => {
                    if (response)
                        this.$router.push('feed')
                    else
                        this.error = true
                })
                .catch(() => {
                    this.error = true
                })
        },
    }
}
</script>