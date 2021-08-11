<template>
    <div id="feed" class="content">
        <div class="posts">
            <Post v-for="post in feed" 
                :key="post.id"
                :post="post" />
        </div>
    </div>
</template>

<script>
import api from '../api'
import Post from './Post'

export default {

    components: {
        Post
    },

    computed: {

        user() {
            return this.$store.state.user
        },

        feed() {
            return this.$store.state.feed
        }
    },

    methods: {
        
        getFeed() {
            api.getFeed()
                .then(response => {
                    let posts = response.data
                    this.$store.dispatch('setFeed', posts)
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    },

    created() {
        if (!this.feed.length)
            this.getFeed()
    }
    
}
</script>