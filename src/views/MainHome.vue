<template>
    <v-sheet>
        <v-container fluid>
            <employe-filters :roles="roles"
                             @updateFilters="updateFilters"
                             @updateSort="updateSort"
            ></employe-filters>
            <v-row>
                <v-col cols="12">
                    <v-btn color="primary" to="/add">Добавить пользователя</v-btn>
                </v-col>
            </v-row>
            <employe-items :items="displayEmployees" :roles="roles"></employe-items>
        </v-container>
    </v-sheet>
</template>

<script>

    import EmployeItems from "@/components/EmployeItems";
    import EmployeFilters from "@/components/EmployeFilters";

    export default {
        name: 'MainHome',

        components: {EmployeFilters, EmployeItems},

        data() {
            return {
                filters: {
                    role: [],
                    isArchive: false,
                },
                sort: () => {
                },
                employees: [],
                roles: {
                    'cook': "Повар",
                    'waiter': "Официант",
                    'driver': "Водитель",
                },
            }
        },
        mounted() {
            fetch("employees.json")
                .then(data => {
                    return data.json()
                })
                .then(items => {
                    this.employees = items;
                });
        },
        methods: {
            updateFilters(filters) {
                this.filters = filters;
            },
            updateSort(sort) {
                this.sort = sort;
            },
        },
        computed: {
            displayEmployees() {
                let response = this.employees;
                if (this.filters.role.length > 0) {
                    response = response.filter(item => {
                        return this.filters.role.includes(item.role);
                    })
                }
                if (this.filters.isArchive) {
                    response = response.filter(item => {
                        return item.isArchive
                    })
                }
                return response.sort(this.sort);
            }
        }
    }
</script>
