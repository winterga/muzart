import numpy as np
from pydub import AudioSegment

# Step 1: Load the MP3 file
audio_file = AudioSegment.from_file("/vanderbiltCS/SyBBURE/SU23/piano_middle_C.mp3", format="mp3")

# Step 2: Convert to a numerical representation
samples = np.array(audio_file)

# Step 3: Apply Fourier Transform
spectrum = np.fft.fft(samples)
frequencies = np.fft.fftfreq(len(samples))

# Step 4: Define piano note frequencies
piano_notes = {
    "C3": 130.81, "C#3/Db3": 138.59, "D3": 146.83, "D#3/Eb3": 155.56, "E3": 164.81,
    "F3": 174.61, "F#3/Gb3": 185.00, "G3": 196.00, "G#3/Ab3": 207.65, "A3": 220.00,
    "A#3/Bb3": 233.08, "B3": 246.94, "C4": 261.63, "C#4/Db4": 277.18, "D4": 293.66,
    "D#4/Eb4": 311.13, "E4": 329.63, "F4": 349.23, "F#4/Gb4": 369.99, "G4": 392.00,
    "G#4/Ab4": 415.30, "A4": 440.00, "A#4/Bb4": 466.16, "B4": 493.88, "C5": 523.25,
    # Add more notes as needed...
}

# Step 5: Identify piano notes
threshold = 0.5  # Adjust as per your requirements
piano_notes_detected = []

for note, frequency in piano_notes.items():
    closest_frequency = frequencies[np.abs(frequencies - frequency).argmin()]
    spectrum_index = np.where(frequencies == closest_frequency)[0][0]
    if np.abs(spectrum[spectrum_index]) > threshold:
        piano_notes_detected.append(note)

print("Detected piano notes:", piano_notes_detected)