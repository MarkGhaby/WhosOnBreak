<template>
    <div>
      <q-list bordered class="rounded-borders">
        <q-item-label header>Select a user to view common breaks.</q-item-label>
        <q-item v-for="user in users" :key="user" clickable @click="selectUser(user)">
          <q-item-section>{{ user }}</q-item-section>
        </q-item>
      </q-list>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      users: Array
    },
    methods: {
      selectUser(user) {
        this.$emit('user-selected', user);
      }
    }
  };
  </script>
  