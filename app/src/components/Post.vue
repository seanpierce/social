<template>
    <div class="post">
        <div class="post_author linkish"
            @click="goToProfile()">
            @{{ post.author }}
        </div>
        <div class="post_content">
            {{ post.content }}
        </div>
        <div class="post_details">
            {{ formatCreatedAt(post.created_at) }}
        </div>
    </div>
</template>

<script>
import moment from 'moment'

export default {
    
    props: {
        post: Object
    },

    computed: {

        user() {
            return this.$store.state.user
        }
    },

    methods: {
        formatCreatedAt(input) {
            return moment(input).format('MM/DD/YYYY h:mma')
        },

        goToProfile() {
            if (this.post.author === this.user.username)
                return

            this.$router.push(`/profile/${this.post.author}`)
        }
    }
}
</script>