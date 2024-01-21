<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-teal-400">
      <q-toolbar>
        <div
          class="text-[#00000] font-bold text-3xl tracking-[-1.5px] cursor-pointer"
          @click="$router.push('/')"
        >
          Who's On Break?
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
