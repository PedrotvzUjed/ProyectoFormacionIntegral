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
    <v-row>
      <v-btn
          depressed
          elevation="2"
          plain
          block
          @click="validarAlumnos()"
        >Registrar Alumnos</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";

export default {
    name: "registro",
    data() {
      return {
        alumnos: [],
        singleSelect: false,
        selected: [],
        search: '',
        headers: [
          { text: 'Matricula', align: 'start', sortable: true, value: 'matricula'},
          { text: 'Nombres', value: 'nombres' },
          { text: 'Apellidos', value: 'apellidos' },
          { text: 'Carrera', sortable: true, value: 'carrera' },
          { text: 'Semestre', value: 'semestre' }
        ],
        registro: {
          id: null,
          nombre: "",
          matricula: "",
          asistencia: null,
          evento: null,
          alumno: null,
        },
        submitted: false
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
      },
      validarAlumnos(){
        console.log(this.selected)

        for (let alumno of this.selected) {
          FormacionInDataService.getUserExist(this.$route.params.id, alumno.matricula)
            .then(response => {
              if(response.data.length == 1){
                console.log("alumno existente: " + alumno.nombres + ' ' + alumno.apellidos);
              } else {
                console.log("alumno registrado: " + alumno.nombres + ' ' + alumno.apellidos);
                this.registrarAlumnos(alumno);
              }
            })
            .catch(e =>{
              console.log(e)
            });
        }
      },
      registrarAlumnos(alumno){
        var data = {
          nombre: alumno.nombres + ' ' + alumno.apellidos,
          matricula: alumno.matricula,
          asistencia: null,
          evento: this.$route.params.id,
          alumno: alumno.id,
        }
        
        FormacionInDataService.create(data)
          .then(response => {
            this.eventos.id = response.data.id;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      }
    },
    mounted() {
      
    },
    created() {
      this.retrieveAlumnos();
    }
}
</script>

<style>

</style>