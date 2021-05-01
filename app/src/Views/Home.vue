<template>
    <div id="home">
        <div v-if="user">

            <div class="tabs">
                <div 
                    class="tab" 
                    :class="{ 'selected' : tab == 'feed' }"
                    @click="setTab('feed')">Feed</div>
                <div 
                    class="tab" 
                    :class="{ 'selected' : tab == 'post' }"
                    @click="setTab('post')">Post</div>
            </div>

            <div>

                <div v-show="showFeed">
                    <Feed />
                </div>
                <div v-show="showPost">
                    <CreatePost :setTab="setTab" />
                </div>

            </div>
            
        </div>
    </div>
</template>

<script>
import Feed from '../components/Feed'
import CreatePost from '../components/CreatePost'

export default {

    components: {
        Feed,
        CreatePost
    },

    data() {
        return {
            tab: 'feed'
        }
    },
    
    computed: {

        user() {
            return this.$store.state.user
        },

        showFeed() {
            return this.tab === 'feed'
        },

        showPost() {
            return this.tab === 'post'
        },
    },

    methods: {

        setTab(tab) {
            this.tab = tab
        } 
    }
}
</script>