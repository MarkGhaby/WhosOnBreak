import { boot } from "quasar/wrappers";
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async (/* { app, router, ... } */) => {
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBrEytYh8bptGQFB-C0_SsAbftR590xcZk",
    authDomain: "whosonbreak.firebaseapp.com",
    projectId: "whosonbreak",
    storageBucket: "whosonbreak.appspot.com",
    messagingSenderId: "1090757611930",
    appId: "1:1090757611930:web:24c35cc3cdd696c0276a23",
    measurementId: "G-LQYKHTPNGQ",
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
});
