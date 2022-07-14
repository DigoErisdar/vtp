<template>
    <v-row>
        <v-col>
            <v-select
                    :items="listRoles"
                    label="Должность"
                    multiple
                    v-model="form.role"
            ></v-select>
        </v-col>
        <v-col>
            <v-checkbox
                    label="В архиве"
                    v-model="form.isArchive"
            ></v-checkbox>
        </v-col>
        <v-col>
            <v-select :items="sortItemsTitles"
                      label="Сортировать"
                      v-model="form.sort">

            </v-select>
        </v-col>
    </v-row>
</template>

<script>
    export default {
        name: "EmployeFilters",
        props: {
            roles: {
                type: Object,
                default: () => {
                },
            },
        },
        data() {
            return {
                filters: {
                    role: [],
                    isArchive: false,
                },
                form: {
                    role: [],
                    isArchive: false,
                    sort: 'По имени ↑',
                },
                sortItems: {
                    'По имени ↑': (a, b) => {
                        return a.name.localeCompare(b.name)
                    },
                    'По имени ↓': (a, b) => {
                        return b.name.localeCompare(a.name)
                    },
                    'По дате рождения ↑': (a, b) => {
                        return this.parseDate(a.birthday) - this.parseDate(b.birthday)
                    },
                    'По дате рождения ↓': (a, b) => {
                        return this.parseDate(b.birthday) - this.parseDate(a.birthday)
                    },
                },
            }
        },
        methods: {
            parseDate(str) {
                let m = str.match(/^(\d{1,2}).(\d{1,2}).(\d{4})$/);
                return (m) ? new Date(m[3], m[2] - 1, m[1]) : null;
            }
        },
        watch: {
            "form.role": function (roles) {
                this.filters.role = roles.map(role => {
                    return this.keysRoles[role]
                })
                this.$emit("updateFilters", this.filters);
            },
            "form.isArchive": function (isArchive) {
                this.filters.isArchive = isArchive;
                this.$emit("updateFilters", this.filters);
            },
            "form.sort": {
                handler: function (sort) {
                    this.sort = this.sortItems[sort];
                    this.$emit('updateSort', this.sort);
                },
                immediate: true,
            }
        },
        computed: {
            listRoles() {
                return Object.values(this.roles);
            },
            sortItemsTitles() {
                return Object.keys(this.sortItems);
            },
            keysRoles() {
                let temp = {};
                for (let k in this.roles) {
                    temp[this.roles[k]] = k;
                }
                return temp;
            }
        }
    }
</script>

<style scoped>

</style>