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
        self.noteLib = {
            8.18: 'C0', 8.66: 'C#0', 9.18: 'D0', 10.30: 'E0', 10.91: 'F#0', 12.25: 'G0', 12.98: 'G#0',
            13.75: 'A0', 14.57: 'A#0', 15.43: 'B0', 16.35: 'C1', 17.32: 'C#1', 18.35: 'D1', 19.45: 'D#1',
            20.60: 'E1', 21.83: 'F1', 23.12: 'F#1', 24.50: 'G1', 25.96: 'G#1', 27.50: 'A1', 29.14: 'A#1',
            30.87: 'B1', 32.70: 'C2', 34.65: 'C#2', 36.71: 'D2', 38.89: 'D#2', 41.20: 'E2', 43.65: 'F2',
            46.25: 'F#2', 49.00: 'G2', 51.91: 'G#2', 55.00: 'A2', 58.27: 'A#2', 61.74: 'B2', 65.41: 'C3',
            69.30: 'C#3', 73.42: 'D3', 77.78: 'D#3', 82.41: 'E3', 87.31: 'F3', 92.50: 'F#3', 98.00: 'G3',
            103.83: 'G#3', 110.00: 'A3', 116.54: 'A#3', 123.47: 'B3', 130.81: 'C4', 138.59: 'C#4',
            146.83: 'D4', 155.56: 'D#4', 164.81: 'E4', 174.61: 'F4', 185.00: 'F#4', 196.00: 'G4',
            207.65: 'G#4', 220.00: 'A4', 233.08: 'A#4', 246.94: 'B4', 261.63: 'C5', 277.18: 'C#5',
            293.66: 'D5', 311.13: 'D#5', 329.63: 'E5', 349.23: 'F5', 369.99: 'F#5', 392.00: 'G5',
            415.30: 'G#5', 440.00: 'A5', 466.16: 'A#5', 493.88: 'B5', 523.25: 'C6', 554.37: 'C#6',
            587.33: 'D6', 622.25: 'D#6', 659.25: 'E6', 698.46: 'F6', 739.99: 'F#6', 783.99: 'G6',
            830.61: 'G#6', 880.00: 'A6', 932.33: 'A#6', 987.77: 'B6', 1046.50: 'C7', 1108.73: 'C#7',
            1174.66: 'D7', 1244.51: 'D#7', 1318.51: 'E7', 1396.91: 'F7', 1479.98: 'F#7', 1567.98: 'G7',
            1661.22: 'G#7', 1760.00: 'A7', 1864.66: 'A#7', 1975.53: 'B7', 2093.00: 'C7', 2217.46: 'C#7',
            2349.32: 'D7', 2489.02: 'D#7', 3000: "E7"}

        self.freqList = [16.35, 17.32, 18.35, 20.6, 21.83, 24.5, 25.96, 27.5, 29.14, 30.87,
            32.7, 34.65, 36.71, 38.89, 41.2, 43.65, 46.25, 49.0, 51.91, 55.0, 58.27,
            61.74, 65.41, 69.3, 73.42, 77.78, 82.41, 87.31, 92.5, 98.0, 103.83, 110.0,
            116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.0, 196.0,
            207.65, 220.0, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23,
            369.99, 392.0, 415.3, 440.0, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25,
            659.25, 698.46, 739.99, 783.99, 830.61, 880.0, 932.33, 987.77, 1046.5, 1108.73,
            1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.0, 1864.66,
            1975.53, 2093.0, 2217.46, 2349.32, 2489.02, 3000]


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
        # def normalize(decibelPower):
        noteIncrement = 0.1

        freqInfo = self.spec.getMaxFrequency(self.rangeArray[0],self.rangeArray[1])
        note = self.noteTranslator.note(freqInfo[1])
        prevNote = note
        noteDuration = noteIncrement
        curDecibel = freqInfo[0]
        curMaxDecibel = curDecibel
        for i in range(2,self.rangeArray.size):
            freqInfo = self.spec.getMaxFrequency(self.rangeArray[i-1],self.rangeArray[i])
            note = self.noteTranslator.note(freqInfo[1])
            if (note[0] == prevNote[0] or abs(freqInfo[0]-curDecibel) < 1000):
                noteDuration += noteIncrement
                curDecibel = freqInfo[0]
            else:
                self.noteList.append([prevNote,curMaxDecibel,noteDuration])
                curMaxDecibel = freqInfo[0]
                prevNote = note
                noteDuration = noteIncrement

        self.noteList.append([prevNote,curMaxDecibel,noteDuration])

        # normalize decibel power values to be between 0 and 1
        decibelList = []
        for i in range(len(self.noteList)):
            decibelList.append(self.noteList[i][1])
        mean_power = np.mean(decibelList)
        std_power = np.std(decibelList)

        std_value = 0.25
        
        decibelList = np.where(decibelList > mean_power + std_value*std_power, mean_power + std_value*std_power, decibelList)

        if mean_power - std_value*std_power > 0:
            decibelList = np.where(decibelList < mean_power - std_value*std_power, mean_power - std_value*std_power, decibelList)
        
        max_power = max(decibelList)
        min_power = min(decibelList)
        normalized = [(x-min_power)/(max_power-min_power) for x in decibelList]

        

        # add all normalized values to noteList
        for i in range(len(self.noteList)):
            self.noteList[i][1] = normalized[i] 

            
        return self.noteList


def options():
    parser = argparse.ArgumentParser(description="Read image metadata")
    parser.add_argument("-o", "--first", help="Input audio file.", required=True)
    arg = parser.parse_args()
    return arg

# muzart = Muzart(file = '/vanderbiltCS/SyBBURE/SU23/Owl-City-Fireflies-m8.mp3')
# muzart.run()


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