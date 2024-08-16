import os
import sys
import datetime as dt
import speech_recognition as sr
import pyttsx3

# Create a list of numbers as strings
numbers = [str(t) for t in range(11)]

# Create a dictionary mapping numbers as strings to their integer values
numbers_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
numd = {k: int(k) for k in numbers}
numd.update({numbers_strings[i]: i for i in range(len(numbers_strings))})

# Function to speak a given text
def SpeakText(command):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(command)
    engine.runAndWait()

# Function to recognize speech and respond
def SpeakLoop():
    SpeakTime = True
    r = sr.Recognizer()

    try:
        while SpeakTime:
            with sr.Microphone() as source:
                print('START SPEAKING')
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()

                # Speak the recognized text
                SpeakText(MyText)

                # Perform calculation if "calculate" is mentioned in the command
                if "calculate" in MyText:
                    split = MyText.split(" ")
                    print("CALCULATE")
                    print(f"You said: {MyText}")

                    # Extract numbers from the command and calculate their sum
                    calc = [numd[k] for k in split if k in numd.keys()]
                    total = sum(calc)
                    print(f"Total: {total}")

                    # Write the timestamp and calculation result to a file
                    timestamp = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    folder = "MATH"
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                    with open(f"{folder}{os.sep}math.txt", "a") as f:
                        f.write(f"\nTime stamp: {timestamp}")
                        f.write(f"\nTotal: {total}")
                        f.write(f"\n{calc}")
                        f.write("\n")

                # Handle loop termination
                elif "quit" in MyText or "stop" in MyText:
                    print("Goodbye!") 
                    SpeakText("Goodbye!")
                    SpeakTime = False
                    sys.exit()

                # Print the recognized text
                else:
                    print(f"You said: {MyText}")

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except KeyboardInterrupt:
        print("\nProgram terminated manually.")

if __name__ == "__main__":
    SpeakLoop()
