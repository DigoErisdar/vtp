<template>
    <v-row class="fill-height">
        <v-col :key="item.id" lg="4" sm="6" v-for="item in items" xs="12" >
            <v-card elevation="5" class="fill-height">
                <v-card-title>{{ item.name }}</v-card-title>
                <v-card-subtitle> {{ getRole(item.role) }}</v-card-subtitle>
                <v-card-text>
                    <p>Телефон: {{ item.phone }}</p>
                    <p>День рождение: {{ item.birthday }}</p>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" :to="getLink(item)">
                        Редактировать
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>

</template>

<script>
    export default {
        name: "employe-items",
        props: {
            items: {
                type: Array,
                default: () => [],
            },
            roles: {
                type: Object,
                default: () => {},
            }
        },
        methods: {
            getRole(role) {
                return this.roles[role] || "";
            },
            getLink(item){
                return item.id + "/edit/"
            },
        }
    }
</script>

<style scoped>

</style>