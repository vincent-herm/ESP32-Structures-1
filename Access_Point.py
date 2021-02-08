import _thread
from machine import Pin
import time  
led1 = Pin(2, Pin.OUT) # 2
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(23, Pin.OUT)
try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Acces-Point-ESP32'
password = '123123'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
#ap.config(essid=ssid,authmode=network.AUTH_WPA_WPA2_PSK, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

#def web_page():
#  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
#  <body><h1>ESP 32 ENIM Access Point !</h1></body></html>"""
#  return html

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>ESP 32 ENIM Access Point !</h1>
  <p>
  <a href=\"?led1=on\"><button1>LED1 ON</button1></a>&nbsp;
  <a href=\"?led1=off\"><button1>LED1 OFF</button1></a>
  </p><p>
  <a href=\"?led2=on\"><button2>LED2 ON</button2></a>&nbsp;
  <a href=\"?led2=off\"><button2>LED2 OFF</button2></a>
  </p><p>
  <a href=\"?led3=on\"><button3>LED13 ON</button3></a>&nbsp;
  <a href=\"?led3=off\"><button3>LED3 OFF</button3></a>
  </p><p>
  <a href=\"?led4=on\"><button4>LED4 ON</button4></a>&nbsp;
  <a href=\"?led4=off\"><button4>LED4 OFF</button4></a>
  </p>
  </body></html>"""
  return html

#def web_page():
#  if led1.value() == 1:
#    led1_state = 'checked'
#  else:
#    led1_state = ""
#  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
#  body{max-width: 300px; margin: 0px auto;}
#  .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:LED1}
#  .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:LED2}
#  .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
#  .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
#  input:checked+.slider{background-color:#2196F3}
#  input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
#  </style><script>function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); if(element.checked){ xhr.open("GET", "/?led1=on", true); }
#  else { xhr.open("GET", "/?led1=off", true); } xhr.send(); }</script></head><body>
#  <h1>ESP ENIM ACCESS POINT !</h1><label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" %s><span class="slider">
#  </span></label></body></html>""" % (led1_state)
#  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#while True:
#  conn, addr = s.accept()
#  print('Got a connection from %s' % str(addr))
#  request = conn.recv(1024)
#  print('Content = %s' % str(request))
#  response = web_page()+'<h1>Connecte a : <br>Adresse IP, numero de port : <br>' + str(addr)+'</h1>'
#  conn.send('HTTP/1.1 200 OK\n')
#  conn.send('Content-Type: text/html\n')
#  conn.send('Connnection: close\n\n')
#  conn.send(response)
#  conn.close()
allumage = 0
start = time.ticks_ms()

def serveur():
    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      print('Content = %s' % request)
      led1_on = request.find('/?led1=on')
      led1_off = request.find('/?led1=off')
      led2_on = request.find('/?led2=on')
      led2_off = request.find('/?led2=off')
      led3_on = request.find('/?led3=on')
      led3_off = request.find('/?led3=off')
      led4_on = request.find('/?led4=on')
      led4_off = request.find('/?led4=off')
      
      if led1_on == 6:
        print('LED1 ON')
        led1.value(1)
        
      if led1_off == 6:
        print('LED1 OFF')
        led1.value(0)
        
      if led2_on == 6:
        print('LED2 ON')
        led2.value(1)

      if led2_off == 6:
        print('LED2 OFF')
        led2.value(0)
      
      if led3_on == 6:
        print('LED3 ON')
        led3.value(1)
        
      if led3_off == 6:
        print('LED3 OFF')
        led3.value(0)
        
      if led4_on == 6:
        print('LED4 ON')
        led4.value(1)

      if led4_off == 6:
        print('LED4 OFF')
        led4.value(0)
      
      response = web_page()
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
  
def temps():
  while True:
    print("Temps écoulé : ",time.ticks_ms() - start)
    time.sleep(1.990)
    
_thread.start_new_thread(serveur, ())
_thread.start_new_thread(temps, ())