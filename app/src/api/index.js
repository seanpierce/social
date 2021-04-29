import axios from 'axios'

let login = (username, password) => {
    let payload = {
        username: username,
        password: password
    }
    return axios.post('/api/authenticate/login', payload)
}

let checkSession = () => {
    return axios.post('/api/authenticate/checksession')
}

let logout = () => {
    return axios.post('/api/authenticate/logout')
}

let createPost = (content) => {
    let payload = {
        content: content
    }
    return axios.post('/api/posts/create', payload)
}

let getFeed = () => {
    return axios.get('/api/posts')
}

export default {
    login,
    checkSession,
    logout,
    createPost,
    getFeed
}