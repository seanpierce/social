import store from '@/store'

let guard = (to, from, next) => {
    if (!store.state.user) {
        if (to.name === 'Login')
            next()
        else
            next('/') // login
    }
    else
        next()
}

export default guard