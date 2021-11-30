<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          block
          color = "#a4010b"
          text
        >Creditos obtenidos hasta ahora: {{totalcreditos}}</v-btn>
      </v-col>
      <v-col>
        
        <v-btn
          depressed
          elevation="2"
          block
          color = "#a4010b"
          class="white--text"
          @click="exportPDF()"
        >Exportar Tabla de eventos</v-btn>
        
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="eventos"
          :single-select="singleSelect"
          :search="search"
          item-key="id"
          show-select
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Eventos registrados</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Buscar"
                single-line
                hide-details
              ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:no-data> Espere un momento! </template>
        </v-data-table>
      </v-col>
      <v-col>
        <info-Evento :evento="selected[0]"></info-Evento>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";
import jsPDF from "jspdf";
import 'jspdf-autotable';

import infoEvento from "../Eventos/EventoInfoAlumno";

export default {
  name: "formacionIntegral",
  data() {
    return {
      formaciones: [],
      formacionescreditos: [],
      eventos: [],
      totalcreditos: 0,
      singleSelect: true,
      asignados: [],
      selected: [
        {
          tituloEvento: "",
          unidadResponsable: "",
          descripcionEvento: "",
          eventoDedicadoA: "",
          fechaEvento: "",
          inicioEvento: "",
          finEvento: "",
          sede: "",
          cupo: "",
          descripcion: "",
          creditos: "",
          categorias: "",
        },
      ],
      singleExpand: true,
      expanded: [],
      search: "",
      headers: [
        //{ text: "Id", align: "start", sortable: true, value: "id" },
        { text: "Titulo de evento", value: "tituloEvento" },
        { text: "Unidad responsable", value: "unidadResponsable" },
        { text: "Fecha de evento", sortable: true, value: "fechaEvento" },
        { text: "Creditos", value: "creditos" },
      ],
    };
  },
  components: {
    infoEvento,
  },
  methods: {
    retrieveFormacionesByMatricula() {
      FormacionInDataService.getRaw()
        .then((response) => {
          

          let formacionesbymatricula = response.data.filter(function (i) {
            return i.matricula === "1234567897";
          });

          let formacionesbyasistencia = formacionesbymatricula.filter(function(i){
            return i.asistencia !== 0;
          });

          let formacionesbycreditos = formacionesbymatricula.filter(function(i){
            return i.asistencia === 1;
          });

          this.formacionescreditos = formacionesbycreditos;
          this.formaciones = formacionesbyasistencia;
          console.log(this.formaciones);
          console.log(this.formacionescreditos);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    retrieveEventos() {
      EventosDataService.getAll()
        .then((response) => {

          var idseventos = this.formaciones;
          var idseventoscreditos = this.formacionescreditos;
          
          const ids = idseventos.map(x => x.evento)
          console.log(ids);

          let eventosbyid = ids.map(i => response.data.find(({id}) => i === id));

          const idscreditos = idseventoscreditos.map(x => x.evento)
          console.log(idscreditos);

          let eventosbyidcreditos = idscreditos.map(i => response.data.find(({id}) => i === id));

          /*let eventosbymatricula = response.data.filter(function (i) {
            return i.id == idseventos.filter(function (i) {
            return i.evento});
          });*/ 

          let creditos = eventosbyidcreditos.map(x=> x.creditos)
          console.log(creditos);
          
          let sumacreditos = 0;

          creditos.forEach(function(valor){
            sumacreditos += parseFloat(valor)
          });
          this.totalcreditos = sumacreditos

          this.eventos = eventosbyid;
          console.log(this.eventos);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    exportPDF() {
      var columns = [
        {title: "Titulo de evento", dataKey: "tituloEvento"},
        {title: "Unidad responsable", dataKey: "unidadResponsable"},
        {title: "Fecha de evento", sortable: true, dataKey: "fechaEvento"},
        {title: "Creditos", dataKey: "creditos"},
      ];
      var doc = new jsPDF('p', 'pt');
      doc.text('Lista de Eventos           Creditos Totales obtenidos: ' + this.totalcreditos , 40, 40);
      doc.autoTable(columns, this.eventos, {
        margin: {top: 60},
      });
      doc.save('Lista de Eventos.pdf');
    },
  

    /*       sendEvent(evento) {
        console.log(evento)
        this.$router.push("/fi-registro/"+evento.id);
      } */
  },
  mounted() {
    //this.retrieveAlumnos(this.$route.params.id);
  },
  created() {
    this.retrieveFormacionesByMatricula();
    this.retrieveEventos();
    //console.log(this.ejemplo);
    //this.retrieveAlumnos(this.$route.params.id);
  },
};
</script>

<style>
</style>