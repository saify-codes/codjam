import React, { useState, useEffect } from "react";
import { onAuthStateChanged } from "firebase/auth";
import { auth } from "./firebase";
import Nav from "./components/nav";
import Food from "./API"
const Home = () => {
  
  useEffect(() => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // User is signed in, see docs for a list of available properties
        // https://firebase.google.com/docs/reference/js/firebase.User
        const uid = user.uid;

        console.log("uid", uid);
      } else {
        // User is signed out
        console.log("user is logged out");
      }
    });
  }, []);

  return (
    <>
      <Nav action="login" />
      <Food/>
    </>
  );
};

export default Home;
