<template>
    <div id="home">
        <div v-if="user">

            <div class="tabs">
                <div 
                    class="tab" 
                    :class="{ 'selected' : tab == 'club' }"
                    @click="setTab('club')">Club</div>
                <div 
                    class="tab" 
                    :class="{ 'selected' : tab == 'post' }"
                    @click="setTab('post')">Post</div>
            </div>

            <div>

                <div v-show="showFeed">
                    <Club />
                </div>
                <div v-show="showPost">
                    <CreatePost :setTab="setTab" />
                </div>

            </div>
            
        </div>
    </div>
</template>

<script>
import Club from '../components/Club'
import CreatePost from '../components/CreatePost'

export default {

    components: {
        Club,
        CreatePost
    },

    data() {
        return {
            tab: 'club'
        }
    },
    
    computed: {

        user() {
            return this.$store.state.user
        },

        showFeed() {
            return this.tab === 'club'
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