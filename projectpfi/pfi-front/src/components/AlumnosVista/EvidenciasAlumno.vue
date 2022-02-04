<template>
  <v-container fluid>
    <v-row v-if="evidencia.length == 0">
      <form @submit.prevent="create">
        <v-card height="250px">
          <v-card-title>Subir evidencia</v-card-title>
          <v-row>
            <v-col>
              <v-file-input
                :rules="rules"
                small-chips
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Seleccionar imagen "
                prepend-icon="mdi-file"
                @change="getImage($event)"
                required
              ></v-file-input>
              <v-card-actions>
                <v-btn
                  block
                  depressed
                  type="submit"
                  color="#a4010b"
                  class="white--text"
                  :disabled="active"
                >
                  Subir evidencia
                </v-btn>
              </v-card-actions>
            </v-col>
            <v-col>
              <v-container fluid>
                <v-row justify="space-around" style="padding-top: 10px">
                  <v-img
                    lazy-src="https://st3.depositphotos.com/2927609/32461/v/600/depositphotos_324611032-stock-illustration-no-image-vector-icon-no.jpg"
                    max-height="150"
                    max-width="150"
                    src="https://st3.depositphotos.com/2927609/32461/v/600/depositphotos_324611032-stock-illustration-no-image-vector-icon-no.jpg"
                  ></v-img>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-card>
      </form>
    </v-row>
    <v-row v-else-if="evidencia[0] != []">
      <form @submit.prevent="update">
        <v-card height="250px">
          <v-card-title>Actualizar evidencia</v-card-title>
          <v-row>
            <v-col>
              <v-file-input
                :rules="rules"
                small-chips
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Seleccionar imagen "
                prepend-icon="mdi-file"
                @change="getImage($event)"
                required
              ></v-file-input>
              <v-card-actions>
                <v-btn
                  block
                  depressed
                  type="submit"
                  color="#a4010b"
                  class="white--text"
                  :disabled="active"
                >
                  Actualizar evidencia
                </v-btn>
              </v-card-actions>
            </v-col>
            <v-col>
              <v-container fluid>
                <v-row justify="space-around" style="padding-top: 10px">
                  <v-img
                    :lazy-src="evidencia[0].img"
                    max-height="150"
                    max-width="250"
                    :src="evidencia[0].img"
                  ></v-img>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-card>
      </form>
    </v-row>
  </v-container>
</template>

<script>
import EventosDataService from "../../services/EventosDataService";

export default {
  name: "EvidenciasAlumno",
  data() {
    return {
      rules: [
        (value) =>
          !value ||
          value.size < 12000000 ||
          "La imagen debe pesar maximo 12 MB!",
      ],
      evidencia: [],
      data: {
        img: "",
        evento: "",
        alumno: "",
      },
      active: true,
    };
  },
  methods: {
    retrievEvidencia(evento, alumno) {
      EventosDataService.getEvidencias(evento, alumno)
        .then((response) => {
          console.log(response.data);
          this.evidencia = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    getImage(event) {
      this.data.img = event;
      this.data.evento = this.$route.params.id;
      this.data.alumno = 2;
      if (event != null) {
        this.active = false;
      } else {
        this.active = true;
      }
    },

    create: function() {
      this.active = true;
      let formData = new FormData();
      /*
                    Add the form data we need to submit
                */
      formData.append("img", this.data.img);
      formData.append("evento", this.data.evento);
      formData.append("alumno", this.data.alumno);
      /*
                  Make the request to the POST /single-file URL
                */
      EventosDataService.createEvidencia(formData)
        .then((response) => {
          console.log(response);
          this.retrievEvidencia(this.$route.params.id, 2);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    update: function() {
      this.active = true;
      let formData = new FormData();

      /*
                    Add the form data we need to submit
                */
      formData.append("img", this.data.img);
      formData.append("evento", this.data.evento);
      formData.append("alumno", this.data.alumno);

      EventosDataService.updateEvidencia(formData, this.evidencia[0].id)
        .then((response) => {
          console.log(response.data);
          this.retrievEvidencia(this.$route.params.id, 2);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  created() {
    this.retrievEvidencia(this.$route.params.id, 2);
  },
};
</script>

<style></style>
