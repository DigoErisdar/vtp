<template>
  <v-app>
    <v-layout app>
      <v-navigation-drawer
              bottom
              temporary
              v-model="drawer"
      >
        <v-list
                :items="items"
        ></v-list>
      </v-navigation-drawer>
      <v-app-bar fixed
                 prominent
                 shrink-on-scroll>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" variant="text"></v-app-bar-nav-icon>
        <v-app-bar-title>Главная</v-app-bar-title>
      </v-app-bar>

      <v-main>
        <router-view/>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        drawer: false,
        group: null,
        items: [
          {
            title: 'Главная',
            value: 'main',
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