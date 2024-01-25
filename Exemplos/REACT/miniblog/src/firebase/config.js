import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCK8ZX_gGTzPmsMmFOAUc0NFE2Y2gcX-lQ",
  authDomain: "miniblog-655e4.firebaseapp.com",
  projectId: "miniblog-655e4",
  storageBucket: "miniblog-655e4.appspot.com",
  messagingSenderId: "1031175169873",
  appId: "1:1031175169873:web:d4fadb65fa3d75b20c1570",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const db = getFirestore(app);

export { db };
