# Raspberry-Pi
lineと連携させて撮影した画像を送信するやつ
## つかったもの
- raspberry pi 3  
- pi camera  
- PIRモーションセンサ  
- python3  
- ngrok  
- line messaging  
- line notify  

## 全体の仕様的な
### line_picture.py
line messagingに**check**か**watch**を送信するとline notifyからpi cameraで撮影したものが送られる。
### line_motion.py
PIRモーションセンサで検知されるとline notifyからpi cameraで撮影されたものが送られる。
