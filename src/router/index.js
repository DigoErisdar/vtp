import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Index',
        component: () => import(/* webpackChunkName: "about" */ '../views/MainHome.vue')
    },
    {
        path: '/add',
        name: "AddPage",
        component: () => import('../views/EmployeDetail.vue')
    },
    {
        path: '/:id/edit',
        name: "EditPage",
        component: () => import('../views/EmployeDetail.vue')
    }
];
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});
export default router