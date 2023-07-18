import math
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.io import wavfile
from tempfile import mktemp
from mutagen.mp3 import MP3
# from tempfile import NamedTemporaryFile
import argparse

class FileLoader:
    def __init__(self, filename):
        self.filename = filename
        # Step 1: Load the MP3 file
        # audio_file = AudioSegment.from_file("/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3", format="mp3")
        # with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        #     tmp_filename = tmp_file.name
        #     audio_file.export(tmp_filename, format="wav")

        audio_file = AudioSegment.from_file(filename, format="mp3")
        wname = mktemp(".wav") # use temp file
        audio_file.export(wname, format="wav")

        # Step 2: Read WAV file
        self.FS, self.data = wavfile.read(wname)

        audio = MP3(filename)

        self.duration = audio.info.length


    
    def getData(self):
        if self.data.ndim > 1:
            self.data = self.data.mean(axis=1)  # Convert stereo to mono by taking the mean of channels
        return self.FS, self.data, self.duration
    


class Spectrogram:
    def __init__(self, FS, data, nfft=None):
        self.FS = FS
        self.data = data
        self.nfft = nfft
        self.spec, self.freqs, self.t, self.im = plt.specgram(self.data, Fs=self.FS, NFFT=self.nfft, noverlap=round(0.75*self.nfft), cmap="rainbow")
    
    def plot(self):
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.title('Spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.show()


    def getMaxFrequency(self, start_time, end_time):
        # Step 3: Define the time frame of interest
        start = start_time  # Start time of the time frame (in seconds)
        end = end_time  # End time of the time frame (in seconds)

        # Step 4: Convert the time frame to spectrogram indices
        start_index = int(start * self.FS / (self.nfft - self.nfft // 2))
        end_index = int(end * self.FS / (self.nfft - self.nfft // 2))

        # Step 5: Extract the relevant portion of the spectrogram
        spec_frame = self.spec[:, start_index:end_index]

        # Step 6: Find the frequency bin with the maximum magnitude
        max_magnitude_index = np.argmax(spec_frame)
        max_magnitude = spec_frame.flatten()[max_magnitude_index]
        max_frequency = self.freqs[max_magnitude_index]
        return [max_magnitude, max_frequency]
    
class Translator:
    def __init__(self):
        self.noteLib = {16.35: 'C0', 17.32: 'C#0', 18.35: 'D0', 20.6: 'E0', 21.83: 'F#0', 24.5: 'G0', 25.96: 'G#0', 
27.5: 'A0', 29.14: 'A#0', 30.87: 'B0', 32.7: 'C1', 34.65: 'C#1', 36.71: 'D1', 38.89: 'D#1', 
41.2: 'E1', 43.65: 'F1', 46.25: 'F#1', 49.0: 'G1', 51.91: 'G#1', 55.0: 'A1', 58.27: 'A#1', 
61.74: 'B1', 65.41: 'C2', 69.3: 'C#2', 73.42: 'D2', 77.78: 'D#2', 82.41: 'E2', 87.31: 'F2', 
92.5: 'F#2', 98.0: 'G2', 103.83: 'G#2', 110.0: 'A2', 116.54: 'A#2', 123.47: 'B2', 130.81: 'C3', 
138.59: 'C#3', 146.83: 'D3', 155.56: 'D#3', 164.81: 'E3', 174.61: 'F3', 185.0: 'F#3', 
196.0: 'G3', 207.65: 'G#3', 220.0: 'A3', 233.08: 'A#3', 246.94: 'B3', 261.63: 'C4', 
277.18: 'C#4/D4', 293.66: 'D4', 311.13: 'D#4', 329.63: 'E4', 349.23: 'F4', 369.99: 'F#4', 
392.0: 'G4', 415.3: 'G#4', 440.0: 'A4', 466.16: 'A#4', 493.88: 'B4', 523.25: 'C5'}
        self.freqList = [16.35, 17.32, 18.35, 20.6, 21.83, 21.83, 24.5, 25.96, 27.5, 29.14, 30.87, 
                         32.7, 34.65, 36.71, 38.89, 41.2, 43.65, 46.25, 49.0, 51.91, 55.0, 58.27, 
                         61.74, 65.41, 69.3, 73.42, 77.78, 82.41, 87.31, 92.5, 98.0, 103.83, 110.0, 
                         116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.0, 196.0, 
                         207.65, 220.0, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 
                         369.99, 392.0, 415.3, 440.0, 466.16, 493.88, 523.25]


    def note(self, target):
        diffList = self.freqList-target
        key = min(diffList, key=abs) + target
        return self.noteLib[key]
    
class Muzart:
    def __init__(self, file = '/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3'):
        self.fileKeeper = FileLoader(filename = file)
        self.noteTranslator = Translator()
        self.FS, self.data, self.duration = self.fileKeeper.getData()
        self.spec = Spectrogram(FS=self.FS, data=self.data, nfft=8192)
        self.rangeArray = np.arange(0,round(self.duration),0.1)
        self.noteList = []
        self.noteTime = []
        # self.noteDuration = []
        self.noteCount = 0
        self.noteTimeCount = 0
        self.noteCountList = []
        self.noteDurationCountList = []
        self.noteTimeCountList = []
        
    def run(self):
        freqInfo = self.spec.getMaxFrequency(self.rangeArray[0],self.rangeArray[1])
        note = self.noteTranslator.note(freqInfo[1])
        prevNote = note
        noteDuration = 0.1
        curDecibel = freqInfo[0]
        curMaxDecibel = curDecibel
        for i in range(2,self.rangeArray.size):
            freqInfo = self.spec.getMaxFrequency(self.rangeArray[i-1],self.rangeArray[i])
            note = self.noteTranslator.note(freqInfo[1])
            if (note[0] == prevNote[0] or abs(freqInfo[0]-curDecibel) < 1000):
                noteDuration += 0.1
                curDecibel = freqInfo[0]
            else:
                self.noteList.append([prevNote,curMaxDecibel,noteDuration])
                curMaxDecibel = freqInfo[0]
                prevNote = note
                noteDuration = 0.1

        self.noteList.append([prevNote,curMaxDecibel,noteDuration])

        return self.noteList


def options():
    parser = argparse.ArgumentParser(description="Read image metadata")
    parser.add_argument("-o", "--first", help="Input audio file.", required=True)
    arg = parser.parse_args()
    return arg

muzart = Muzart(file = '/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3')
print(muzart.run())


# def main():
# arg = options()
# fileKeeper = FileLoader()
# noteTranslator = Translator()

# FS, data, duration = fileKeeper.getData()
# spec = Spectrogram(FS=FS, data=data, nfft=8192)
# spec.plot()
# rangeArray = np.arange(0,round(duration),0.1)
                       
# prevNote = ''
# for i in range(1,rangeArray.size):
#     freqInfo = spec.getMaxFrequency(rangeArray[i-1],rangeArray[i])
#     note = noteTranslator.note(freqInfo)
#     if (note[0] != prevNote):
#         prevNote = note[0]
#     print(note)





    

# # Step 1: Load the MP3 file
# # audio_file = AudioSegment.from_file("/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3", format="mp3")
# # with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
# #     tmp_filename = tmp_file.name
# #     audio_file.export(tmp_filename, format="wav")

# audio_file = AudioSegment.from_file("/vanderbiltCS/SyBBURE/SU23/with-one-hand-demo-song.mp3", format="mp3")
# wname = mktemp(".wav") # use temp file
# audio_file.export(wname, format="wav")

# # Step 2: Read WAV file
# FS, data = wavfile.read(wname)

# if data.ndim > 1:
#     data = data.mean(axis=1)  # Convert stereo to mono by taking the mean of channels


# # Step 3: Display spectrogram

# nfft = 8192
# spec, freqs, t, im = plt.specgram(data, Fs=FS, NFFT=nfft, noverlap=round(0.75*8192), cmap="rainbow")
# plt.xlabel('Time')
# plt.ylabel('Frequency')
# plt.title('Spectrogram')
# plt.colorbar(format='%+2.0f dB')
# plt.show()

# # Step 3: Define the time frame of interest
# start_time = 0  # Start time of the time frame (in seconds)
# end_time = 0.1  # End time of the time frame (in seconds)

# # Step 4: Convert the time frame to spectrogram indices
# start_index = int(start_time * FS / (nfft - nfft // 2))
# end_index = int(end_time * FS / (nfft - nfft // 2))

# # Step 5: Extract the relevant portion of the spectrogram
# spec_frame = spec[:, start_index:end_index]

# # Step 6: Find the frequency bin with the maximum magnitude
# max_magnitude_index = np.argmax(spec_frame)
# max_frequency = freqs[max_magnitude_index]

# # Step 7: Print maximum frequency result
# print("Maximum Frequency in time frame: ", max_frequency,'\n')

# # Step 2: Convert to a numerical representation
# samples = np.array(audio_file)

# # Step 3: Apply Fourier Transform
# spectrum = np.fft.fft(samples)
# frequencies = np.fft.fftfreq(len(samples))

# # Step 4: Define piano note frequencies
# piano_notes = {
#     "C3": 130.81, "C#3/Db3": 138.59, "D3": 146.83, "D#3/Eb3": 155.56, "E3": 164.81,
#     "F3": 174.61, "F#3/Gb3": 185.00, "G3": 196.00, "G#3/Ab3": 207.65, "A3": 220.00,
#     "A#3/Bb3": 233.08, "B3": 246.94, "C4": 261.63, "C#4/Db4": 277.18, "D4": 293.66,
#     "D#4/Eb4": 311.13, "E4": 329.63, "F4": 349.23, "F#4/Gb4": 369.99, "G4": 392.00,
#     "G#4/Ab4": 415.30, "A4": 440.00, "A#4/Bb4": 466.16, "B4": 493.88, "C5": 523.25,
#     # Add more notes as needed...
# }

# # Step 5: Identify piano notes
# threshold = 0.5  # Adjust as per your requirements
# piano_notes_detected = []

# for note, frequency in piano_notes.items():
#     closest_frequency = frequencies[np.abs(frequencies - frequency).argmin()]
#     spectrum_index = np.where(frequencies == closest_frequency)[0][0]
#     if np.abs(spectrum[spectrum_index]) > threshold:
#         piano_notes_detected.append(note)

# print("Detected piano notes:", piano_notes_detected) 