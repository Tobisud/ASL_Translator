Clone this project into your raspberypi 5 <br>
Install all necessary package in requirements.txt 
pip install -r requirement.txt
Note: Tensorflow version need to be 2.12.1 to run kesar_model.h5
pip install tensorflow==2.12.1 


After install all requirements, run main.py to use the default pre-trained model (only recognize 0-9)

Or you can train your own model at :
https://teachablemachine.withgoogle.com/train/image by uploading photo for different classes.
Simply replace .h5 file after trainning to use the new model
