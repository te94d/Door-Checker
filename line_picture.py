# -- coding: utf-8 --
import requests
import cv2
import time
import picamera
import datetime
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

channel_secret = "シークレットトークン"
channel_access_token = "アクセストークン"


line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():    
  signature = request.headers['X-Line-Signature']     
  body = request.get_data(as_text=True)        
  app.logger.info("Request body: " + body)     
  try:         
    handler.handle(body, signature)     
  except InvalidSignatureError:         
    abort(400)
  return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  print("event")
  messe = event.message.text

  if messe == "check" or messe == "watch":
    line_bot_api.reply_message(
      event.reply_token,
			TextSendMessage("OK"))

    name = "LINE_pic/raspic" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".jpg"

    #capture = cv2.VideoCapture(0)

    with picamera.PiCamera() as camera:
      camera.resolution = (1024, 768)
      camera.start_preview()
			# Camera warm-up time
      time.sleep(2)
      #capture=
      camera.capture(name)
      fname=name
      image=cv2.imread(name)
      camera.close()
      #ret=cv2.imread(name)
      #ret, image = capture.read()
				
      #if ret == True:
        #cv2.imwrite(name, image)
    token = 'notifyのトークン'
    url = 'https://notify-api.line.me/api/notify'
    ms_data="watching door"
         
    send_data = {'message': ms_data}
    headers = {'Authorization': 'Bearer ' + token}
    files = {'imageFile': open(name, 'rb')}
        
    res = requests.post(url,data=send_data,headers=headers,files=files)
    print(res)

  else:
    line_bot_api.reply_message(event.reply_token,TextSendMessage('"check or watch'))

if __name__ == "__main__":
  arg_parser = ArgumentParser(usage='Usage: python ' + __file__ + ' [--port ] [--help]')
  arg_parser.add_argument('-p', '--port', default=8080, help='port')
  arg_parser.add_argument('-d', '--debug', default=False, help='debug')
  options = arg_parser.parse_args()

  app.run(debug=options.debug, port=options.port)