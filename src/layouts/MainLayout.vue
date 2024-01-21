<template>
  <input
    type="file"
    ref="fileInput"
    style="display: none"
    @change="handleFileChange"
  />
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-teal-400">
      <q-toolbar>
        <div
          class="text-[#00000] font-bold text-3xl tracking-[-1.5px] cursor-pointer"
          @click="$router.push('/')"
        >
          Who's On Break?
        </div>

        <div class="absolute right-0 mr-[24px]">
          <div v-if="isUserSignedIn">
            <q-btn flat round>
              <q-icon name="person" size="30px" />
            </q-btn>
            <q-menu v-model="menuVisible">
              <q-list>
                <q-item clickable v-close-popup @click="triggerFileUpload">
                  <q-item-section>Upload a Schedule</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="signOut">
                  <q-item-section>Sign Out</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </div>
          <div v-else @click="$router.push('/login')">
            <q-btn flat round>
              <q-icon name="person" size="30px" />
            </q-btn>
          </div>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref, onMounted } from "vue";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { useRouter } from "vue-router";
import axios from "axios";

export default defineComponent({
  name: "MainLayout",

  setup() {
    const menuVisible = ref(false);
    const isUserSignedIn = ref(false);
    const fileInput = ref(null);
    const auth = getAuth();
    const router = useRouter();

    onMounted(() => {
      onAuthStateChanged(auth, (user) => {
        isUserSignedIn.value = user;
      });
    });

    const triggerFileUpload = () => {
      fileInput.value.click();
    };

    const handleFileChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append("file", file);

        axios
          .post("http://127.0.0.1:5000/upload", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            console.log("File uploaded successfully " + response.data);
            // Handle successful response
          })
          .catch((error) => {
            console.error("Error uploading file", error);
            // Handle error
          });
      }
    };

    const toggleMenu = () => {
      menuVisible.value = !menuVisible.value;
    };

    const signOut = async () => {
      try {
        await auth.signOut();
        isUserSignedIn.value = false;
        router.push("/login");
      } catch (error) {
        console.error("Sign out error:", error);
      }
    };

    return {
      menuVisible,
      isUserSignedIn,
      fileInput,
      triggerFileUpload,
      handleFileChange,
      signOut,
    };
  },
});
</script>
