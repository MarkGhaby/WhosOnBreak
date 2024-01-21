<template>
    <div>
      <!-- Display the schedule here -->
      <div v-if="mainUserSchedule && selectedUserSchedule">
        <!-- Show schedule grid and highlight common breaks -->
      </div>
      <div v-else>
        Select a user to view common breaks.
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      mainUserSchedule: Object,
      selectedUserSchedule: Object
    }
  };
  </script>
  