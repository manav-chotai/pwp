import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r'D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav')



import soundfile as sf
# Read existing audio file into data
data, samplerate = sf.read(r"D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav")
# Write it to another file
sf.write('output.wav', data, samplerate)



import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r"D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav")
# Write audio file
sf.write('new_audio_file.wav', audio, sample_rate)


import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
audio , sample_rate = sf.read(r"D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav")
# Load audio file
#audio, sample_rate = sf.read('audio_file.wav')
# Create time axis
time = np.arange(0, len(audio)) / sample_rate
# Plot audio signal
plt.plot(time, audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()


from pydub import AudioSegment
# Load audio file
audio = AudioSegment.from_file(r'D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav')
# Add fade in effect
audio_fade_in = audio.fade_in(2000)  # 2 seconds
# Export audio file with fade in effect
audio_fade_in.export('audio_file_fade_in.wav', format='wav')