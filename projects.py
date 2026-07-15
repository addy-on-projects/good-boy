import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("hello sir ! how may i help you ")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            # Wake word
            if "good boy" in word.lower():
                speak("on your command sir")
            


                # Take command
                with sr.Microphone() as source:
                    print("Waiting for command...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
            

                # Example commands
                if "open google" in command.lower():
                    webbrowser.open("https://google.com")
                
                elif "roi" in command.lower():
                    webbrowser.open("https://www.youtube.com/watch?v=qhpH6wYJZuQ&list=RDqhpH6wYJZuQ&start_radio=1")

                elif "play piano" in command.lower():
                    webbrowser.open("https://www.youtube.com/watch?v=q9bU12gXUyM&list=RDq9bU12gXUyM&start_radio=1")

                elif "play python tutorial" in command.lower():
                    webbrowser.open("https://www.youtube.com/watch?v=UrsmFxEIp5k&t=13s")

                elif "play haryanvi song" in command.lower():
                    webbrowser.open("https://www.youtube.com/watch?v=_ijaEtNzZgw")

                elif "sleep" in command.lower():
                    speak("Goodbye sir")
                    break

                else:
                    speak("I did not understand")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print(f"Error: {e}")