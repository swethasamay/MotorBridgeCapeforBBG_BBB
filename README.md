
Motor bridge cape libraries--> MotorBridge.py located in BBG_MotorBridgeCape folder
To test the Stepper motor --> StepperMotortest.py located in tests folder

First install these dependencies:
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git -y
sudo pip install Adafruit-GPIO
sudo pip install Adafruit_BBIO
sudo pip install pyserial

To upgrade the firmware, execute the following but in order to resolve the IOError: [Errno 121] Remote I/O error, make sure to change the flasher code--> Changed the flasher code to comment the export gpio lines as that has been taken care of in the universal cape line.

git clone https://github.com/Seeed-Studio/MotorBridgeCapeFirmware
cd MotorBridgeCapeFirmware/ && make flash

Also make sure that after running sudo nano /boot/uEnv.txt it has the following 2 lines at bottom of the uEnv.txt.
uboot_overlay_addr0=/lib/firmware/BB-UART2-00A0.dtbo
enable_uboot_cape_universal=1



