# Vietnamese Handwriting Recognition WebApp

We divide our Application into backend for managing user input image and giving out prediction. The other is frowned which represents user interface and receive their input

You can dowload our pretrained [model](https://drive.google.com/drive/folders/1pgSICcELr0HFSaugtsaCfJA-WeRzAQP-?usp=sharing)

You can trained your own model with this [repo](https://github.com/NgTuanLoc/OCR_source_code) 

## Installation

**A/ Go to backend folder and run this command to download package**

```bash
pip3 install -r requirements.txt
```

**B/ Go to frontend folder and run this command to download package**

\*You should have install [Nodejs](https://nodejs.org/en/)

```bash
npm install
```

## Usage

**A/ Activate backend session**

**Go to backend folder to activate by running this command**

```bash
python3 app.py
```

Or this command

```bash
 flask run --without-threads
```

**B/ Activate frontend**
**Go to frontend folder to activate by running this command**

```bash
 npm start
```
