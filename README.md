# Setup MQTT broker server on Raspberry Pi
1. Update raspberry pi

	> sudo apt update

3. Install mosquitto broker and client

	> sudo apt install mosquitto mosquitto-clients

5. Set mosquitto broker server to auto start after reboot.

	> sudo systemctl enable mosquitto.service


# Setup ESP8266 as MQTT client (with Micro Python)
1. Upgarding the pip
	
	> python -m pip install --upgrade pip
	
2. Installing esptool and adafruit-ampy

	> pip install esptool
	
	> pip install adafruit-ampy
	
3. Downloding the latest MicroPython firmware (.bin file) from https://micropython.org/download/esp8266

4. Connect the ESP8266 device to computer and check the port (COM3 - for windows)

5. Open command prompt and using esptool.py erase the exiting firmware from flash memory of esp8266.

	> esptool.py --port COM3 erase_flash
	
6. write the downloaded firmware to esp8266

	> esptool.py --port COM3 write_flash flash_size=detect 0 D:\ESP8266\esp8266-20210902-v1.17.bin
	
7. Use ampy to check the file system or transfer new python file to esp8266
	
	> **ampy -p COM3 ls -l** ---->  To list down all the existing files from esp8266
	
	> **ampy -p COM3 get [SOURCE_FILE_NAME] [DESTINATION_FILE_NAME]** ---> Copy file from esp8266 to local machine
	
	> **ampy -p COM3 put [FILE_NAME_WITH_PATH]** ----> copy file to esp8266
	
