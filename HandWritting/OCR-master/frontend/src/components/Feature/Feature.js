import React, { useState } from "react";
import Result from "../../result/result.txt";
import "./Feature.css";
import axios from "axios";

const Feature = () => {
  const [previewImage, setPreviewImage] = useState(false);
  const [imageFile, setImageFile] = useState(null);
  const [imagePrediction, setImagePrediction] = useState("");

  const generatePreviewImage = (file, callback) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = (e) => callback(reader.result);
  };

  const handleChange = (event) => {
    const file = event.target.files[0];

    if (!file) {
      return;
    }

    setImageFile(file);
    generatePreviewImage(file, (previewImageUrl) => {
      setPreviewImage(previewImageUrl);
      setImagePrediction("");
    });
  };

  const uploadTransformerHandler = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", imageFile, "img_transformer.png");

    let t0 = performance.now();
    axios.post("http://127.0.0.1:5000/upload", formData).then((res, data) => {
      data = res.data;
      setImagePrediction(data);
      let t1 = performance.now();
      console.log(data);
      console.log(
        "The time Transformer model took to predict the image " +
          (t1 - t0) +
          " milliseconds."
      );
    });
  };

  const uploadCRNNHandler = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", imageFile, "img_crnn.png");

    let t0 = performance.now();
    axios.post("http://127.0.0.1:5000/upload", formData).then((res, data) => {
      data = res.data;
      setImagePrediction(data);
      let t1 = performance.now();
      console.log(data);
      console.log(
        "The time LSTM & Attention took to predict the image " +
          (t1 - t0) +
          " milliseconds."
      );
    });
  };

  return (
    <div className="container--feature">
      <div className="container--feature__col container--feature__uploading">
        <p>Upload Your Writting</p>
        {/* Button for choosing an image */}
        <div>
          <input
            type="file"
            name="file"
            onChange={handleChange}
            className="btn"
          />
        </div>

        {/* Button for sending image to backend */}
        <div style={{ margin: "1rem" }}>
          <input
            type="submit"
            onClick={uploadTransformerHandler}
            className="btn"
            value="Transformer"
          />
        </div>
        <div style={{ margin: "1rem" }}>
          <input
            type="submit"
            onClick={uploadCRNNHandler}
            className="btn"
            value="LSTM & Attention"
          />
        </div>

        {/* Field for previewing the chosen image */}
        <div className="container--image">
          {previewImage && (
            <img alt="inputimg" src={previewImage} className="previewImage" />
          )}
        </div>
      </div>
      {/* Text for model prediction */}
      <div className="container--feature__col container--feature__predicted ">
        {imagePrediction && <p>The model predicted: {imagePrediction}</p> && (
          <a href={Result} download="result.txt" className="btn">
            Click to download
          </a>
        )}
      </div>
      <div>
        {imagePrediction && <p>The model predicted: {imagePrediction}</p>}
      </div>
    </div>
  );
};

export default Feature;
