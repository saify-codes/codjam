// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA960SL05m-1SnIdbJ-CSlDEc7cw53-0jI",
  authDomain: "foody-7ffe6.firebaseapp.com",
  projectId: "foody-7ffe6",
  storageBucket: "foody-7ffe6.appspot.com",
  messagingSenderId: "963060222474",
  appId: "1:963060222474:web:a80e74071611bc11d12df3",
  measurementId: "G-9HZ93V1SV6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Firebase Authentication and get a reference to the service
export const auth = getAuth(app);
export const db = getFirestore(app)
export default app;
