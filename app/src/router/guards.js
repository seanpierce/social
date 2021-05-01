import store from '../store'
import api from '../api'

let validateSession = (to, from , next) => {
    if (!store.state.user) {
        api.checkSession()
            .then(response => {
                let user = response.data
                store.dispatch('setUser', user)
                next()
            })
            .catch(error => {
                // no session or not authenticated
                next('/login/')
            })
    } else {
        next()
    }
}

export {
    validateSession 
}