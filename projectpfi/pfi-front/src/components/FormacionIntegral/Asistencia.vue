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
        :headers="headers"
        :items="alumnos"
        :search="search"
        item-key="id"
        class="elevation-1"
        @change="retrieveAlumnos"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Alumnos Registrados al evento</v-toolbar-title>
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
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
import FormacionInDataService from "../../services/FormacionInDataService";
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
          /* { text: 'Asistencia', align: 'center', value: 'asistencia' }, */
          { text: 'Aplicar Asistencia', align: 'center', value: 'apAsistencia'},
          { text: 'Eliminar', align: 'center', value: 'eliminar'}
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
      }
    },
    mounted() {
      
    },
    created (){
      this.retrieveAlumnos(this.$route.params.id);
    },
}
</script>

<style>

</style>