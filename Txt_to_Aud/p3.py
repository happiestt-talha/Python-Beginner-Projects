import pyttsx3 as ppy
engine = ppy.init()
voices = engine.getProperty('voices')  # getting details of current voice
# changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

engine.say("Hello boss, kesy Ho")
engine.runAndWait()

engine.say("Sab theeek hai naa?")
engine.runAndWait()

str = {"Soft moonlight filters through dusty windows, casting a mysterious glow on rows of neglected books. EMMA, an adventurous young archaeologist with a passion for ancient artifacts, cautiously explores the silent space. Suddenly, she hears a faint, haunting melody."}
engine.save_to_file(str, "D:\\speech.mp3")
engine.runAndWait()

# engine.
