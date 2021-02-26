import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.say("Привет") #say hello
engine.say('Говори') #say say
engine.runAndWait()


def command():
	r = sr.Recognizer()

	with sr.Microphone() as source: #use defolt Mic() 
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	try: 
		direct = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + direct)

	except sr.UnknownValueError:
		direct = command()

	return direct


def act(direct):
    
    if '<your phrase>' == direct:
        engine.say("<answer>")
        engine.runAndWait()
    
act(command())

