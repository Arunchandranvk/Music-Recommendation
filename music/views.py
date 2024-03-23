from typing import Any
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


from .models import Emotion

from django.shortcuts import render
from .models import Emotion,Music  # Import the Emotion model

def emotion_detection(request):
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    # Load the emotion detection model
    emotion_model = tf.keras.models.load_model(r'D:/Internship Luminar/Main Projects/Music Recommendation/Emotion_model/emotion_model.h5')

    # Capture video
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    emotion_label = "Unknown"  # Default value if no emotion detected

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:  # Check for empty frames
            break
        frame = cv2.resize(frame, (1280, 720))

        face_detector = cv2.CascadeClassifier(r'D:/Internship Luminar/Main Projects/Music Recommendation/haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in num_faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            emotion_prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(emotion_prediction))
            emotion_label = emotion_dict.get(maxindex, "Unknown")
            # Emotion.objects.create(name=emotion_label)  # Save detected emotion to database
            p=Music.objects.filter(type=emotion_label)
            print(p)
            print(emotion_label)
            cv2.putText(frame, emotion_label, (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return render(request, 'emotion_detection.html', {'emotion_label': emotion_label,'data':p})



class Emotion(TemplateView):
    template_name='emotion_detection.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data']=Music.objects.all()
        return context
