import pixellib
import image as image
from pixellib.instance import instance_segmentation
import cv2
import numpy as np
import os
from gtts import gTTS
def sample():
    segmentation_model = instance_segmentation(infer_speed="rapid")
    segmentation_model.load_model('mask_rcnn_coco.h5')
    cap = cv2.VideoCapture("mi.mp4")
    video = "mi.mp4"

    while cap.isOpened():
        ret, frame = cap.read()

        # Apply instance segmentation
        res = segmentation_model.segmentFrame(frame, show_bboxes=True)
        image = res[1]

        cv2.imshow('Instance Segmentation', image)
    if video == "mi.mp4":
        fh = open("mi.txt", "r")
        myText = fh.read().replace("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        fh.close()
        # Play the converted file
        os.system("start output.mp3")
    # City.jpg
    if video == "video1.mp4":
        fh = open("video1.txt", "r")
        myText = fh.read().replace("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        fh.close()
        # Play the converted file
        os.system("start output.mp3")
    if video == "video2.mp4":
        fh = open("video2.txt", "r")
        myText = fh.read().replace("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=True)
        output.save("output.mp3")
        fh.close()
        # Play the converted file
        os.system("start output.mp3")
    if video == "video3.mp4":
        fh = open ("video3.txt", "r")
        myText = fh.read ().replace ("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS (text=myText, lang=language, slow=True)
        output.save ("output.mp3")
        fh.close ()
        # Play the converted file
        os.system ("start output.mp3")
    cap.release()
    cv2.destroyAllWindows()
    segmentation_model.segmentFrame
