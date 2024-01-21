<template>
  <div class="schedule-container">
    <table class="schedule-table">
      <thead>
        <tr>
          <th class="header">Time</th>
          <th class="header" v-for="day in days" :key="day">{{ day }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(timeSlot, index) in timeSlots" :key="index">
          <td class="time-slot">{{ timeSlot }}</td>
          <td
            v-for="dayIndex in 5"
            :key="dayIndex"
            :class="getScheduleClass(dayIndex - 1, timeSlot)"
          ></td>
        </tr>
      </tbody>
    </table>
    <div class="legend">
      <div class="legend-item">
        <span class="dot your-schedule"></span> Your Schedule
      </div>
      <div class="legend-item">
        <span class="dot common-break"></span> Common Breaks with Alice
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "SchedulePage",

  data() {
    return {
      timeSlots: this.generateTimeSlots(),
      days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      userSchedule: this.generateUserSchedule(),
      commonBreaksWithAlice: this.generateCommonBreaksWithAlice(),
    };
  },

  methods: {
    generateTimeSlots() {
      const startTime = 7 * 60; // Start at 7:00 AM
      const endTime = 23 * 60; // End at 11:00 PM
      const interval = 15; // 15-minute intervals
      let slots = [];
      for (let time = startTime; time <= endTime; time += interval) {
        let hours = Math.floor(time / 60);
        let minutes = time % 60;
        let formattedTime = `${hours % 12 === 0 ? 12 : hours % 12}:${minutes
          .toString()
          .padStart(2, "0")} ${hours < 12 ? "AM" : "PM"}`;
        slots.push(formattedTime);
      }
      return slots;
    },

    generateUserSchedule() {
      // Your schedule data (Modify as needed)
      let schedule = new Array(5).fill(null).map(() => []);
      // Example: User has a schedule on Monday from 9:00 AM to 10:15 AM
      schedule[0].push({ start: 540, end: 615 }); // Convert time to minutes
      return schedule;
    },

    generateCommonBreaksWithAlice() {
      // Hardcoded common break data with Alice
      return {
        0: [
          { start: 960, end: 975 },
          { start: 1035, end: 1440 },
        ],
        2: [
          { start: 960, end: 975 },
          { start: 1080, end: 1110 },
          { start: 1230, end: 1440 },
        ],
        3: [
          { start: 825, end: 885 },
          { start: 1050, end: 1440 },
        ],
        4: [
          { start: 960, end: 975 },
          { start: 1080, end: 1110 },
          { start: 1215, end: 1440 },
        ],
      };
    },

    getScheduleClass(dayIndex, timeSlot) {
      const currentMinutes = this.timeToMinutes(timeSlot);
      const isUserScheduled = this.userSchedule[dayIndex].some(
        ({ start, end }) => currentMinutes >= start && currentMinutes < end
      );
      const isCommonBreak = this.commonBreaksWithAlice[dayIndex]?.some(
        ({ start, end }) => currentMinutes >= start && currentMinutes < end
      );

      if (isCommonBreak) return "common-break";
      if (isUserScheduled) return "your-schedule";
      return "unscheduled";
    },

    timeToMinutes(timeString) {
      const [time, period] = timeString.split(" ");
      let [hours, minutes] = time.split(":").map(Number);
      hours = period === "PM" ? (hours % 12) + 12 : hours % 12;
      return hours * 60 + minutes;
    },
  },
});
</script>

<style scoped>
.schedule-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.schedule-table {
  border-collapse: collapse;
  margin-right: 20px; /* Space between table and legend */
}

.header {
  background-color: #4fd1c5;
  color: white;
  padding: 8px;
  text-align: center;
}

.time-slot {
  background-color: #2c7a7b;
  color: white;
  padding: 8px;
  text-align: center;
}

.your-schedule {
  background-color: #82e9de; /* Light color for your schedule */
}

.common-break {
  background-color: #2c6a6a; /* Different color for common breaks */
}

.unscheduled {
  background-color: #2c7a7b; /* Neutral color for unscheduled slots */
}

.legend {
  display: flex;
  flex-direction: column;
}

.legend-item {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.dot {
  height: 15px;
  width: 15px;
  border-radius: 50%;
  display: inline-block;
  margin-right: 10px;
}
</style>
