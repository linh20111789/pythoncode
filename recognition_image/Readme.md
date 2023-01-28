
#Requiste Libraries:

pip install requests
pip install opencv-contrib-python
pip install scikit-learn
 
#Steps to Proceed:

 
Run the program 
 

 
#Face Recognition Steps: 
 
Embedding data to a dictionary and then serialize the data  in a pickle file with available Datasets
 
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7
 
Train Using  Linear Support Vector Machine model on top of embeddings
 
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle
 
Test input images to detect faces:
 
python recognize.py --image images/messi.jpg
python recognize.py --image images/BanNinh_0001.bmp
python recognize.py --image images/BanThanh_0001.bmp
python recognize.py --image images/ChiTai1.jpg
python recognize.py --image images/CongLy1.jpg
python recognize.py --image images/ThayDuc_0030.bmp
python recognize.py --image images/XuanBac10.jpg
python recognize.py --image images/TuLong7.jpg

