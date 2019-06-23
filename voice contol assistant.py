import speech_recognition as sr
import webbrowser

sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512)

r=sr.Recognizer()

r.energy_threshold = 5000

with sr.Microphone() as source:
    print("Speak!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You Said:" .format(text))
        url = 'https://www.google.com/search?q='
        search_url = url + text
        webbrowser.open(search_url)

    except:
        print("Can't Recognize")
