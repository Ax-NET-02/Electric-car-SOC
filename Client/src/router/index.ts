import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Predict from '../components/predict.vue';
import Train from '../components/train.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/predict'
  },
  {
    path: '/predict',
    name: 'Predict',
    component: Predict
  },
  {
    path: '/train',
    name: 'Train',
    component: Train
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
