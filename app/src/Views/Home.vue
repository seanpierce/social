<template>
    <div id="home">
        <div v-if="user">
            <h1>Hello, @{{ user.username }}</h1>
        </div>
    </div>
</template>

<script>
export default {
    
    computed: {

        user() {
            return this.$store.state.user
        }
    }
}
</script>