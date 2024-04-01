import pyttsx3 as ppy
eng = ppy.init()
li = ['talha', 'ahmad', 'bilal']

# print(eng.getProperty('rate'))
eng.setProperty('rate', 150)
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)

for i in li:
    eng.say(f'Welcome {i}')

eng.save_to_file('Hello World', 'D://test.mp3')
eng.runAndWait()
