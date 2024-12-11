# <ins> ASL Translator Project </ins>
<br>
This project uses a Raspberry Pi and computer vision to recognize American Sign Language (ASL) hand gestures. The default model can detect and translate ASL digits (0-9) into text in real-time using a live camera feed. The system uses a pre-trained TensorFlow model 'keras_model.h5' for classification, and users can optionally train their own model for custom gestures.
<br>
<br>
### <ins> How to use Project </ins>
<br>
* Clone this project into your raspberypi 5 <br>
* Install all necessary package in 'requirements.txt' <br>
* pip install '-r requirement.txt'<br>
* Note: Tensorflow version need to be '2.12.1' to run kesar_model.h5<br>
* pip install 'tensorflow==2.12.1' <br>
<br>
<br>
After install all requirements, run main.py to use the default pre-trained model (only recognize 0-9)<br>
<br>
Or you can train your own model at :<br>
https://teachablemachine.withgoogle.com/train/image by uploading photo for different classes.<br>
Simply replace .h5 file after trainning to use the new model<br>
<br>
