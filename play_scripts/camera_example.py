import picamera
from time import sleep
 
 camera = picamera.PiCamera()
  
  camera.capture('image1.jpg')
  sleep(5)
  camera.capture('image2.jpg')
   
   camera.start_recording('video.h264')
   sleep(5)
   camera.stop_recording()
