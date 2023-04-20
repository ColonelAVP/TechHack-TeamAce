import React from "react";
import Templete from "../Components/Templete";
import SignupImg from "../assets/signup.png";

function Signup({ setIsLoggedIn }) {
  return (
    <div>
      {" "}
      <Templete
        title='Make a smart move'
        desc1='For better, tomorrow and beyond.'
        desc2='Join us'
        image={SignupImg}
        formtype='signup'
        setIsLoggedIn={setIsLoggedIn}
      />
    </div>
  );
}

export default Signup;
