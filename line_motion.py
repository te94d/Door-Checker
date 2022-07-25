# -- coding: utf-8 --
#Import Files
import RPi.GPIO as GPIO
import picamera
import time
import cv2
import os
import datetime
import time
import numpy as np
import requests,os
 
# os.chdir("./photo") #画像保存先に移動
line_notify_token = 'notifyのトークン'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '誰かな？？'

#GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Camera Settings
CAM_DIR  = "LINE_pic"

#Main
try:
  while True:
    if GPIO.input(25) == 1:
      camera = picamera.PiCamera()
      print("camerad")
      filename = time.strftime("%Y%m%d%H%M%S") + ".jpeg"
      save_dir_filename = CAM_DIR + filename
      camera.capture(save_dir_filename)
      camera.close()
      # motion detection
        #line
      payload = {'message': message}
      headers = {'Authorization': 'Bearer ' + line_notify_token}
      files = {'imageFile': open("LINE_pic"+filename, "rb")} #バイナリファイルを開く
      line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
      time.sleep(60)
    else:
      pass
        
except KeyboardInterrupt:
  GPIO.cleanup()