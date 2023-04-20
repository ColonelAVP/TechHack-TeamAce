import React from "react";
import gif from "../assets/bandicam 2023-04-19 10-27-20-157 (1).gif";

function parking() {
  return (
    <div className="flex justify-center text-white z-10">
    <h1>Parking Solution with real time security survillance</h1>
      <div >
        <img src={gif} alt="" />
      </div>
    </div>
  );
}

export default parking;
