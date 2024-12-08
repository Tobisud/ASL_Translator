Clone this project into your raspberypi 5 <br>
Install all necessary package in requirements.txt <br>
pip install -r requirement.txt<br>
Note: Tensorflow version need to be 2.12.1 to run kesar_model.h5<br>
pip install tensorflow==2.12.1 <br>
<br>
<br>
After install all requirements, run main.py to use the default pre-trained model (only recognize 0-9)<br>
<br>
Or you can train your own model at :<br>
https://teachablemachine.withgoogle.com/train/image by uploading photo for different classes.<br>
Simply replace .h5 file after trainning to use the new model<br>
<br>
