import matplotlib.pyplot as plt
from PIL import Image

from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

import os
from ocr.segmentation.segmentation import segment
os.environ['KMP_DUPLICATE_LIB_OK']='True'

config = Cfg.load_config_from_name('vgg_transformer')

# config['weights'] = './weights/transformerocr.pth'
config['weights'] = 'https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA'
config['cnn']['pretrained']=False
config['device'] = 'cpu'
config['predictor']['beamsearch']=False

detector = Predictor(config)


def remove_file(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def predict(input_path, output_path):
    print("segmentation", input_path, output_path)
    l = segment(input_path, output_path)
    lines = []
    for i in reversed(range(l)):
        path = './test/img_transformer{0}.jpg'.format(i)
        if os.path.exists(path):    
            img = Image.open(path)
            s = detector.predict(img)
            print(path, s)
            lines.append(s)
    # remove_file('./test')
    return lines

def save_file(path, lines):
    with open(path, 'w') as f:
        for line in reversed(lines): 
            f.write(line)
            f.write('\n')