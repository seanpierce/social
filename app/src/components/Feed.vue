<template>
    <div id="feed" class="content">
        
        <h1>Feed</h1>

        <div class="posts">

            <div class="post"
                v-for="post in feed" :key="post.id">
                <div class="post_author">
                    @{{ post.author }}
                </div>
                <div class="post_content">
                    {{ post.content }}
                </div>
                <div class="post_details">
                    {{ formatCreatedAt(post.created_at) }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import api from '../api'

export default {

    computed: {

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
        },

        formatCreatedAt(input) {
            return moment(input).format('MM/DD/YYYY h:mm a')
        }
    },

    created() {

        this.getFeed()
    }
    
}
</script>