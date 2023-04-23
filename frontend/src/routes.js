import {createWebHistory, createRouter } from 'vue-router';
import HomeApp from './components/HomeApp.vue'


const routes=[
    {
        name:'HomeApp',
        path:'/',
        component:HomeApp
    }
];

const router=createRouter({
    history:createWebHistory(),
    routes
});

export default router;