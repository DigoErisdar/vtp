import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
      path: '/',
      redirect: {
          name: "Employees",
      }
    },
    {
        path: '/employees',
        name: 'Employees',
        meta: {
            title: "Сотрудники"
        },
        component: () => import(/* webpackChunkName: "about" */ '../views/MainHome.vue'),
        children: [

        ],
    },
    {
        path: '/employees/add',
        name: "AddPage",
        meta: {
            title: "Добавить сотрудника",
        },
        component: () => import('../views/EmployeDetail.vue')
    },
    {
        path: '/employees/:id/edit',
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