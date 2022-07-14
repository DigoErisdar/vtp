<template>
    <v-sheet>
        <v-container>
            <v-row>
                <v-col cols="12">
                    <h1 v-if="$route.params.id">
                        Редактирование сотрудника
                    </h1>
                    <h1 v-else>
                        Добавление сотрудника
                    </h1>
                </v-col>
            </v-row>
        </v-container>
    </v-sheet>
</template>

<script>
    export default {
        name: "EmployeDetail",
    }
</script>

<style scoped>

</style>