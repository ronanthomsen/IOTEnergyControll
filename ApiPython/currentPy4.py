from flask import Flask, jsonify, request


import time
import serial
import io
import smtplib
import thread
import datetime
import requests
import json
 
app = Flask(__name__)
  
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

def saveDB(value):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('[URL FireBase]', None)
    new_status = value
    result = firebase.post('/status', {'controle': new_status})
    # result = firebase.get('/status', None)
    # print result

def sendPushIos():
    """ Fuction to send a Push Notificarion for Active Users """

    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "Basic [Chave Para API Push OneSignal]"}

    t = datetime.datetime.now()
    dt = t.strftime('%d/%m/%Y | %H:%M')          

    payload = {"app_id": "[ID do App para no OneSignal]",
               "included_segments": ["Active Users"],
               "contents": {"en": "Qeda de energia!!!  "+dt}}

    req = requests.post("https://onesignal.com/api/v1/notifications",
                        headers=header, data=json.dumps(payload))

    print(req.status_code, req.reason)


def verificaCorrente():
    m1 = ""
    while True:
        ser.flushInput()
        global message
        message = ser.readline()
        if m1 != message:
            m1 = message
            saveDB(message)
            print (message)

        ser.flushInput()

        if m1[0] == 'Q':
            # send_email()
            sendPushIos()
            time.sleep(60)

        time.sleep(4.5)


@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    return message



thread.start_new_thread(verificaCorrente, ())





