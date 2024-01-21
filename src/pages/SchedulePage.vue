  <template>
    <q-layout view="lHh Lpr lFf">
      <q-header elevated class="bg-teal-400">
        <q-toolbar>
          <q-toolbar-title @click="$router.push('/')">
            Who's On Break?
          </q-toolbar-title>

          <!-- Spacer to push the button to the right -->
          <q-space></q-space>

          <q-btn flat round icon="person" size="lg" @click="toggleProfileMenu">
            <q-menu v-model="showProfile">
              <q-list>
                <q-item clickable v-close-popup @click="$router.push('/profile')">
                  <q-item-section>Profile</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="logout">
                  <q-item-section>Sign Out</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </q-toolbar>
      </q-header>

      <q-page-container>
        <user-selection :users="users" @user-selected="handleUserSelected"></user-selection>
        <schedule-display :mainUserSchedule="mainUserSchedule" :selectedUserSchedule="selectedUserSchedule"></schedule-display>
      </q-page-container>
    </q-layout>
  </template>

  <script>
  import UserSelection from '../components/UserSelection.vue';
  import ScheduleDisplay from '../components/ScheduleDisplay.vue';

  export default {
    components: {
      UserSelection,
      ScheduleDisplay
    },
    data() {
      return {
        users: ['Alice', 'Bob', 'Charlie'],
        mainUserSchedule: {}, // This should contain your main user's schedule data
        selectedUserSchedule: {}, // This will be updated when a user is selected
        showProfile: false // Controls the profile menu visibility
      };
    },
    methods: {
      handleUserSelected(selectedUserName) {
        this.selectedUserSchedule = this.mockFetchUserSchedule(selectedUserName);
      },
      mockFetchUserSchedule(userName) {
        return {
          name: userName,
          schedule: {/* ... simulated schedule data ... */}
        };
      },
      toggleProfileMenu() {
        this.showProfile = !this.showProfile;
      },
      logout() {
        this.showProfile = false;
        this.$router.push('/login');
      }
    },
    created() {
      // Initialize your main user's schedule here
      this.mainUserSchedule = {/* ... your schedule data ... */};
    }
  };
  </script>
