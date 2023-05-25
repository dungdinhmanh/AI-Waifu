import speech_recognition, pyaudio
import pyttsx3, os
from datetime import date, datetime
micro=speech_recognition.Recognizer()
spk=pyttsx3.init()
ai=""
date=date.today()
time=datetime.now()
while True:
    with speech_recognition.Microphone() as mic:
        print("Haru: Tôi đang nghe")
        audio=micro.listen(mic)
    print('Haru: ...')
    try:
        user=micro.recognize_google(audio,language="vi-VI")
    except:
        user=''
    print('You: '+user)

    if user=='':
        ai="Tôi không thể nghe thấy bạn nói, hãy thử lại"
    elif 'hello' in user:
        ai='Hello, User'
    elif 'today' in user:
        ai=('Hôm nay là '+ date.strftime("ngày %d tháng %m năm %Y"))
    elif 'time' in user:
        ai=('Current time is: '+ time.strftime("%H giờ %M phút %S giây"))
    elif 'bye' in user:
        ai='Goodbye, User.'
        print(ai)
        spk.say(ai)
        spk.runAndWait()
        break
    else:
        ai="Tôi không hiểu yêu cầu của bạn, hãy thử lại!"
    print(ai)

    spk.say(ai)
    spk.runAndWait()