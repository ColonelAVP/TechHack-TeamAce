import React from "react";
import Maps from "../Components/Map";
import gif from "../assets/bandicam 2023-04-19 10-27-20-157 (1).gif"

const Home = () => {
  return (
    
    <div className='flex h-screen justify-center text-white '>
    <div className='z-10'><img src={gif} alt="" /></div>
    <Maps/>
    </div>
    
  
  );
};

export default Home;
