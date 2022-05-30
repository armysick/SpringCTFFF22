import multiprocessing
import random
import threading
import time

FLAG = "Flag{XD}"
TIMEOUT = 60

def quenoqueout(localPort, counter, PIN):
  print(localPort)
  import socket
  import time


  localIP     = "0.0.0.0"
  bufferSize  = 1024

  # Create a datagram socket

  UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  # Bind to address and ip

  UDPServerSocket.bind((localIP, localPort))
  #print("UDP server listening on port {}".format(localPort))


  def receivepkt():

      bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
      message = bytesAddressPair[0]

      address = bytesAddressPair[1]

      clientMsg = "Message from Client:{}".format(message)

      print(clientMsg)


      if PIN not in clientMsg:
        bytesToSend = str.encode("WRONG PIN!")
      # Sending a reply to client
      elif counter == 3:
        bytesToSend = str.encode(FLAG)
      else:
        portn = random.randint(22223,33333)
        NEWPIN = str(random.randint(1000,9999))
        bytesToSend = str.encode("Opened port {} - Hurry you got {} seconds!. Use this PIN - {}".format(portn,str(TIMEOUT),NEWPIN))
        x = multiprocessing.Process(target=quenoqueout, args=(portn,counter+1,NEWPIN))
        x.start()

        y = multiprocessing.Process(target=KILLER, args=(x,TIMEOUT))
        y.start()

      UDPServerSocket.sendto(bytesToSend, address)


  while True:
    aa = receivepkt()


  print('HELLO')



def KILLER(thr,tmp):
  time.sleep(tmp)
  thr.terminate()



mainsocket = multiprocessing.Process(target=quenoqueout, args=(22222,1,"0000"))
mainsocket.start()

