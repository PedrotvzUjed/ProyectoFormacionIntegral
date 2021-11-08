<template>
  <v-container id="createDoc">
      <v-row id="datosAlumno">
        <v-card >
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
      <v-row style="margin-top: 20px">
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
      <v-speed-dial
        v-model="fab"
        top
        right
        :direction="direction"
        :open-on-hover="hover"
        :transition="transition"
        >
        <template v-slot:activator>
            <v-btn
            v-model="fab"
            color="#a4010b"
            dark
            fab
            >
            <v-icon v-if="fab">
                mdi-close
            </v-icon>
            <v-icon v-else>
                mdi-file-export
            </v-icon>
            </v-btn>
        </template>
        <v-btn
            fab
            dark
            color="green"
        >
            <v-icon>mdi-file-excel</v-icon>
        </v-btn>
        <v-btn
            fab
            dark
            color="indigo"
        >
            <v-icon>mdi-file-word</v-icon>
        </v-btn>
        <v-btn
            fab
            dark
            color="red"
            @click="createPDF()"
        >
            <v-icon>mdi-file-pdf-box</v-icon>
        </v-btn>
    </v-speed-dial>
  </v-container>
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";
import EventosDataService from "../../services/EventosDataService";
/* import html2canvas from "html2canvas";*/
import jsPDF from "jspdf"; 
import 'jspdf-autotable'

export default {
  name: "HistorialEventos",
  data() {
    return {
      eventsAlumno: [],
      dataAlumno: [],
      eventsFormacion: [],
      totalCreditos: 0,
      alumnoPdf: [],
      heading: "Eventos",
      direction: 'bottom',
      fab: false,
      fling: false,
      hover: true,
      top: true,
      right: true,
      transition: 'slide-y-reverse-transition',
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
                this.alumnoPdf.push(response.data);
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
                    this.eventsAlumno.push(this.datosEvento(evento, response.data));
                    this.validarCreditos(evento, response.data)
                })
                .catch(e => {
                    console.log(e);
                })   
        }
    },
    datosEvento(evento, response){
        var status;
        if( evento.asistencia == 1){
            status = "Asistió";
        } else {
            status = "No asistió";
        }
        var data = {
            tituloEvento: response.tituloEvento,
            unidadResponsable: response.unidadResponsable,
            descripcionEvento: response.descripcionEvento,
            eventoDedicadoA: response.eventoDedicadoA,
            fechaEvento: response.fechaEvento,
            inicioEvento: response.inicioEvento,
            finEvento: response.finEvento,
            sede: response.sede,
            cupo: response.cupo,
            descripcion: response.descripcion,
            creditos: response.creditos,
            categorias: response.categorias,
            asistencia: status
        };
        return data;
    },
    validarCreditos(evento, response){
        var creditos = parseFloat(this.totalCreditos);
        var creditos2 = parseFloat(response.creditos);
        if(evento.asistencia == 1){
            var res = creditos + creditos2;
            this.totalCreditos =  res;
        }
    },
    createPDF(){
        const doc = new jsPDF({
            orientation: "portrait",
            unit: "in",
            format: "letter"
        });
        // text is placed using x, y coordinates
        doc.setFontSize(16).text("Historial de eventos", 0.5, 1.0);
        doc.setFontSize(16).text("Total de creditos: "+ this.totalCreditos, 5, 1.0);
        // create a line under heading 
        doc.setLineWidth(0.01).line(0.5, 1.1, 8.0, 1.1);
        doc.autoTable({
            headStyles: { fillColor: [149, 47, 87] },
            body: this.alumnoPdf,
            columns: [
                { header: 'Nombre', dataKey: 'nombres' },
                { header: 'Apellido', dataKey: 'apellidos' },
                { header: 'Matricula', dataKey: 'matricula' },
                { header: 'Carrera', dataKey: 'carrera' },
                { header: 'Semestre', dataKey: 'semestre' }
            ],
            margin: { left: 0.5, top: 1.3 }
        });

        doc.setLineWidth(0.01).line(0.5, 3.1, 8.0, 3.1);
        doc.autoTable({
            headStyles: { fillColor: [199, 0, 57] },
            body: this.eventsAlumno,
            columns: [
                { header: 'Eventos', dataKey: 'tituloEvento' },
                { header: 'Creditos', dataKey: 'creditos' },
                { header: 'Asistencia', dataKey: 'asistencia'}
            ],
            margin: { left: 0.5, top: 40.5 }
        });

        doc
            .setFont("times")
            .setFontSize(11)
            .text(
            "Universidad Júarez del Estado de Durango",
            0.5,
            doc.internal.pageSize.height - 0.5
            )
            .save(`${this.alumnoPdf[0].matricula}_${this.heading}.pdf`);
    }
  }
}
</script>

<style>
    #createDoc .v-speed-dial {
        position: absolute;
    }

    #createDoc .v-btn--floating {
        position: relative;
    }
</style>