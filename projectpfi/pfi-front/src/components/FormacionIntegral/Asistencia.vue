<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Registro</v-btn>
      </v-col>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          plain
          block
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
            <v-toolbar-title>Alumnos Registrados al evento</v-toolbar-title>
          </v-toolbar>
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
import FormacionInDataService from "../../services/FormacionInDataService";

export default {
    name: "asistencia",
    data() {
      return {
        alumnos: [],
        singleSelect: true,
        selected: [],
        search: '',
        headers: [
          { text: 'Nombre', align: 'start', sortable: true, value: 'nombre'},
          { text: 'Natricula', value: 'matricula' },
          { text: 'asistencia', value: 'asistencia' }
        ],
      };
    },
    methods: {
      sendEvent() {
        console.log(this.$route.params.id)
        this.$router.push("/fi-registro/"+this.$route.params.id);
      },
      retrieveAlumnos(evento_id) {
        FormacionInDataService.getAll(evento_id)
          .then(response => {
            this.alumnos = response.data;
            console.log(this.alumnos);
          })
          .catch(e => {
            console.log(e);
          });
      },
    },
    mounted() {
      this.retrieveAlumnos(this.$route.params.id);
    }
}
</script>

<style>

</style>