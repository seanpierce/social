<template>
    <div>
        <div id="container" :class="{ 'showSideNav' : showSideNav }">
            <Nav v-if="user" :showSideNav="showSideNav" :toggleSideNav="toggleSideNav" :class="{ 'showSideNav' : showSideNav }"/>
            <routerView />
        </div>
        <Clubby v-if="user" />
    </div>
</template>

<script>
import Nav from './components/Nav'
import Clubby from './components/clubby'

export default {

    components: {
        Nav,
        Clubby
    },

    data() {
        return {
            showSideNav: false
        }
    },

    computed: {
        user() {
            return this.$store.state.user
        },
    },

    methods: {
        toggleSideNav() {
            this.showSideNav = !this.showSideNav
        }
    }
}
</script>