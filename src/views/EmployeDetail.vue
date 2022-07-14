<template>
    <v-sheet>
        <v-container>
            <h1>
                {{ $route.meta.title }}
            </h1>
            <v-form>
                <v-container>
                    <v-row>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field v-model="form.name" label="Имя" />
                        </v-col>
                        <v-col cols="12" xs="12" sm="6">
                            <v-select :items="rolesValues" v-model="form.role" label="Должность"></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field v-model="form.phone" label="Номер телефона"/>
                        </v-col>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field v-model="form.birthday" label="День рождения"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col>
                            <v-switch label="В архиве" v-model="form.isArchive" color="primary"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="6">
                            <v-btn :to="{name: 'Index'}" class="mx-auto" width="100%">На главную</v-btn>
                        </v-col>
                        <v-col cols="6">
                            <v-btn color="primary" class="mx-auto" width="100%">
                                <template v-if="$route.params.id">Сохранить</template>
                                <template v-else>Добавить</template>
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-container>
            </v-form>
        </v-container>
    </v-sheet>
</template>

<script>
    export default {
        name: "EmployeDetail",
        props: {
            roles: {
                type: Object,
                default: () => {
                },
            },
        },
        data() {
            return {
                form: {
                    name: "",
                    phone: "",
                    birthday: new Date(),
                    isArchive: false,
                    role: "",
                },
            }
        },
        mounted() {
            fetch('/employees.json')
                .then(data => {
                    return data.json()
                })
                .then(items => {
                    this.form = items.filter(item => {
                        return item.id === parseInt(this.$route.params.id);
                    })[0];
                })
        },
        computed: {
            rolesKeys() {
                return Object.keys(this.roles);
            }
            ,
            rolesValues() {
                return Object.values(this.roles);
            }
        }
    }
</script>

<style scoped>

</style>