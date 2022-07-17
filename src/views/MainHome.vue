<template>
    <v-sheet>
        <v-container fluid>
            <employe-filters :roles="roles"
                             @updateFilters="updateFilters"
                             @updateSort="updateSort"
            ></employe-filters>
            <v-row>
                <v-col cols="12">
                    <v-btn :to="{name:'AddPage'}" color="primary">Добавить сотрудника</v-btn>
                </v-col>
            </v-row>
            <employe-items :items="displayEmployees" :roles="roles"></employe-items>
        </v-container>
    </v-sheet>
</template>

<script>

    import EmployeItems from "@/components/EmployeItems";
    import EmployeFilters from "@/components/EmployeFilters";
    import {mapActions, mapGetters} from "vuex";

    export default {
        name: 'MainHome',
        components: {EmployeFilters, EmployeItems},
        props: {
            roles: {
                type: Object,
                default: () => {},
            },
        },
        data() {
            return {
                filters: {
                    role: [],
                    isArchive: false,
                },
                sort: () => {
                },
                employees: [],
            }
        },
        mounted() {
            this.fetchEmployees();
        },
        methods: {
            ...mapActions('employees', ['fetchEmployees']),
            updateFilters(filters) {
                this.filters = filters;
            },
            updateSort(sort) {
                this.sort = sort;
            },
        },
        computed: {
            ...mapGetters('employees', ['allEmployees']),
            displayEmployees() {
                let response = this.allEmployees;
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
            },
        }
    }
</script>
