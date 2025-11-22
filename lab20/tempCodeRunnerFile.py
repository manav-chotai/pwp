
import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r"D:\ict\sem3\PWP\lecture code\labs\lab20\file_example_WAV_1MG.wav")
# Write audio file
sf.write('new_audio_file.wav', audio, sample_rate)

