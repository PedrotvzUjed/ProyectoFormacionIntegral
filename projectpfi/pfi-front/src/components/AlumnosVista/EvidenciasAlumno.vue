<template>
  <v-container fluid>
      <v-row >
        <form action="POST">
            <v-card height="250px" v-if="evidencia.length == 0">
                <v-card-title>Subir evidencia</v-card-title>
                <v-row>
                    <v-col>
                        <v-file-input
                            :rules="rules"
                            small-chips
                            accept="image/png, image/jpeg, image/bmp"
                            placeholder="Seleccionar imagen "
                            prepend-icon="mdi-file"
                            label="Evidencia"
                            v-model="uploadFile.img"
                        ></v-file-input>
                        <v-card-actions>
                            <v-btn
                                block
                                depressed
                                color="#a4010b"
                                class="white--text"
                                @click="upload()"
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
            <v-card height="250px" v-else-if="evidencia[0] != []">
                <v-card-title>Actualizar evidencia</v-card-title>
                <v-row>
                    <v-col>
                        <v-file-input
                            :rules="rules"
                            small-chips
                            accept="image/png, image/jpeg, image/bmp"
                            placeholder="Seleccionar imagen "
                            prepend-icon="mdi-file"
                            label="Evidencia"
                        ></v-file-input>
                        <v-card-actions>
                            <v-btn
                                block
                                depressed
                                color="#a4010b"
                                class="white--text"
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
    data (){
        return {
            rules: [
            value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',],
            evidencia: [],
            uploadFile: {
                img: null,
                evento: null,
                alumno: null,
            }
        }
    },
    methods: {
        retrievEvidencia(evento, alumno){
            EventosDataService.getEvidencias(evento, alumno)
                .then(response => {
                    console.log(response.data);
                    this.evidencia = response.data;
                })
                .catch(e => {
                    console.log(e);
                })
        },
        upload(){
            this.uploadFile.evento = this.$route.params.id;
            this.uploadFile.alumno = 2;
            /* console.log(this.uploadFile) */
            EventosDataService.createEvidencia(this.uploadFile)
                .then(response => {
                    console.log(response.data);
                })
                .catch(e => {
                    console.log(e);
                })
        }
    },
    created() {
        this.retrievEvidencia(this.$route.params.id, 2);
    },
}
</script>

<style>

</style>