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
            <v-app-bar-title>{{ $route.meta.title }}</v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-snackbar
                    variant="text"
                    :timeout="alert.timeout"
                    v-model="alert.isOpen">
                <v-alert
                        :type="alert.type"
                >
                    {{ alert.text }}
                </v-alert>
            </v-snackbar>
            <router-view :roles="roles"/>
        </v-main>
    </v-app>
</template>

<script>

    import {mapGetters} from "vuex";

    export default {
        name: 'App',
        data() {
            return {
                drawer: false,
                group: null,
                roles: [
                    {value: 'cook', title: "Повар"},
                    {value: 'waiter', title: "Официант"},
                    {value: 'driver', title: "Водитель"},
                ],
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
        computed: {
            ...mapGetters(['alert']),
        },
    }

</script>