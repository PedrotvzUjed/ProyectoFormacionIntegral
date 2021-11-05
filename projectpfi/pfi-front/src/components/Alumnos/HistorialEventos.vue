<template>
  <v-container>
      <v-row id="datosAlumno">
        <v-card>
            <v-card-title>Datos del Alumno</v-card-title>
            <v-row>
                
                    <v-col>
                        <v-img
                            :lazy-src="dataAlumno.img"
                            max-height="150"
                            max-width="250"
                            :src="dataAlumno.img"
                        ></v-img>
                    </v-col>
                    <v-col>
                        <v-card-text>
                            <label><strong>Alumno: </strong></label>
                            <v-spacer></v-spacer>
                            <label>{{ dataAlumno.nombres }}  {{dataAlumno.apellidos}}</label>
                            <v-spacer></v-spacer>
                            <label><strong>Matricula: </strong></label>
                            <v-spacer></v-spacer>
                            <label>{{ dataAlumno.matricula }} </label>
                        </v-card-text>
                    </v-col>
                    <v-col>
                         <v-card-text>
                            <label><strong>Carrera: </strong></label>
                            <v-spacer></v-spacer>
                            <label>{{ dataAlumno.carrera }}</label>
                            <v-spacer></v-spacer>
                            <label><strong>Semestre: </strong></label>
                            <v-spacer></v-spacer>
                            <label>{{ dataAlumno.semestre }}</label>
                            <v-spacer></v-spacer>
                            <label><strong>Correo electronico: </strong></label>
                            <v-spacer></v-spacer>
                            <label>{{ dataAlumno.correo }}</label>
                        </v-card-text>
                    </v-col>
            </v-row>
        </v-card>
      </v-row>
      <v-row id="" style="margin-top: 20px">
          <v-col>
              <v-card-title>Historial de eventos</v-card-title>
          </v-col>
          <v-col>
              <v-card-title>Total de creditos: {{totalCreditos}}</v-card-title>
          </v-col>
            
        
      </v-row>
      <v-row id="historialEventos" style="margin-top: 20px"
        v-for="(item, index) in eventsAlumno" :key="index">
          <v-card>
            
            <v-row>
                <v-col>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title>{{item.tituloEvento}}</v-list-item-title>
                            <v-list-item-subtitle>
                            {{item.descripcionEvento}}
                            </v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Fecha: {{item.fechaEvento}}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-subtitle>Responsable: {{item.unidadResponsable}}</v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Sede: {{item.sede}}
                            </v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Creditos: {{item.creditos}}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                        <v-list-item-action>
                            <v-list-item-action-text></v-list-item-action-text>

                            <v-icon
                                v-if="eventsFormacion[index].asistencia != 1"
                                color="red"
                                aria-label="No asistio"
                            >
                                mdi-close-circle
                            </v-icon>

                            <v-icon
                                v-else
                                color="teal"
                                aria-label="asistio"
                            >
                                mdi-check-decagram
                            </v-icon>
                            
                        </v-list-item-action>
                    </v-list-item>
                </v-col>
            </v-row>

            
        </v-card>
      </v-row>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";
import EventosDataService from "../../services/EventosDataService";

export default {
  name: "HistorialEventos",
  data() {
    return {
      eventsAlumno: [],
      dataAlumno: [],
      eventsFormacion: [],
      totalCreditos: 0
    };
  },
  created() {
      this.getAlumno();
      this.getEventsAlumno();
      
  },
  mounted() {
      
  },
  methods: {
    getAlumno() {
        AlumnosDataService.get(this.$route.params.id)
            .then(response => {
                this.dataAlumno = response.data;
            })
            .catch(e =>{
                console.log(e);
            })
    },
    getEventsAlumno(){
        FormacionInDataService.getEventsAlumno(this.$route.params.id)
        .then(response => {
            this.eventsFormacion = response.data;
            this.getEventsInfo(response.data);
        })
        .catch(e => {
            console.log(e);
        })
    },
    getEventsInfo(eventsFor){
        for (let evento of eventsFor) {
            EventosDataService.get(evento.evento)
                .then(response => {
                    this.eventsAlumno.push(response.data);
                    console.log(response.data);
                    this.validarCreditos(evento, response.data)
                })
                .catch(e => {
                    console.log(e);
                })   
        }
    },
    validarCreditos(evento, response){
        var creditos = parseFloat(this.totalCreditos);
        var creditos2 = parseFloat(response.creditos);
        if(evento.asistencia == 1){
            var res = creditos + creditos2;
            this.totalCreditos =  res;
        }
    }
  }
}
</script>

<style>

</style>