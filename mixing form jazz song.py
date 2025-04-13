import os
from pydub import AudioSegment

# xác định 2 file wav đầu vào và file wav đầu ra
wav_file_1 = "E:/Study bk/nen/separated_melody_chords.wav"  
wav_file_2 = "E:/Study bk/nen/input.wav"  
output_mixed_wav = "E:/Study bk/nen/mixed_output_formjazz.wav" 

# check lại file wav đầu vào
if not os.path.exists(wav_file_1):
    raise FileNotFoundError(f"File not found: {wav_file_1}")
if not os.path.exists(wav_file_2):
    raise FileNotFoundError(f"File not found: {wav_file_2}")

# load file wav đầu vào
audio1 = AudioSegment.from_file(wav_file_1)
audio2 = AudioSegment.from_file(wav_file_2)

# trộn 2 file wav lại với nhau
mixed_audio = audio1.overlay(audio2)

# xuất file wav đầu ra
mixed_audio.export(output_mixed_wav, format="wav")

print(f"Mixing complete! Mixed WAV file saved at: {output_mixed_wav}")