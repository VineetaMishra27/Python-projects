from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, lang='en'):
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Save the audio file
        audio_file = "output.mp3"
        tts.save(audio_file)
        
        # Play the audio file
        os.system(f"start {audio_file}")  # Use 'afplay' for macOS or 'mpg321' for Linux
        print(f"Audio saved as {audio_file} and is now playing.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    # Input text
    text = input("Enter the text you want to convert to speech: ")
    
    # Call the text to speech function
    text_to_speech(text)