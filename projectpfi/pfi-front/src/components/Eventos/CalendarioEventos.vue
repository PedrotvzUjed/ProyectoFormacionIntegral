<template>
  <v-container>
    <v-row class="fill-height">
      <v-col>
        <v-sheet height="64">
          <v-toolbar flat>
            <v-btn
              outlined
              class="mr-4"
              color="grey darken-2"
              @click="setToday"
            >
              Hoy
            </v-btn>
            <v-btn fab text small color="grey darken-2" @click="prev">
              <v-icon small>
                mdi-chevron-left
              </v-icon>
            </v-btn>
            <v-btn fab text small color="grey darken-2" @click="next">
              <v-icon small>
                mdi-chevron-right
              </v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-menu bottom right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn outlined color="grey darken-2" v-bind="attrs" v-on="on">
                  <span>{{ typeToLabel[type] }}</span>
                  <v-icon right>
                    mdi-menu-down
                  </v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item @click="type = 'day'">
                  <v-list-item-title>Dia</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = 'week'">
                  <v-list-item-title>Semana</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = 'month'">
                  <v-list-item-title>Mes</v-list-item-title>
                </v-list-item>
                <v-list-item @click="type = '4day'">
                  <v-list-item-title>4 Dias</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-toolbar>
        </v-sheet>
        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="focus"
            color="primary"
            :events="events"
            :event-color="getEventColor"
            :type="type"
            @click:event="showEvent"
            @click:more="viewDay"
            @click:date="viewDay"
            locale="Es"
          ></v-calendar>
          <v-menu
            v-model="selectedOpen"
            :close-on-content-click="false"
            :activator="selectedElement"
            offset-x
          >
            <v-card color="grey lighten-4" min-width="350px" flat>
              <v-toolbar :color="selectedEvent.color" dark>
                <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <span v-html="selectedEvent.details"></span>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  text
                  color="secondary"
                  @click="
                    sendEvent(selectedEvent.evento), (selectedOpen = false)
                  "
                >
                  Más Información
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-menu>
        </v-sheet>
      </v-col>
      <v-col>
        <v-data-table
          :headers="headers"
          :items="eventsToday"
          item-key="id"
          class="elevation-1"
          hide-default-footer
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Eventos del dia de hoy!!</v-toolbar-title>
            </v-toolbar>
          </template>
          <template v-slot:item.detalles="{ item }">
            <v-btn class="ma-2" @click="sendEvent(item.id)">
              <v-icon>
                mdi-details
              </v-icon>
            </v-btn>
          </template>
          <template v-slot:no-data>
            No hay eventos el dia de hoy!
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row id="details">
      <info-Evento :evento="selected"></info-Evento>
    </v-row>
  </v-container>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";
import infoEvento from "../Eventos/InfoEvento";

export default {
  name: "calendario",
  data() {
    return {
      focus: "",
      type: "month",
      typeToLabel: {
        month: "Mes",
        week: "Semana",
        day: "Dia",
        "4day": "4 Dias",
      },
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      eventsToday: [],
      headers: [
        { text: "Titulo de evento", value: "tituloEvento" },
        { text: "Unidad responsable", value: "unidadResponsable" },
        { text: "Cupo", value: "cupo" },
        { text: "Detalles", value: "detalles" },
      ],
      selected: {
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
      colors: [
        "blue",
        "indigo",
        "deep-purple",
        "cyan",
        "green",
        "orange",
        "grey darken-1",
      ],
    };
  },
  components: {
    infoEvento,
  },
  mounted() {
    this.$refs.calendar.checkChange();
    console.log(this.selected);
  },
  created() {
    this.getEvents();
    this.getEventsToday();
  },
  methods: {
    viewDay({ date }) {
      this.focus = date;
      this.type = "day";
    },
    getEventColor(event) {
      return event.color;
    },
    setToday() {
      this.focus = "";
    },
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        requestAnimationFrame(() =>
          requestAnimationFrame(() => (this.selectedOpen = true))
        );
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }
      nativeEvent.stopPropagation();
    },
    getEvents() {
      EventosDataService.getAllCalendario()
        .then((response) => {
          this.events = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getEventsToday() {
      EventosDataService.getTodayEvents(this.getDate())
        .then((response) => {
          this.eventsToday = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getDate() {
      var dd = new Date();
      var y = dd.getFullYear();
      var m = dd.getMonth() + 1;
      var d = dd.getDate();
      m = m < 10 ? "0" + m : m;
      d = d < 10 ? "0" + d : d;
      var today = y + "-" + m + "-" + d;
      return today;
    },
    sendEvent(id) {
      EventosDataService.get(id)
        .then((response) => {
          this.selected = response.data;
          console.log(this.selected);
        })
        .catch((e) => {
          console.log(e);
        });
        setTimeout(this.scrollView, 1000);
    },
    scrollView() {
      const el = this.$el.querySelector("#details");
      if (el) {
        el.scrollIntoView();
      }
    },
  },
};
</script>

<style></style>
