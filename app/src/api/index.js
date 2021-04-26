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

export default {
    login,
    checkSession,
    logout
}