import boto3
import os
from tkinter import Tk, filedialog

polly_client = boto3.client('polly', region_name='us-west-2')

voices = ["Joanna", "Matthew", "Ivy", "Justin", "Kendra", "Kimberly", 
          "Salli", "Joey", "Brian", "Amy", "Emma", "Nicole", "Russell"]

def text_to_speech():
    print("Available Voices:")
    for i, voice in enumerate(voices, start=1):
        print(f"{i}: {voice}")
    
    while True:
        try:
            choice = int(input("Select a voice by entering its number: "))
            if 1 <= choice <= len(voices):
                selected_voice = voices[choice - 1]
                break
            else:
                print(f"Please select a number between 1 and {len(voices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    text = input("Enter the text you want to convert to speech: ").strip()
    if not text:
        print("No text entered. Exiting.")
        return

    Tk().withdraw()
    directory = filedialog.askdirectory(title="Select Directory to Save Audio")
    if not directory:
        print("No directory selected. Exiting.")
        return

    output_file = os.path.join(directory, "output.mp3")
    print(f"Saving audio to: {output_file}")

    try:
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=selected_voice
        )
        with open(output_file, "wb") as file:
            file.write(response["AudioStream"].read())
        print(f"Audio saved successfully at: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    text_to_speech()
