<template>
    <v-app>
        <v-navigation-drawer
                temporary="temporary"
                v-model="drawer"
        >
            <v-list>
                <v-list-item v-for="item in items" :key="item.title" :to="item.href"
                             :title="item.title"></v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar app
        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" variant="text"></v-app-bar-nav-icon>
            <v-app-bar-title>Главная</v-app-bar-title>
        </v-app-bar>

        <v-main>
            <router-view :roles="roles" />
        </v-main>
    </v-app>
</template>

<script>

    export default {
        name: 'App',
        data() {
            return {
                drawer: false,
                group: null,
                roles: {
                    'cook': "Повар",
                    'waiter': "Официант",
                    'driver': "Водитель",
                },
                items: [
                    {
                        title: 'Главная',
                        href: '/',
                    },
                ],
            }
        },

        watch: {
            group() {
                this.drawer = false
            },
        },
    }

</script>