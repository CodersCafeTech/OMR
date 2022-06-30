#!/usr/bin/env python

import imp
import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

import pyfiglet
from termcolor import colored
from random import randint, random

runner = None
# if you don't want to see a camera preview, set this to False
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = True

def now():
    return round(time.time() * 1000)

def get_webcams():
    port_ids = []
    for port in range(1):
        #print("Looking for a camera in port %s:" %port)
        camera = cv2.VideoCapture(port)
        if camera.isOpened():
            ret = camera.read()[0]
            if ret:
                backendName =camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                #print("Camera %s (%s x %s) found in port %s " %(backendName,h,w, port))
                port_ids.append(port)
            camera.release()
    return port_ids

def sigint_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def help():
    print('python classify.py <path_to_model.eim> <Camera port ID, only required when more than 1 camera is present>')

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

    if len(args) == 0:
        help()
        sys.exit(2)

    model = args[0]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    os.system('clear')
    answer_key=[]

    valid_color = ['red', 'green', 'yellow', 'blue', 'cyan', 'white']
    random_choice = randint[0,6]
    color = valid_color[random_choice]  
    result = pyfiglet.figlet_format("F - OMR", )
    colored_result = colored(result, color)
    print(colored_result)

    while True:
        if (answer_key==[]):
            with ImageImpulseRunner(modelfile) as runner:
                    model_info = runner.init()
                    labels = model_info['model_parameters']['labels']
                    if len(args)>= 2:
                        videoCaptureDeviceId = int(args[1])
                    else:
                        port_ids = get_webcams()
                        if len(port_ids) == 0:
                            raise Exception('Cannot find any webcams')
                        if len(args)<= 1 and len(port_ids)> 1:
                            #raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use to this script")
                            print()
                        videoCaptureDeviceId = int(port_ids[0])

                    camera = cv2.VideoCapture(videoCaptureDeviceId)
                    ret = camera.read()[0]
                    if ret:
                        backendName = camera.getBackendName()
                        w = camera.get(3)
                        h = camera.get(4)
                        camera.release()
                    else:
                        raise Exception("Couldn't initialize selected camera.")

                    next_frame = 0 # limit to ~10 fps here

                    for res, img in runner.classifier(videoCaptureDeviceId):
                        if (next_frame > now()):
                            time.sleep((next_frame - now()) / 1000)

                        y = input("Place your answerkey in position and press 'Y' : ")
                        if (y=="Y"):
                            if "bounding_boxes" in res["result"].keys():
                                #print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                                for bb in res["result"]["bounding_boxes"]:
                                    #print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                                    img = cv2.rectangle(img, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
                                    answer_key.append([bb['x'],bb['y']])
                                print(answer_key)
                                y = input("Is answerkey correct? Y/N : ")
                                if(y=="Y"):
                                    break
                                else:
                                    answer_key = []
                                    break
                        #next_frame = now() + 100
        else:
            with ImageImpulseRunner(modelfile) as runner:
                y = input("Place your answersheet in position and press 'Y' : ")
                if (y=="Y"):
                    model_info = runner.init()
                    labels = model_info['model_parameters']['labels']
                    if len(args)>= 2:
                        videoCaptureDeviceId = int(args[1])
                    else:
                        port_ids = get_webcams()
                        if len(port_ids) == 0:
                            raise Exception('Cannot find any webcams')
                        if len(args)<= 1 and len(port_ids)> 1:
                            #raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use to this script")
                            print()
                        videoCaptureDeviceId = int(port_ids[0])

                    camera = cv2.VideoCapture(videoCaptureDeviceId)
                    ret = camera.read()[0]
                    if ret:
                        backendName = camera.getBackendName()
                        w = camera.get(3)
                        h = camera.get(4)
                        camera.release()
                    else:
                        raise Exception("Couldn't initialize selected camera.")

                    next_frame = 0 # limit to ~10 fps here

                    for res, img in runner.classifier(videoCaptureDeviceId):
                        if (next_frame > now()):
                            time.sleep((next_frame - now()) / 1000)

                        point = 0
                        if "bounding_boxes" in res["result"].keys():
                                for bb in res["result"]["bounding_boxes"]:
                                    if ([bb['x'],bb['y']] in answer_key):
                                        print([bb['x'],bb['y']])
                                        point = point + 1
                        print("Marks:", point)
                        break


if __name__ == "__main__":
   main(sys.argv[1:])