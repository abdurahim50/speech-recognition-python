import speech_recognition as sr

# Initialize the Recognizer
myAI = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as mysource:
    print("Speak please...")
    try:
        # Listen for speech with a timeout of 10 seconds
        audio_data = myAI.listen(mysource, timeout=10)
        print("Stopped Recording")
        
        # Recognize speech using Google's Web Speech API
        data = myAI.recognize_google(audio_data)
        print("You said:", data)
    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
