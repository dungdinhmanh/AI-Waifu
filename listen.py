import speech_recognition
micro=speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Haru: I'm listening")
    audio=micro.listen(mic)
try:
    user=micro.recognize_google(audio)
except:
    user=''
print('You: '+user)