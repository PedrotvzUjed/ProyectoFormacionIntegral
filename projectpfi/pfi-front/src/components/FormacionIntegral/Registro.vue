<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          block
          color = "#a4010b"
          class="white--text"
        >Registro</v-btn>
      </v-col>
      <v-col>
        <v-btn
          v-if="categoria != 'Externos'"
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Asistencia</v-btn>
        <v-btn
          v-else
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Validación de creditos</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="alumnos"
          :single-select="singleSelect"
          :search="search"
          item-key="matricula"
          show-select
          class="elevation-8 overflow-auto"
          height="520px"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Alumnos</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Buscar Alumnos"
                  single-line
                  hide-details
                ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:no-data>
            No se encuentran alumnos registrados actualmente!
          </template>
        </v-data-table>
      </v-col>
      <v-col>
        <v-row>
          <v-col>
            <v-toolbar-title>{{evento.tituloEvento}}</v-toolbar-title>
          </v-col>
          <v-col>
            <v-toolbar-title>Cupo de evento total: {{evento.cupo}}</v-toolbar-title>
            <v-toolbar-title v-if="evento.cupo - alumnosRegistrados - selected.length > 0">Disponible: {{evento.cupo - alumnosRegistrados - selected.length}}</v-toolbar-title>
            <v-toolbar-title v-else>No hay más lugares disponibles</v-toolbar-title>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-data-table
            dense
            :headers="headersRegistrados"
            :items="selected"
            item-key="name"
            class="elevation-8 overflow-auto"
            max-height="520px"
            v-if="selected.length != 0"
          >
            <template v-slot:top>
              <v-toolbar flat>
                <v-btn
                  block
                  depressed
                  color="#a4010b"
                  class="white--text"
                  @click="validarAlumnos()"
                >Registrar Alumnos
              </v-btn>
              </v-toolbar>
            </template>
            <template v-slot:item.nombre="{ item }">
                {{ item.nombres}} {{item.apellidos}}
            </template>
          </v-data-table>
          <v-data-table
            item-key="name"
            class="elevation-8 overflow-auto"
            max-height="480px"
            loading
            loading-text="Seleccionar alumnos para registrar"
            v-else
          >
            <template v-slot:no-data>
              No se encuentran alumnos registrados actualmente!
            </template>
          </v-data-table>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";
import EventosDataService from "../../services/EventosDataService";
import swal from 'sweetalert';

export default {
    name: "registro",
    data() {
      return {
        alumnos: [],
        singleSelect: false,
        selected: [],
        evento: [],
        search: '',
        alumnosRegistrados: 0,
        disponible: 0,
        count: 0,
        categoria: '',
        headers: [
          { text: 'Matricula', align: 'start', sortable: true, value: 'matricula'},
          { text: 'Nombres', value: 'nombres' },
          { text: 'Apellidos', value: 'apellidos' },
          { text: 'Carrera', sortable: true, value: 'carrera' },
          { text: 'Semestre', value: 'semestre' }
        ],
        headersRegistrados: [
          { text: 'Nombre', align: 'start', sortable: false, value: ('nombre')},
          { text: 'Matricula', align: 'start', sortable: false, value: 'matricula'},
        ],
        registro: {
          id: null,
          nombre: "",
          matricula: "",
          asistencia: null,
          evento: null,
          alumno: null,
        },
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
        if(this.categoria != 'Externos') {
          this.$router.push("/fi-asistencia/"+this.$route.params.id);
        }
        else {
          this.$router.push("/fi-validacion/"+this.$route.params.id);
        }
        
      },
      validarAlumnos(){
        this.obtenerDisponible();
        if(this.disponible >= 0){
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
        }else{
          swal("Excedio el limite de lugares disponibles","","warning")
        }     
        setTimeout(this.sendEvent, 1000);   
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
      },
      
      infoEvento(){
        EventosDataService.get(this.$route.params.id)
            .then(response => {
                this.evento = response.data
            })
            .catch(e => {
                console.log(e)
            });
      },
      numAlumnos() {
        FormacionInDataService.getAll(this.$route.params.id)
          .then(response => {
            this.alumnosRegistrados = response.data.length;
            console.log("Alumnos registrados: " + this.alumnosRegistrados);
          })
          .catch(e => {
            console.log(e);
          });
      },
      obtenerDisponible(){
        this.disponible = this.evento.cupo - this.alumnosRegistrados - this.selected.length;
      },
      
      getEvent(){
        EventosDataService.get(this.$route.params.id)
          .then(response => {
            this.categoria = response.data.categorias;
            console.log(response.data.categorias);
          })
          .catch(e => {
            console.log(e);
          });
      },
    },
    mounted() {
    },
    created() {
      this.retrieveAlumnos();
      this.infoEvento();
      this.numAlumnos();
      this.getEvent();
    }
}
</script>

<style>

</style>