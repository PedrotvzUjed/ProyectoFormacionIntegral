<template>
  <v-container>
    <v-row>
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="alumnos"
        :single-select="singleSelect"
        :single-expand="singleExpand"
        :expanded.sync="expanded"
        :search="search"
        item-key="matricula"
        show-select
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Alumnos</v-toolbar-title>
            <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
          </v-toolbar>
        </template>
        <template v-slot:expanded-item="{ headers, item }">
          <td :colspan="headers.length">
            {{ item.descripcionEvento }}
          </td>
        </template>
      </v-data-table>
    </v-row>
    <v-row>

    </v-row>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";

export default {
    name: "registro",
    data() {
      return {
        alumnos: [],
        singleSelect: true,
        selected: [],
        search: '',
        headers: [
          { text: 'Matricula', align: 'start', sortable: true, value: 'matricula'},
          { text: 'Nombres', value: 'nombres' },
          { text: 'Apellidos', value: 'apellidos' },
          { text: 'Carrera', sortable: true, value: 'carrera' },
          { text: 'semestre', value: 'semestre' }
        ],
      };
    },
    methods: {
      retrieveAlumnos() {
        AlumnosDataService.getAll()
          .then(response => {
            this.alumnos = response.data;
            console.log(this.alumnos);
          })
          .catch(e => {
            console.log(e);
          });
      }
    },
    mounted() {
      this.retrieveAlumnos();
    }
}
</script>

<style>

</style>