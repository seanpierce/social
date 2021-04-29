<template>
    <div>
        <div id="container" :class="{ 'showSideNav' : showSideNav }">
            <Nav v-if="user" :showSideNav="showSideNav" :toggleSideNav="toggleSideNav" :class="{ 'showSideNav' : showSideNav }"/>
            <routerView />
        </div>
    </div>
</template>

<script>
import Nav from './components/Nav'

export default {

    components: {
        Nav
    },

    data() {
        return {
            showSideNav: false
        }
    },

    computed: {
        user() {
            return this.$store.state.user
        }
    },

    methods: {
        toggleSideNav() {
            this.showSideNav = !this.showSideNav
        }
    }
}
</script>