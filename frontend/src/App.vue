<template>
    <div>
        <Nav />
        <RouterView id ="app"/>
    </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {

    components: {
        Nav
    },
}
</script>