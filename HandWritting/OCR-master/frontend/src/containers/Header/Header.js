import React from "react";
import Navbar from "./Navbar/Navbar";
import video from "../../video/writing.mp4";

const Header = () => {
  return (
    <React.Fragment>
      <Navbar />
      <header id="home">
        <Navbar />
        <div class="banner">
          <div class="container">
            <video
              controls={false}

              muted={true}
              autoPlay={true}
              loop={true}
              class="video-container"

            >
              <source src={video} type="video/mp4" />
            </video>
            <h1>Handwriting Regconition</h1>
            <p>The Power Of Writing</p>
            <a href="#howitworks" class="scroll-link btn btn-white">
              explore more
            </a>
          </div>
        </div>
      </header>
    </React.Fragment>
  );
};

export default Header;
