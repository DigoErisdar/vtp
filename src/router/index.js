import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Index',
        meta: {
            title: "Главная"
        },
        component: () => import(/* webpackChunkName: "about" */ '../views/MainHome.vue')
    },
    {
        path: '/add',
        name: "AddPage",
        meta: {
            title: "Доабвить сотрудника",
        },
        component: () => import('../views/EmployeDetail.vue')
    },
    {
        path: '/:id/edit',
        name: "EditPage",
        meta: {
            title: "Редактировать сотрудника",
        },
        component: () => import('../views/EmployeDetail.vue')
    }
];
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});
export default router