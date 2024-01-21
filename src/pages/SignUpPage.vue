<template>
    <q-page class="flex flex-center">
      <div class="q-pa-md" style="max-width: 400px">
        <div class="text-h5 text-center q-mb-md">Sign Up</div>
        <q-form @submit.prevent="onSubmit" class="q-gutter-md">
          <q-input filled v-model="email" label="Email" type="email" :dense="false" lazy-rules :rules="[val => val && val.length > 0 || 'Please type something']" />
          <q-input filled v-model="fullName" label="Full Name" type="text" :dense="false" lazy-rules :rules="[val => val && val.length > 0 || 'Please type something']" />
          <q-input filled v-model="password" label="Password" type="password" :dense="false" lazy-rules :rules="[val => val && val.length > 0 || 'Please type something']" />
          <div class="row q-mt-lg">
            <q-btn label="Sign Up" type="submit" color="primary" class="full-width" />
          </div>
          <div class="row justify-center q-mt-md">
            <q-btn flat label="Already Have an Account? Login" @click="onLogin" color="primary" />
          </div>
        </q-form>
      </div>
    </q-page>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'SignUpPage',
    setup() {
      const email = ref('');
      const fullName = ref('');
      const password = ref('');
  
      const onSubmit = () => {
        // Handle the sign-up logic, such as validating input and sending data to your server
        console.log('Sign-up submitted:', { email: email.value, fullName: fullName.value, password: password.value });
      };
  
      const onLogin = () => {
        // Redirect to login page
        console.log('Redirect to login');
      };
  
      return {
        email,
        fullName,
        password,
        onSubmit,
        onLogin,
      };
    },
  });
  </script>
  