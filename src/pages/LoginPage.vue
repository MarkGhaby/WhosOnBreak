<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 400px">
      <div class="text-h5 text-center q-mb-md">Login</div>
      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input
          filled
          v-model="email"
          label="Email"
          type="email"
          :dense="false"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Please type something']"
        />
        <q-input
          filled
          v-model="password"
          label="Password"
          type="password"
          :dense="false"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Please type something']"
        />
        <div class="row q-mt-lg">
          <q-btn
            label="Login"
            type="submit"
            color="primary"
            class="full-width"
          />
        </div>
        <div class="row justify-center q-mt-md">
          <q-btn
            flat
            label="Not Registered? Sign Up"
            @click="$router.push('/signup')"
            color="primary"
          />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import {
  getAuth,
  signInWithEmailAndPassword,
  onAuthStateChanged,
} from "firebase/auth";
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "LoginPage",
  setup() {
    const email = ref("");
    const password = ref("");

    const onSubmit = async () => {
      const auth = getAuth();
      // Here you would usually handle the login logic, like sending the data to your server
      console.log("Form submitted:", {
        email: email.value,
        password: password.value,
      });
      try {
        await signInWithEmailAndPassword(auth, email.value, password.value);
      } catch (error) {
        console.log(error);
      }
    };

    onAuthStateChanged(getAuth(), (user) => {
      if (user) {
        // User is signed in
        console.log("User is signed in:", user);
        window.location.href = "/";
      } else {
        // User is signed out
        console.log("User is signed out");
      }
    });

    const onReset = () => {
      email.value = "";
      password.value = "";
    };

    const onSignUp = () => {
      // Handle sign up action, like redirecting to the sign-up page
      console.log("Redirect to sign up");
    };

    return {
      email,
      password,
      onSubmit,
      onReset,
      onSignUp,
    };
  },
});
</script>
