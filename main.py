import speech_recognition as sr
import pyttsx3
import datetime
import cv2

audio = sr.Recognizer()
maquina = pyttsx3.init()

video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def identifica_face():
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if len(faces) != 0:
            break

    cv2.destroyAllWindows()
    return True

def ouvindo():
    voz = audio.listen(source)        
    comando = audio.recognize_google(voz, language='pt')
    comando = comando.lower()
    print(comando)
    return comando



with sr.Microphone() as source:
                while True:
                    face = identifica_face()

                    if face == True:
                        maquina.say('Olá, como posso ajuda-lo?')
                        maquina.runAndWait()
                        comando = ouvindo()
                        