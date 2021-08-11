<template>
    <div id="post" class="content">

        <h1>Create Post</h1>

        <div class="input-group">
            <textarea v-model="content"></textarea>
        </div>
        <div class="input-group">
            <button type="submit" @click="createPost()">Submit</button>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import api from '../api'

export default {

    props: {
        setTab: Function
    },
    
    data() {
        return {
            content: null
        }
    },

    computed: {
        user() {
            return this.$store.state.user
        }
    },

    methods: {

        createPost() {
            api.createPost(this.content)
                .then(response => {
                    let post = {
                        id: response.data,
                        content: this.content,
                        author: this.user.username,
                        author_id: this.user.id,
                        created_at: moment()
                    }

                    this.$store.dispatch('insertPost', post)
                    this.setTab('club')
                    this.content = null
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    }
}
</script>