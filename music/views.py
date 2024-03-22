from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render
import cv2
import numpy as np
from keras.models import model_from_json
import tensorflow as tf
# Create your views here.


class Main(TemplateView):
    template_name='home.html'

class Survey(TemplateView):
    template_name='survey.html'


class Result(TemplateView):
    template_name='result.html'




emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

emotion_model = tf.keras.models.load_model('D:\Internship Luminar\Main Projects\Music Recommendation\Emotion_model\emotion_model.h5')

def detect_emotions(request):
    # cap = cv2.VideoCapture(0)

    while True:
        for index in range(4):  # Try first 4 camera indexes
            cap = cv2.VideoCapture(index)
            ret, frame = cap.read()
            if ret:
                # print(f"Camera found at index {index}")
                break
            cap.release()
        print(ret)
        frame = cv2.resize(frame, (1280, 720))
        if not ret:
            break
        face_detector = cv2.CascadeClassifier('D:\Internship Luminar\Main Projects\Music Recommendation\haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in num_faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            emotion_prediction = emotion_model.predict(cropped_img)
            print(emotion_prediction)
            maxindex = int(np.argmax(emotion_prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'emotion_detection.html')


class Emotion(TemplateView):
    template_name='emotion_detection.html'
