import axios from 'axios';

const base = axios.create({
    baseURL: 'http://localhost:8000/api/',
})

export default base