<template>
  <v-card v-if="evento.tituloEvento != ''"
    elevation="8"
  >
    <v-img
      height="150"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>{{ evento.tituloEvento }}</v-card-title>

    <v-card-text>
      <v-row>
        <label><strong>Descripcion del evento:</strong></label>
        <v-spacer></v-spacer>
        <label>{{ evento.descripcionEvento }}</label>
      </v-row>
      <v-row>
        <label><strong>Unidad Responsable del evento: </strong></label>
        <v-spacer></v-spacer>
        <label>{{ evento.unidadResponsable }}</label>
      </v-row>
      <v-row>
        <label><strong>Evento dedicado a: </strong></label>
        <v-spacer></v-spacer>
        <label>{{ evento.eventoDedicadoA }}</label>
      </v-row>
      <v-row>
        <v-col>
          <label><strong>Fecha del evento:</strong></label>
        </v-col>
        <v-col>
          <label> {{ evento.fechaEvento }}</label>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <label><strong>Hora de inicio del evento: </strong>{{ evento.inicioEvento }}</label>
        </v-col>
        <v-col>
          <label><strong>Hora del final del evento: </strong> {{ evento.finEvento }} </label>
        </v-col>
      </v-row>
      <v-row>
        <label><strong>Sede del evento:</strong></label>
        <v-spacer></v-spacer>
        <label>{{ evento.sede }}</label>
      </v-row>
      <v-row>
        <v-col>
          <label><strong>Cupo del evento:</strong></label>
        </v-col>
        <v-col>
          <label> {{ evento.cupo }}</label>
        </v-col>
      </v-row>

      <v-row>
        <label><strong>Descripción: </strong></label>
        <v-spacer></v-spacer>
        <label>{{ evento.descripcion }}</label>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-btn
        block
        depressed
        color="error"
        @click="sendEvent(evento)"
      >
        Registro y Asistencia
      </v-btn>
    </v-card-actions>
  </v-card>

  <v-card class="align-center" elevation="8" v-else>
    <v-card-text>
      <v-row>
        <h4>Favor de seleccionar un evento para mas detalles</h4>
      </v-row>
      <v-row class="center">
        <v-btn
          loading
          text
          x-large
        ></v-btn>
      </v-row>
      
    </v-card-text>
    <v-card-actions>
      <v-btn
        block
        depressed
        disabled
        color="error"
      >
        Registro y Asistencia
      </v-btn>
    </v-card-actions>
  </v-card>
  <!-- <v-row v-else>
    <div>
        <p>Por favor selecciona un Evento para ver más información del mismo</p>
    </div>
  </v-row> -->
</template>

<script>
export default {
    name: 'info-Evento',
    data() {
      return {

      };
    },
    props: {
        evento: {
            type: Object,
        }
    },
    methods: {
      sendEvent(evento) {
        console.log(evento)
        this.$router.push("/fi-registro/"+evento.id);
      }
    }
}
</script>

<style>

</style>