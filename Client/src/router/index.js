import { createRouter, createWebHistory } from 'vue-router';
import Predict from '../components/predict.vue';
import Train from '../components/train.vue';

const routes = [
  {
    path: '/',
    redirect: '/predict'
  },
  {
    path: '/predict',
    component: Predict
  },
  {
    path: '/train',
    component: Train
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
