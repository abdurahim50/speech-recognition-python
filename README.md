# Building a Simple Speech Recognition Tool in Python

Have you ever wanted to build your own voice-controlled applications? Thanks to Python and powerful libraries, it’s easier than you think. In this tutorial, I’ll walk you through building a simple speech recognition tool using Python. By the end of this project, you’ll have a script that listens to your voice and converts it into text, and even opens applications like Notepad, Chrome, and WhatsApp based on your commands.

---

## Overview

In this project, we’ll use Python’s speech_recognition library to:

- Capture audio input from a microphone.
- Process the audio and convert it into text using the Google Web Speech API.
- Open applications like Notepad, Chrome, and WhatsApp based on voice commands.
- Handle common errors like timeouts or unrecognizable speech.

---

## Prerequisites

### 1. Python Installation
Make sure Python (version 3.7 or above) is installed on your machine. You can check this by running:
```
python --version
```
### 2. Install Required Libraries
We’ll use two libraries: speech_recognition and pyaudio. To install them, run the following commands:

```
pip install SpeechRecognition
pip install pyaudio
```

## Step 1: Writing the Code
Here’s the complete code for our speech recognition tool:

```
import os
import speech_recognition as sr

# Display options for the user
print("\t\t\t\tWelcome to my Automation Tool")
print("\t\t\t\t-----------------------------")
print("Option 1: Open Notepad")
print("Option 2: Open Chrome")
print("Option 3: Open WhatsApp")
print()

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
        choice = myAI.recognize_google(audio_data).lower()
        print(f"You said: {choice}")

        # Logic to open applications based on the voice command
        if (not ("don't" in choice)) and (("notepad" in choice) or ("editor" in choice)):
            os.system("notepad")
        elif "chrome" in choice:
            os.system("start chrome")  # For Windows, 'start' is used to open apps
        elif "whatsapp" in choice:
            print("Opening WhatsApp...")
            # Add the code to open WhatsApp here if needed (such as via WhatsApp Web)
        else:
            print("Sorry, I didn't understand that. Please try again.")
    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

```
## How It Works
1. `speech_recognition.Recognizer`: The `Recognizer` class processes audio and converts it into text.
2. `sr.Microphone`: Captures live audio from your microphone.
3. **Error Handling:**
  - **Timeouts** if no speech is detected within 10 seconds.
  - Handles unintelligible speech that the API can’t process.
  - **API Request Errors** caused by network issues or service unavailability.
  
## Step 2: Running the Script
Save the script as `speech_recognition.py`.
Run it using:
```
python speech_recognition.py
```
#### Expected Output
When you speak into the microphone, the script will transcribe your speech into text. For example:

```
Speak please...
Stopped Recording
You said: Hello world, this is a test!
```
If no speech is detected:
```
No speech detected within the timeout period.
```
## Step 3: Troubleshooting Common Issues

1. #### Microphone Not Detected
- Ensure your microphone is connected and enabled.
- On Windows or macOS, check system settings to verify the default input device.
  
2. #### Installation Errors
- If pyaudio fails to install, try:
  
```
sudo apt-get install portaudio19-dev
pip install pyaudio
```
For macOS:
```
brew install portaudio
pip install pyaudio
```
3. #### Speech Not Recognized
- Background noise or unclear speech can affect accuracy. Ensure a quiet environment and speak clearly into the microphone.

## Step 4: Enhancing the Project
Take this project further by:

1. **Adding a GUI**: Use libraries like `Tkinter` or `PyQt` to create a graphical interface.
2. **Integrating with Other APIs**: Use the recognized text as input for chatbots, search engines, or home automation systems.
3. **Supporting Multiple Languages:** Pass a language code (e.g., `language='es-ES' for Spanish`) to recognize_google.

## Conclusion
Congratulations! You’ve built a simple yet powerful speech recognition tool in Python. Whether you’re a beginner exploring AI or an experienced developer, this project is a great foundation for voice-enabled applications.

If you found this tutorial helpful, don’t forget to clap, comment, and share. Let me know how you plan to use this tool in your projects!

### Resources:

- [SpeechRecognition Documentation](https://pypi.org/project/SpeechRecognition/)
- [Google Web Speech API Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)











