import parselmouth

def get_pitch(file_path):
    sound = parselmouth.Sound(file_path)
    pitch = sound.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    return pitch_values.mean()

def determine_gender(pitch):
    if pitch > 165:
        return "female"
    else:
        return "male"

# Example usage
file_path = "path/to/audio/file.wav"
pitch = get_pitch(file_path)
gender = determine_gender(pitch)
print("The voice in the audio file is likely a", gender)
