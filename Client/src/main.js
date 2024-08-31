import ElementPlus from 'element-plus';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'element-plus/dist/index.css';

const app = createApp(App);
app.use(router);
app.use(ElementPlus);
app.mount('#app');

// Disable scrolling
document.body.style.overflow = 'hidden';
