<template>
  <v-container id="createFile">
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
                                v-if="item.asistencia != 1"
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
            <download-excel
                class=""
                :data="eventsDataFiles"
                :fields="json_fields"
                type = "xls"
                :name="`${this.fileName}_${this.heading}.xls`"
                :header="alumnoExcel"
                :footer ="`Creditos validados: ${this.totalCreditos}`"
            >
                <v-icon>mdi-file-excel</v-icon>
            </download-excel>
        </v-btn>
        <v-btn
            fab
            dark
            color="indigo"
            @click="createDoc(alumnoDataFiles[0].matricula)"
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

/* import html2canvas from "html2canvas";*/
import jsPDF from "jspdf"; 
import 'jspdf-autotable';
import downloadExcel from "vue-json-excel";

export default {
  name: "HistorialEventos",
  data() {
    return {
      dataAlumno: [],
      eventsAlumno: [],
      totalCreditos: 0,
      alumnoDataFiles: [],
      eventsDataFiles: [],
      fileName: '',
      alumnoExcel: '',
      heading: "Eventos",
      direction: 'bottom',
      fab: false,
      fling: false,
      hover: true,
      top: true,
      right: true,
      transition: 'slide-y-reverse-transition',
      json_fields: {
        "Evento": "tituloEvento",
        "Unidad Responsable": "unidadResponsable",
        "Despcripción": "descripcionEvento",
        "Fecha del evento": "fechaEvento",
        "Sede": "sede",
        "Creditos de evento": "creditos",
        "Asistencia" :"asistencia"
      },
    };
  },
  created() {
      this.getAlumno();
      this.getEventsAlumno(); 
  },
  mounted() {
      
  },
  components: {
      downloadExcel 
  },
  methods: {
    getAlumno() {
        AlumnosDataService.get(this.$route.params.id)
            .then(response => {
                this.dataAlumno = response.data;
                this.alumnoDataFiles.push(response.data);
                this.fileName = response.data.matricula;
                this.alumnoExcel = "Alumno: "+ response.data.nombres + "  " + response.data.apellidos + "  " + "Matricula: " + response.data.matricula + "  "  + "Carrera: " + response.data.carrera + "  " + "Semestre: " + response.data.semestre;
            })
            .catch(e =>{
                console.log(e);
            })
    },
    getEventsAlumno(){
        FormacionInDataService.getEventsAlumno(this.$route.params.id)
        .then(response => {
            this.eventsAlumno = response.data;
            console.log(this.eventsAlumno);
            this.validarCreditos(response.data);
        })
        .catch(e => {
            console.log(e);
        })
    },
    validarCreditos(response){
        for (let evento of response) {
            var creditos = parseFloat(this.totalCreditos);
            var creditos2 = parseFloat(evento.creditos);
            if(evento.asistencia == 1){
                var res = creditos + creditos2;
                this.totalCreditos =  res;
            }
            this.createData(evento);
        }
    },
    createData(response){
        var status;
        if( response.asistencia == 1){
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
        this.eventsDataFiles.push(data);
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
            body: this.alumnoDataFiles,
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
            body: this.eventsDataFiles,
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
            .save(`${this.fileName}_${this.heading}.pdf`);
    },
    createDoc(alumno){
        FormacionInDataService.createDoc(alumno)
            .then(response => {
                console.log(response);
            })
            .catch(e => {
                console.log(e);
            })
    },
    startDownload(){
        alert('show loading');
    },
    finishDownload(){
        alert('hide loading');
    }
  }
}
</script>

<style>
    #createFile .v-speed-dial {
        position: absolute;
    }

    #createFile .v-btn--floating {
        position: relative;
    }
</style>