<template>
    <div>
        <Nav />
        <div id="content">
            <routerView />
        </div>
    </div>
</template>

<script>
import Nav from './components/Nav'

export default {
    components: {
        Nav
    }
}
</script>