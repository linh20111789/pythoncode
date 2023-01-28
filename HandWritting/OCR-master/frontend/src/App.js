import React from "react";

import Header from "./containers/Header/Header";
// import About from "./containers/About/About";
import HowItWorks from "./containers/HowItWorks/HowItWorks";
import Ocr from "./containers/Ocr/Ocr";
import Footer from "./containers/Footer/Footer";

const App = () => {
  return (
    <React.Fragment>
      <Header />
      <Ocr />
      <HowItWorks />
      {/* <About /> */}
      <Footer />
    </React.Fragment>
  );
};

export default App;
