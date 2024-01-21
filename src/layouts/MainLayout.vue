<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-teal-400">
      <q-toolbar>
        <q-toolbar-title @click="$router.push('/')">
          Who's On Break?
        </q-toolbar-title>

        <div v-if="isUserSignedIn">
          <q-btn flat round>
            <q-icon name="person" size="30px" />
          </q-btn>
          <q-menu v-model="menuVisible">
            <q-list>
              <q-item clickable v-close-popup>
                <q-item-section>Profile</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="signOut">
                <q-item-section>Sign Out</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </div>
        <div v-else @click="$router.push('/login')">
          <q-icon name="person" size="30px"></q-icon>
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

export default defineComponent({
  name: "MainLayout",

  setup() {
    const menuVisible = ref(false);
    const isUserSignedIn = ref(false);
    const auth = getAuth();
    const router = useRouter();

    onMounted(() => {
      onAuthStateChanged(auth, (user) => {
        isUserSignedIn.value = user;
      });
    });

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

    return { menuVisible, isUserSignedIn, toggleMenu, signOut };
  },
});
</script>
