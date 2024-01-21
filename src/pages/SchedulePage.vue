<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-semibold mb-4">University Schedule</h1>
      <div class="grid grid-cols-6 gap-2">
        <!-- Empty cell in the top-left corner -->
        <div class="bg-gray-200 p-2"></div>
        <!-- Days of the week -->
        <div v-for="day in days" :key="day" class="bg-blue-200 p-2 text-center">
          {{ day }}
        </div>
        <!-- Time slots and schedule cells -->
        <div v-for="timeSlot in timeSlots" :key="timeSlot" class="bg-gray-200 p-2 text-center">
          {{ timeSlot }}
        </div>
        <div v-for="timeSlot in timeSlots" :key="timeSlot" class="border p-2 text-center">
          <!-- You can dynamically populate this with events for each day and time slot -->
          <!-- For simplicity, I'm displaying a placeholder 'Event' -->
          <div class="bg-green-300 p-1 rounded">{{ getEvent(timeSlot) }}</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import { defineComponent } from "vue"

  export default defineComponent ({
  name: "SchedulePage",
  });
  </script>
  
  <style scoped>
  /* You can add additional styling here */
  .grid {
    grid-template-rows: repeat(17, 1fr);
  }
  
  /* Adjust cell height as needed */
  .bg-gray-200,
  .bg-blue-200,
  .border {
    height: 40px;
  }
  </style>
  