<template>
  <q-page class="flex flex-center">
    <p>Hello</p>
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
        // User is signed in
        console.log("User is signed in:", user);
      } else {
        // User is signed out
        console.log("User is signed out");
      }
    });
  },
});
</script>
