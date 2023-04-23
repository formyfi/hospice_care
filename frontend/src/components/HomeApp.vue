<template>
    <v-container class="container">
      <v-row>
        <v-col cols="6" sm="6">
          <v-card>
            <v-card-title color="primary">Hospice Care Helper</v-card-title>
            <img alt="Vue img" aspect-ratio="1" contain src="../assets/hospice.png" style="max-width: 50%; max-height: 50%;">
            <v-card-text>
              <v-form>
                <v-row>
                  <v-col cols="6" sm="6">
                    <v-select
                      :items="genderOptions"
                      label="Gender"
                      v-model="gender"
                      variant="underlined"
                      color="primary"
                    ></v-select>
                  </v-col>
                  <v-col cols="6" sm="6">
                    <v-text-field
                      v-model="age"
                      label="Enter Age"
                      type="number"
                      variant="underlined"
                      color="primary"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-text-field
                  v-model="currentCondition"
                  label="Current Condition"
                  multi-line
                  variant="underlined"
                  color="primary"
                  :style="{ width: 'calc(' + (100 / 12) * 6 + '% - 8px)' }"
                ></v-text-field>
                <v-textarea
                  v-model="userInput"
                  label="Enter your message"
                  placeholder="Type your message"
                  rows="3"
                  variant="underlined"
                  color="primary"
                ></v-textarea>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="sendForm">Send</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6" sm="6">
            
        </v-col>
      </v-row>
      <v-card v-if="loading" class="response-card">
        <v-card-text>Generating Response...</v-card-text>
      </v-card>
      <v-card v-else-if="res" class="response-card">
        <v-card-text>{{ res }}</v-card-text>
      </v-card>
    </v-container>
  </template>
  
  
  <script>
  import axios from 'axios';
  import {
    VBtn,
    VCard,
    VCardTitle,
    VCardText,
    VCardActions,
    VContainer,
    VForm,
    VCol,
    VRow,
    VSelect,
    VTextField,
    VTextarea,

  } from 'vuetify/lib/components';
  import 'vuetify/dist/vuetify.min.css';
  
  export default {
    components: {
      VBtn,
      VCard,
      VCardTitle,
      VCardText,
      VCardActions,
      VContainer,
      VForm,
      VCol,
      VRow,
      VSelect,
      VTextField,
      VTextarea,
    
    },
    data() {
      return {
        gender: null,
        age: '',
        currentCondition: '',
        userInput: '',
        apiUrl: 'http://127.0.0.1:8000/home/',
        genderOptions: ['Male', 'Female', 'Other'],
        res:'',
        message:'',
        loading: false,
      };
    },
    methods: {
      sendForm() {
        
        this.loading=true
        this.message = `Patient's gender is ${this.gender} and his/her age is ${this.age}. He is currently suffering with ${this.currentCondition} and is in hospice care. I have a question about this patient as follows: ${this.userInput}.`
        axios
          .get(this.apiUrl, {
            params: {
              prompt: this.message,
            },
            headers: {
              'Content-Type': 'application/json',
            },
          })
          .then((response) => {
            this.res = response.data.response
            
            this.loading=false
            // this.message = ''
            
            // this.gender = null
            // this.age = ''
            // this.currentCondition = ''
            // this.userInput =''
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
  };
  </script>

<style>
.container {
  max-width: 750px; /* set a maximum width for the container */
  margin: 0 auto; /* center the container horizontally */
  padding: 16px; /* add padding on all sides */
}
.response-card {
  margin-top: 16px;
}
</style>
  