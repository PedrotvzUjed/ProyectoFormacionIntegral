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
          block
          color = "#a4010b"
          class="white--text"
        >Asistencia</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col>

      </v-col>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          block
          color = "success"
          class="white--text"
          @click="aplicarAsistenciaGrupal()"
        >Aplicar Asistencia a todos</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-data-table
        :headers="headers"
        :items="alumnos"
        :search="search"
        item-key="id"
        class="elevation-8"
        @change="retrieveAlumnos"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Estudiantes Registrados al evento</v-toolbar-title>
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
        <template v-slot:item.eliminar="{ item }">
          <v-btn
            class="ma-2"
            color="red"
            dark
            @click="deleteAlumno(item.id)"
          >
            <v-icon
              dark
            >
              mdi-delete
            </v-icon>
          </v-btn>
        </template>
        <template v-slot:item.evidencia="{ item }">
          <v-btn
            class="ma-2"
            color=""
            @click="retrievEvidencia(item), datosValidacion == item"
            @click.stop="dialog = true"
          >
            <v-icon>
              mdi-account-details
            </v-icon>
          </v-btn> 
        </template>
        <template v-slot:item.apAsistencia="{ item }">
         <v-btn v-if="item.asistencia != 1"
            class="ma-2"
            @click="aplicarAsistencia(item, 1)"
          >
            <v-icon>
              mdi-checkbox-marked-circle
            </v-icon>
          </v-btn>
          <v-btn v-if="item.asistencia == 1"
            class="ma-2"
            color="success"
            dark
            @click="aplicarAsistencia(item, 1)"
          >
            <v-icon>
              mdi-checkbox-marked-circle
            </v-icon>
          </v-btn>
          <v-btn v-if="item.asistencia != 0"
            class="ma-2"
            color=""
            @click="aplicarAsistencia(item, 0)"
          >
            <v-icon
              dark
            >
              mdi-cancel
            </v-icon>
          </v-btn>
          <v-btn v-if="item.asistencia == 0"
            class="ma-2"
            color="red"
            dark
            @click="aplicarAsistencia(item, 0)"
          >
            <v-icon
              dark
            >
              mdi-cancel
            </v-icon>
          </v-btn>
        </template>
        <template v-slot:no-data>
          No se encuentran alumnos registrados actualmente!
        </template>
        
      </v-data-table>
    </v-row>
    <v-dialog
      v-model="dialog"
      transition="dialog-top-transition"
      max-width="600"
    >
      <v-card>
        <v-toolbar
          color="#a4010b"
          dark
        >Evidencia del estudiante: {{datosValidacion.nombre}}</v-toolbar>
        <v-card-text>
          <v-container fluid>
            <v-row justify="space-around" style="padding-top: 10px">
              <v-img
                  v-if="evidencia.length == 0"
                  lazy-src="https://st3.depositphotos.com/2927609/32461/v/600/depositphotos_324611032-stock-illustration-no-image-vector-icon-no.jpg"
                  max-height="300"
                  max-width="300"
                  src="https://st3.depositphotos.com/2927609/32461/v/600/depositphotos_324611032-stock-illustration-no-image-vector-icon-no.jpg"
              ></v-img>
              <v-img
                  v-else
                  :lazy-src="evidencia[0].img"
                  max-height="600"
                  max-width="600"
                  :src="evidencia[0].img"
              ></v-img>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn
            class="ma-2"
            color="red"
            dark
            @click.stop="dialog = false"
          >Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import FormacionInDataService from "../../services/FormacionInDataService";
import EventosDataService from "../../services/EventosDataService";
import swal from 'sweetalert'

export default {
    name: "asistencia",
    data() {
      return {
        alumnos: [],
        search: '',
        headers: [
          { text: 'Nombre', align: 'start', sortable: true, value: 'nombre'},
          { text: 'Matricula', value: 'matricula' },
          { text: 'Verificar Evidencia', align: 'center', value: 'evidencia'},
          { text: 'Aplicar Asistencia', align: 'center', value: 'apAsistencia'},
          { text: 'Eliminar', align: 'center', value: 'eliminar'}
        ],
        evento: [],
        dialog: false,
        evidencia: [],
        datosValidacion: []
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

      aplicarAsistencia(item, asistencia){
        item.asistencia = asistencia;

        FormacionInDataService.update(item.id, item)
        .then(response => {
          console.log(response.data);
            if(asistencia == 1){
              swal("Asistio al evento","","success")
            }else{
              swal("No asistio al evento","","error")
            }
        })
        .catch(e => {
          console.log(e);
           swal("No se pudo actualizar la asistencia","","error")
        });
      },

      aplicarAsistenciaGrupal(){
        for (let alumno of this.alumnos) {
          this.aplicarAsistencia(alumno, 1);
        }
      },

      getEvent(){
        EventosDataService.get(this.$route.params.id)
          .then(response => {
            this.evento = response.data;
          })
          .catch(e => {
            console.log(e);
          });
      },

      deleteAlumno(id){
        FormacionInDataService.delete(id)
        .then(response => {
          console.log(response.data);
          swal("El alumno se elimino correctamente!","","success")
          this.retrieveAlumnos(this.$route.params.id);
        })
        .catch(e => {
          console.log(e);
          swal("Ocurrio un error al eliminar al Alumno","","error")
        });
      },

      retrievEvidencia(data){
            EventosDataService.getEvidencias(this.$route.params.id, data.alumno)
                .then(response => {
                    console.log(response.data);
                    this.evidencia = response.data;
                    this.datosValidacion = data;
                })
                .catch(e => {
                    console.log(e);
                })
        },
    },
    mounted() {
      this.retrieveAlumnos(this.$route.params.id);
    },
    
    created (){
      this.retrieveAlumnos(this.$route.params.id);
      this.getEvent();
    },
}
</script>

<style>

</style>