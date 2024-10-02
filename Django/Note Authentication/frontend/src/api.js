import axios from 'axios'
import { ACCESS_TOKEN } from './constants'


const urls = import.meta.env.VITE_API_URL
const api = axios.create({
    baseURL : urls
})


api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (token) {
            config.headers.Authorization = `Bearer ${token}`

        }
        return (config)
    },
    (err) => {
        return Promise.reject(err)
    }
)
export default api
