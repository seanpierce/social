<template>
    <div id="app">
        <Nav />
        <RouterView />
    </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
    components: {
        Nav
    }
}
</script>