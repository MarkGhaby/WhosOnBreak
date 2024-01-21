<template>
  <q-page padding>
    <div
      class="text-h3 text-center q-my-md"
      style="font-family: 'Playfair', sans-serif"
    >
      Introducing... Who's on Break?
    </div>
    <div
      class="text-subtitle1 text-center q-my-md"
      style="font-family: 'Playfair', sans-serif"
    >
      Don't spend your break alone! Upload your schedule and find out who's
      available in just a few clicks
    </div>
    <div class="q-pa-md row justify-center">
      <q-img
        src="/src/assets/whos_on_break_logo.png"
        class="rounded-borders"
        style="height: 300px; width: 500px; object-fit: cover"
      ></q-img>
    </div>
    <div elevated class="row justify-center q-my-md">
      <q-btn
        label="Sign Up"
        elevated
        class="bg-teal-400 text-color-white q-mr-md"
        @click="$router.push('/signup')"
      />
      <q-btn
        label="Log In"
        outline
        color="teal-400"
        @click="$router.push('/login')"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { getAuth, onAuthStateChanged } from "firebase/auth";

export default defineComponent({
  name: "IndexPage",

  setup() {
    onAuthStateChanged(getAuth(), (user) => {
      if (user) {
        console.log("User is signed in:", user);
      } else {
        console.log("User is signed out");
      }
    });
  },
});
</script>

<style>
.rounded-borders {
  border-radius: 10px;
}
</style>
