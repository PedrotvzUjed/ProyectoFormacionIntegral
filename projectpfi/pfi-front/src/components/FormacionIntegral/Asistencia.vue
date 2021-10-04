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
      
    </v-row>
  </v-container>
</template>

<script>

export default {
    name: "asistencia",
    data() {
      return {
        alumnos: [],
        singleSelect: true,
        selected: [],
        search: '',
        headers: [
          /* { text: 'Matricula', align: 'start', sortable: true, value: 'matricula'},
          { text: 'Nombres', value: 'nombres' },
          { text: 'Apellidos', value: 'apellidos' },
          { text: 'Carrera', sortable: true, value: 'carrera' },
          { text: 'semestre', value: 'semestre' } */
        ],
      };
    },
    methods: {
      sendEvent() {
        console.log(this.$route.params.id)
        this.$router.push("/fi-registro/"+this.$route.params.id);
      }
    },
    mounted() {
      
    }
}
</script>

<style>

</style>