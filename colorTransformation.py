# Name: colorTransformation.py
# Author: Greyson Wintergerst
# Date created: 6/22/2023
# Last updated: 6/22/2023
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import librosa
import matplotlib.pyplot as plt
import numpy as np
import pretty_midi

# Load the audio file
audio_path = "/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3"
audio_data, sample_rate = librosa.load(audio_path)
print(sample_rate)


'''UNCOMMENT THE LINES BELOW TO ESTIMATE STATIC TEMPO OF AUDIO FILE'''


# onset_env = librosa.onset.onset_strength(y = audio_data, sr = sample_rate)
# tempo = librosa.feature.tempo(onset_envelope=onset_env, sr = sample_rate)
# print(tempo)



# Compute the spectrogram
spectrogram = librosa.stft(audio_data)

plt.plot(spectrogram)

# Convert spectrogram to dB scale
spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

# Get the frequencies corresponding to each bin
frequencies = librosa.core.fft_frequencies(sr=sample_rate, n_fft=spectrogram.shape[0])

# Convert frequencies to notes
# notes = []
# for freq in frequencies:
#     if freq > 0:
#         midi = 69 + 12 * np.log2(freq / 440.0)
#         if not np.isinf(midi):  # Skip infinity values
#             rounded_midi = int(round(midi))
#             note = librosa.midi_to_note(rounded_midi)
#             notes.append(note)

notes = []
# Print the frequency data with corresponding notes
# for i, freq in enumerate(frequencies):
#     if freq > 0:
#         notes.append(librosa.hz_to_note(freq))
#         #print(f"Bin {i}: Frequency {freq} Hz, Note {note}, Amplitude {spectrogram_db[i]} dB")

# for i in range(len(notes)):
#     print(notes[i])


