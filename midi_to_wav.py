import os
from midi2audio import FluidSynth

# Specify the paths for the soundfont, input MIDI file, and output WAV file
sound_font_path = "E:/Study bk/nen/MIDI Jazz/FluidR3_GM/FluidR3_GM.sf2"  # Replace with the path to your .sf2 soundfont file
input_midi_path = "E:/Study bk/nen/separated_melody_chords.mid"     # Replace with the path to your input MIDI file
output_wav_path = "E:/Study bk/nen/output.wav"    # Replace with the desired path for the output WAV file

# Verify file paths
if not os.path.exists(sound_font_path):
    raise FileNotFoundError(f"SoundFont file not found: {sound_font_path}")
if not os.path.exists(input_midi_path):
    raise FileNotFoundError(f"MIDI file not found: {input_midi_path}")

# Initialize FluidSynth with the soundfont
fs = FluidSynth(sound_font=sound_font_path)

# Convert the MIDI file to a WAV file
fs.midi_to_audio(input_midi_path, output_wav_path)

print(f"Conversion complete! WAV file saved at: {output_wav_path}")