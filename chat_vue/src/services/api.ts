import axios, { type AxiosInstance } from 'axios';

const API: AxiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/', // Django backend URL
});

export default API;