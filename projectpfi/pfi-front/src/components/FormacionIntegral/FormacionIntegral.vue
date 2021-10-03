<template>
  <div>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="eventos"
      :single-select="singleSelect"
      :single-expand="singleExpand"
      :expanded.sync="expanded"
      :search="search"
      item-key="id"
      show-select
      show-expand
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Eventos</v-toolbar-title>
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
      <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length">
          {{ item.descripcionEvento }}
        </td>
      </template>
    </v-data-table>
    <v-row>
      <v-btn
        depressed
        elevation="2"
        @click="sendEvent(selected)"
      >Registro y Asistencia</v-btn>
    </v-row>
    
  </div>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";

export default {
    name: "formacionIntegral",
    data() {
      return {
        eventos: [],
        singleSelect: true,
        selected: [],
        singleExpand: true,
        expanded: [],
        search: '',
        headers: [
          { text: 'Id', align: 'start', sortable: true, value: 'id'},
          { text: 'Titulo de evento', value: 'tituloEvento' },
          { text: 'Unidad responsable', value: 'unidadResponsable' },
          { text: 'Fecha de evento', sortable: true, value: 'fechaEvento' },
          { text: 'Cupo', value: 'cupo' },
          { text: 'Creditos', value: 'creditos' },
        ],
      };
    },
    methods: {
      retrieveEventos() {
        EventosDataService.getAll()
          .then(response => {
            this.eventos = response.data;
            console.log(this.eventos);
          })
          .catch(e => {
            console.log(e);
          });
      },
      sendEvent(evento) {
        console.log(evento)
        this.$router.push("/fi-registro/"+evento[0].id);
      }
    },
    mounted() {
      this.retrieveEventos();
    }
}
</script>

<style>

</style>