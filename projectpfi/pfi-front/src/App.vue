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

      <v-list>
        <v-list-item to="/eventos">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Inicio</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
  
      <v-list>
        <v-list-item to="/eventos">
          <v-list-item-icon>
            <v-icon>mdi-calendar-text</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Eventos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list>
        <v-list-item to="/add">
          <v-list-item-icon>
            <v-icon>mdi-calendar-plus</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Capturar eventos</v-list-item-title>
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
      <v-btn rounded style="margin-right:20px">Cerrar sesión</v-btn>
      <v-btn rounded style="margin-right:20px">Iniciar sesión</v-btn>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
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
    drawer: true
  }),
};
</script>
