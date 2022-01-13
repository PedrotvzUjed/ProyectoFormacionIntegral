<template>
  <v-container>
      <v-row>
        <v-card height="200px">
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
                    ></v-file-input>
                    <v-card-actions>
                        <v-btn
                            block
                            depressed
                            color="#a4010b"
                            class="white--text"
                        >
                            Subir evidencia
                        </v-btn>
                    </v-card-actions>
                </v-col>
                <v-col>
                    <v-row>
                        <v-img
                            lazy-src="https://picsum.photos/id/11/10/6"
                            max-height="150"
                            max-width="250"
                            src="https://picsum.photos/id/11/500/300"
                        ></v-img>
                    </v-row>
                </v-col>
            </v-row>
        </v-card>
      </v-row>
  </v-container>
</template>

<script>
export default {
    name: "EvidenciasAlumno",
    data (){
        return {
            rules: [
            value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',],

        }
    }
}
</script>

<style>

</style>