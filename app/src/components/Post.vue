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
            <span v-if="showDelete" 
                class="trash" 
                title="Delete this post"
                @click="toggleDeleteModal()">&#x2715;</span>
        </div>
        <div class="delete-post_modal" v-if="showDeleteModal">
            <div class="delete-post_modal_content">
                Delete?
                <span class="_post_content">"{{ post.content }}"</span>
                <div>
                    <button @click="deletePost()">Yep</button>
                    <button @click="toggleDeleteModal()">Nope</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import api from '../api'

export default {
    
    props: {
        post: Object
    },

    data() {
        return {
            showDeleteModal: false
        }
    },

    computed: {

        user() {
            return this.$store.state.user
        },

        showDelete() {
            return this.post.author_id === this.user.id
        }
    },

    methods: {
        formatCreatedAt(input) {
            return moment(input).format('MM/DD/YYYY h:mma')
        },

        goToProfile() {
            this.$router.push(`/profile/${this.post.author}`)
        },

        toggleDeleteModal() {
            this.showDeleteModal = !this.showDeleteModal
        },

        deletePost() {
            if (!this.showDelete) return
            api.deletePost(this.post.id)
                .then(() => {
                    this.$store.dispatch('deletePost', this.post.id)
                    this.toggleDeleteModal()
                }).catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>