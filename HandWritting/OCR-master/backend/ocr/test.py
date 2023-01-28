from ocr.crnn.predict import predict

def predict_crnn():
    return predict('model', datapath='data/', output='ocr/crnn/predict/predict.json')
