<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 400px">
      <div class="text-h5 text-center q-mb-md">Sign Up</div>
      <q-form @submit.prevent="onSubmit" class="q-gutter-md">
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
          v-model="fullName"
          label="Full Name"
          type="text"
          :dense="false"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Please type something']"
        />
        <q-input
          filled
          v-model="userPassword"
          label="Password"
          type="password"
          :dense="false"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Please type something']"
        />
        <div class="row q-mt-lg">
          <q-btn
            label="Sign Up"
            type="submit"
            elevated
            class="bg-teal-400 full-width text-color-white"
          />
        </div>
        <div class="row justify-center q-mt-md">
          <q-btn
            flat
            label="Already Have an Account? Login"
            @click="$router.push('/login')"
            elevated
            class="bg-teal-400 full-width text-color-white"
          />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getDatabase, ref as dbRef, set } from "firebase/database";

export default defineComponent({
  name: "SignUpPage",
  setup() {
    const email = ref("");
    const fullName = ref("");
    const userPassword = ref("");

    const onSubmit = async () => {
      const userData = {
        email: email.value,
        firstName: fullName.value.split(" ")[0],
        lastName: fullName.value.split(" ")[1],
      };

      console.log(userData);

      const auth = getAuth();
      try {
        const userCredential = await createUserWithEmailAndPassword(
          auth,
          userData.email,
          userPassword.value
        );
        console.log("Sign In Success.\n" + userCredential.user.uid);

        // Add user to Realtime Database
        const db = getDatabase();
        const uid = userCredential.user.uid;
        await set(dbRef(db, "Users/" + uid), {
          email: userData.email,
          firstName: userData.firstName,
          lastName: userData.lastName,
        });
        window.location.href = "/";
      } catch (error) {
        console.log(error);
      }
    };

    const onLogin = () => {
      // Redirect to login page
      console.log("Redirect to login");
    };

    return {
      email,
      fullName,
      userPassword,
      onSubmit,
      onLogin,
    };
  },
});
</script>
