from datetime import datetime
import speech_recognition as sr
import   pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#speech engine intialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 = male, 1 = female
activationWord = 'computer' #single word


def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)


    try:
        print('Recognizing speech..')
        query = listener.recognize_google(input_speech, language='en-gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

# Main Loop

if __name__ == '__main__':
    speak('ALl systems nominal.')

    while True:
        # Parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # List commandss
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings,all.')
                else:
                    query.pop(0)# Remove say
                    speech = ''.join(query)
                    speak(speech)
