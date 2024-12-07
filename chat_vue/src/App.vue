<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue';
import API from '@/services/api';

const inputGrade = ref<string>('');
const outputGrade = ref<string>('');
const verifyGrade = ref<string>('');
const dialog = ref<boolean>(false);
const wrong = ref<boolean>(false);
const surprise = ref<boolean>(false);

const formPush = ref({
  storeGrade: '',
})


function forms() {

  const submit = async () => {
    try {
      formPush.value.storeGrade = inputGrade.value.trim();
      inputGrade.value = '';
      const response = await API.post('broadcast/chat/', formPush.value, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken() // Include CSRF token if needed
        }
      })

      if(response.status === 200) {
        dialog.value = true;
      }
      
    }
    catch (error) {
      alert('Error submitting form: ' + error);
    }
  };

  const verify = async () => {
    if (verifyGrade.value.trim() === formPush.value.storeGrade) {
      outputGrade.value = 'Success';
    }
    else {
      outputGrade.value = 'Wrong message';
    }

    wrong.value = true;
    dialog.value = false;
    verifyGrade.value = '';
  }

  return { submit, verify }
};

const getCsrfToken = () => {
  return document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
};
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Vue + Vuetify + Django" />
    </div>
  </header>

  <v-app class="h-0 my-5">
    <v-form class="d-flex flex-row" ref="submitForm" @submit.prevent="forms().submit">
      <v-text-field bg-color="surface-variant" v-model="inputGrade" label="Input something..." :counter="20" maxLength="20" variant="outlined" />

      <v-dialog max-width="500" v-model="dialog" persistent>

        <template #activator="{ props }">
          <v-btn :props type="submit" height="55" text="Submit" class="rounded-0" />
        </template>


        <v-card title="Output" color="surface-variant">
          <v-form class="d-flex flex-row" ref="verifyForm" @submit.prevent="forms().verify">
            <v-text-field v-model="verifyGrade" label="Input something..." :counter="20" maxLength="20" />
            <v-btn type="submit" height="55" text="Submit" class="rounded-0" />
          </v-form>

        </v-card>

      </v-dialog>

    </v-form>

    <v-dialog max-width="500" v-model="wrong" persistent>
      <v-card color="surface-variant">
        <v-card-text>{{ outputGrade }}</v-card-text>
        <v-spacer />

        <v-btn color="surface-variant" text="Close"
          @click="wrong = false; outputGrade === 'Wrong message' ? surprise = true : ''" />

      </v-card>
    </v-dialog>

    <v-dialog v-model="surprise" width="100%" height="100%" persistent>
      <v-card>
        <iframe width="100%" height="100%"
          src="https://www.youtube.com/embed/JHPgcSBnpv4?autoplay=1&mute=1si=gdFW7g1_QPWV1zUq&amp;controls=0&amp;clip=Ugkx6FSFNtzecD7H7d7Xp8KlQP1i-BAErD0X&amp;clipt=EJyGBhikkQc"
          title="YouTube video player" frameborder="0"
          allow=" autoplay; encrypted-media; picture-in-picture; fullscreen"
          referrerpolicy="strict-origin-when-cross-origin"></iframe>
      </v-card>
    </v-dialog>

  </v-app>

</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
