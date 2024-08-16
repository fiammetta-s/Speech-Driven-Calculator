# Speech-Driven Calculator

## Project Overview

This project is a simple speech-driven calculator application built using Python. It utilizes the `speech_recognition` library for capturing and recognizing speech, and `pyttsx3` for text-to-speech functionality. The application performs basic arithmetic calculations based on spoken commands and logs the results to a file.

## Features

- **Speech Recognition**: Utilizes the Google Web Speech API to recognize spoken commands.
- **Text-to-Speech**: Converts text responses into speech using `pyttsx3`.
- **Simple Arithmetic Calculation**: Computes the sum of numbers spoken in a command.
- **Logging**: Records calculation results and timestamps in a text file.
- **Folder Creation**: Automatically creates a directory for storing results if it does not exist.

## Installation

Ensure you have the required libraries installed. Use `pip` to install them:

```bash
pip install SpeechRecognition pyttsx3
```

Additionally, install `pyaudio` for microphone access:

```bash
pip install pyaudio
```

## Usage

1. **Run the Application**:

    ```bash
    python main.py
    ```

2. **Interacting with the Application**:
   
   - **Speak a Command**:
     - You can say commands like "calculate one plus two" or "calculate five six".
     - The application will recognize the numbers and compute the sum.
     - To exit, say "quit" or "stop".

3. **Viewing Results**:
   - Calculation results are saved in the `MATH` directory in a file named `math.txt`.
   - Each entry includes a timestamp and the result of the calculation.

## Code Overview

- **`SpeakText(command)`**:
  - Initializes the text-to-speech engine and speaks the given command.
  
- **`SpeakLoop()`**:
  - Captures and recognizes speech input from the microphone.
  - Processes commands to perform calculations.
  - Logs results to a file in the `MATH` directory.
  - Handles termination commands and exits gracefully.

## File Structure

- `main.py`: Main script that integrates speech recognition, text-to-speech, and arithmetic calculations.
- `MATH/`: Directory created by the application to store calculation results.

## Contribution

Contributions are welcome! If you have improvements or fixes, please fork the repository and submit a pull request.
