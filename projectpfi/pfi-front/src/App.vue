<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      color=""
    >
      <v-list-item class="px-2">
        <v-list-item-content>
            <v-list-item-title>Menu</v-list-item-title>
          </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list v-for="item in items"
          :key="item.title"
          link>
        <v-list-item :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <v-app-bar color="#a4010b" app>
      <v-toolbar-title style="width: 400px" class="ml-0 pl-4">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span class="hidden-sm-and-down" id="pageName">Formación Integral</span>
      </v-toolbar-title>
      <div class="flex-grow-1"></div>

    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'app',

  components: {

  },

  data: () => ({
    drawer: true,
    items: [
      { title: 'Inicio', icon: 'mdi-home', route: '/' },
      { title: 'Eventos', icon: 'mdi-calendar-text', route: '/eventos' },
      { title: 'Capturar Eventos', icon: 'mdi-calendar-plus', route: '/add' },
      { title: 'Formación Integral', icon: 'mdi-home-city', route: '/formacionI' },
      { title: 'Alumnos', icon: 'mdi-account-box-multiple', route: '/fi-alumnos'},
      { title: 'Calendario de Eventos', icon: 'mdi-calendar', route: '/calendario'},
      { title: 'Vista de Alumnos', icon: 'mdi-account-eye', route: '/alumnos-vista-eventos'}
    ],
  }),
};
</script>
