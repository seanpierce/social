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
import api from '../api'

export default {
    
    data() {
        return {
            content: null
        }
    },

    methods: {

        createPost() {
            api.createPost(this.content)
                .then(response => {
                    console.log(response)
                    // if success
                    // add post to store
                    // show success message
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    }
}
</script>