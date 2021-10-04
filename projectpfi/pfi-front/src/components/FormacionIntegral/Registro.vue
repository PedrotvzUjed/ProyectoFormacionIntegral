<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          plain
          block
        >Registro</v-btn>
      </v-col>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Asistencia</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="alumnos"
        :single-select="singleSelect"
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
      </v-data-table>
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
          { text: 'Semestre', value: 'semestre' }
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
      },
      sendEvent() {
        console.log(this.$route.params.id)
        this.$router.push("/fi-asistencia/"+this.$route.params.id);
      }
    },
    mounted() {
      this.retrieveAlumnos();
    }
}
</script>

<style>

</style>