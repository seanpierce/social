<template>
    <div id="home">
        <Login v-if="!user" />

    </div>
</template>

<script>
import Login from '@/components/Login'

export default {

    components: {
        Login
    },

    computed: {
        
        user() {
            return this.$store.state.user
        }
    },

    mounted() {
        if (this.user)
            this.$router.push('feed')
    }
}
</script>