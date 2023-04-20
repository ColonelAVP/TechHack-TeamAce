import React from "react";
import Templete from "../Components/Templete";
import loginImg from "../assets/login.png";
function Login({ setIsLoggedIn }) {
  return (
    <div>
      <Templete
        title='Welcome Back'
        desc1='For better, tomorrow and beyond.'
        desc2='Join us'
        image={loginImg}
        formtype='login'
        setIsLoggedIn={setIsLoggedIn}
      />
    </div>
  );
}

export default Login;
