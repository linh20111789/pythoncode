import os
# import tensorflow as tf 
from ocr.crnn.crnn import get_model
from ocr.crnn.loader import SIZE, MAX_LEN, TextImageGenerator, beamsearch, decode_batch
# from keras import backend as K
import glob                                                                 
import argparse
import tensorflow.compat.v1 as tf
import tensorflow.compat.v1.keras.backend as K
import json
import numpy as np

def loadmodel(weight_path):
    model = get_model((*SIZE, 3), training=False, finetune=0)
    model.load_weights(weight_path)
    return model

def predict(model, datapath, output, verbose=15):
    # K.clear_section()
    sess = tf.Session()
    K.set_session(sess)

    batch_size = 3
    models = glob.glob('{}/best_*.h5'.format(model))
    test_generator  = TextImageGenerator(datapath, None, *SIZE, batch_size, 32, None, False, MAX_LEN)
    test_generator.build_data()
    
    y_preds = []
    for weight_path in models:
        
        print('load {}'.format(weight_path))
        model = loadmodel(weight_path)
        X_test = test_generator.imgs.transpose((0, 2, 1, 3))
        y_pred = model.predict(X_test, batch_size=2)
        y_preds.append(y_pred)
        # for printing        
        decoded_res = beamsearch(sess, y_pred[:verbose])
        for i in range(len(decoded_res)):
            if decoded_res[i] != None:
                print('{}: {}'.format(test_generator.img_dir[i], decoded_res[i]))


    y_preds = np.prod(y_preds, axis=0)**(1.0/len(y_preds))
    y_texts = beamsearch(sess, y_preds)
    submit = dict(zip(test_generator.img_dir, y_texts))
    # with open(output, 'w', encoding='utf-8') as jsonfile:
    #     json.dump(submit, jsonfile, indent=2, ensure_ascii=False)
    return y_texts

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default='model', type=str)
    parser.add_argument('--data', default='test/', type=str)
    parser.add_argument('--output', default='predict/predict.json', type=str)
    parser.add_argument('--device', default=2, type=int)
    args = parser.parse_args()
    
    
    os.environ["CUDA_VISIBLE_DEVICES"]=str(args.device)

    predict(args.model, args.data, args.output)

