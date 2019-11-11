
Motor bridge cape libraries--> MotorBridge.py located in BBG_MotorBridgeCape folder
To test the Stepper motor --> StepperMotortest.py located in tests folder

First install these dependencies:
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git -y
sudo pip install Adafruit-GPIO
sudo pip install Adafruit_BBIO
sudo pip install pyserial

Changed the flasher code--> commented the export gpio lines as that has been taken care of in the universal cape line.
