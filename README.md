# Door-checker
raspberry piとlineを使用してドアを監視するシステム的やつ  
- 鍵の状態を外出先からでもlineを通して知ることが出来る。
- ドアが開いた際にその人を撮影しlineで通知する。
ターミナルからline_motion.pyとline_picture.pyを同時に実行することで任意のタイミングとセンサが反応したタイミングで撮影した画像をlineで送信することが出来る。
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
