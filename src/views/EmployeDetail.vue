<template>
    <v-sheet>
        <v-container>
            <h1>
                {{ $route.meta.title }}
                <!--#TODO: Валидация на только айди-->
            </h1>
            <v-form @submit.prevent="submit" ref="form" v-model="valid" lazy-validation>
                <v-container>
                    <v-row>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field
                                    v-model="form.name"
                                    label="Имя"
                                    :rules="validation.required"
                            />
                        </v-col>
                        <v-col cols="12" xs="12" sm="6">
                            <v-select
                                    :items="rolesValues"
                                    v-model="form.role"
                                    label="Должность"
                                    :rules="validation.required"
                            >

                            </v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field
                                    v-model="form.phone"
                                    label="Номер телефона"
                                    v-maska="'+# (###) ###-####'"
                                    :rules="validation.required"
                            />
                        </v-col>
                        <v-col cols="12" xs="12" sm="6">
                            <v-text-field
                                    v-model="form.birthday"
                                    label="День рождения"
                                    v-maska="dateMask"
                                    :rules="validation.required"
                            />
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col>
                            <v-switch
                                    label="В архиве"
                                    v-model="form.isArchive"
                                    color="primary"
                            />
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="6">
                            <v-btn
                                    :to="{name: 'Employees'}"
                                    class="mx-auto"
                                    width="100%">
                                На главную
                            </v-btn>
                        </v-col>
                        <v-col cols="6">
                            <v-btn
                                    color="primary"
                                    class="mx-auto"
                                    width="100%"
                                    type="submit">
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
    import {mapActions} from "vuex";

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
                valid: true,
                form: {
                    name: "",
                    phone: "",
                    birthday: "",
                    isArchive: false,
                    role: "",
                },
                validation: {
                    required: [
                        v => !!v || "Поле обязательное"
                    ]
                }
            }
        },
        mounted() {
            fetch('/employees.json')
                .then(data => {
                    return data.json()
                })
                .then(items => {
                    if (this.$route.params.id) {
                        this.form = items.filter(item => {
                            return item.id === parseInt(this.$route.params.id);
                        })[0];
                    }
                })
        },
        methods: {
            ...mapActions('employees', ['appendEmploye']),
            submit() {
                this.$refs.form.validate()
                if (this.form.id === undefined) {
                    this.appendEmploye(this.form);
                }
            },
        },
        computed: {
            rolesKeys() {
                return Object.keys(this.roles);
            },
            rolesValues() {
                return Object.values(this.roles);
            }
        },
    }
</script>

<style scoped>

</style>