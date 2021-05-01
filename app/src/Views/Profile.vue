<template>
    <div id="profile" class="content">
        <div v-if="loading">Fetching profile...</div>

        <div v-if="!loading && profile">
            <h1>{{ profile.username }}</h1>
            <div class="member-details">Member since {{ formatMemberSince(profile.date_joined) }}</div>
        </div>

        <hr class="dark">

        <div v-if="!loading && posts">
            <div v-show="!posts.length">
                <em>This user has no public posts...</em>
            </div>

            <div class="posts">
                <Post v-for="post in posts" 
                    :key="post.id"
                    :post="post" />
            </div>
        </div>
    </div>

</template>

<script>
import moment from 'moment'
import api from '../api'
import Post from '../components/Post'

export default {

    components: {
        Post
    },

    data() {
        return {
            loading: true,
            profile: null,
            posts: null
        }
    },
    
    methods: {
        getData() {
            let username = this.$route.params.username
            api.getProfile(username)
                .then(response => {
                    this.profile = response.data.profile
                    this.posts = response.data.posts
                    this.loading = false
                })
                .catch(error => {
                    console.log(error.response)
                    this.loading = false
                })
        },

        formatMemberSince(input) {
            return moment(input).format('MM/DD/YYYY')
        }
    },

    mounted() {
        
        this.getData()
    },
}
</script>