<template>
    <div class="w-[600px] bg-metal text-white mx-auto">
      <table class="col-span-6 py-2 text-center">
        <thead class="fixed-header">
          <tr>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Time</th>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Monday</th>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Tuesday</th>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Wednesday</th>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Thursday</th>
            <th class="box-border h-8 w-32 p-4 border-4 py-3 bg-cyan-800 rounded-lg">Friday</th>
          </tr>
        </thead>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(0, 4)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(4, 8)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(8, 12)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(12, 16)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(16, 20)" :key="index">{{timeSlot}}</div></th>
            <th class="py-3 bg-cyan-800 border-0" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(20, 24)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(24, 28)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(28, 32)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(32, 36)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(36, 40)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(40, 44)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(44, 48)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(48, 52)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(52, 56)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(56, 60)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(60, 64)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>
        <tr>
            <th><div class="py-3 bg-cyan-800 rounded-lg" v-for="(timeSlot, index) in timeSlots.slice(64, 68)" :key="index">{{timeSlot}}</div></th>
            <th class="border-0 py-3 bg-cyan-800 rounded-lg" v-for="n in 5" :key="n"></th>
        </tr>

      </table>
    </div>
</template>
  
  <script>

  import { defineComponent } from "vue"

  export default defineComponent ({
  name: "SchedulePage",

  data() {
    return {
      timeSlots: this.generateTimeSlots(),
    };
  },
  methods: {
    generateTimeSlots() {
      const startTime = 7 * 60;
      const endTime = 23 * 60;
      const interval = 15;

      const timeSlots = [];

      for (let i = startTime; i <= endTime; i += interval) {
        const hours = Math.floor(i / 60);
        const minutes = i % 60;
        const period = hours < 12 ? 'AM' : 'PM';
        const formattedTime = `${hours % 12 || 12}:${minutes === 0 ? '00' : minutes} ${period}`;
        timeSlots.push(formattedTime);
      }

      return timeSlots;
    },

    generateBreakSlots(){

        const inputData = [
            [0, 960, 975],
            [0, 1035, 1440],
            [2, 960, 975],
            [2, 1080, 1110],
            [2, 1230, 1440],
            [3, 825, 885],
            [3, 1050, 1440],
            [4, 960, 975],
            [4, 1080, 1110],
            [4, 1215, 1440],
        ];


//0 ,  960 ,  975 ; 0 ,  1035 ,  1440 ; 2 ,  960 ,  975 ; 2 ,  1080 ,  1110 ; 2 ,  1230 ,  1440 ; 3 ,  825 ,  885 ; 3 ,  1050 ,  1440 ; 4 ,  960 ,  975 ; 4 ,  1080 ,  1110 ; 4 ,  1215 ,  1440 ;

    }
  },
});


  </script>
  
  <style scoped>
  .table-container {
    max-height: 400px; /* Adjust the max height as needed */
    overflow-y: auto;
  }
  
  .fixed-header {
    position: sticky;
    top: 0;
    background-color: white; /* Adjust the background color as needed */
    z-index: 1;
  }
  </style>
  
  
