<template>
  <v-container>
    <v-row>
      <v-data-table
        :headers="headers"
        :items="alumnos"
        :search="search"
        item-key="id"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Estudiantes</v-toolbar-title>
            <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Buscar alumnos"
                single-line
                hide-details
              ></v-text-field>
          </v-toolbar>
        </template>
        <template v-slot:item.detalles="{ item }">
         <v-btn
            class="ma-2"
            @click="sendStudent(item.id)"
          >
            <v-icon>
              mdi-account-details
            </v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";

export default {
    name: "alumnos",
    data() {
      return {
        alumnos: [],
        search: '',
        headers: [
          { text: 'Matricula', align: 'center', sortable: true, value: 'matricula'},
          { text: 'Nombres', value: 'nombres' },
          { text: 'Apellidos', value: 'apellidos' },
          { text: 'Carrera', sortable: true, value: 'carrera' },
          { text: 'Semestre', align: 'center', value: 'semestre' },
          { text: 'Ver detalles', align: 'center', value: 'detalles'}
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
      
      sendStudent(id) {
        console.log(id)
        this.$router.push("/fi-alumnos/"+id);
      },
      
    },
    mounted() {
      this.retrieveAlumnos();
    }
}
</script>

<style>

</style>