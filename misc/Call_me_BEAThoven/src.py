import os
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def generate_tone(frequency, duration_ms, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * duration_ms / 1000), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)

    audio_segment = AudioSegment(
        (tone * (2**15 - 1) * volume).astype(np.int16).tobytes(),
        frame_rate=sample_rate,
        sample_width=2,
        channels=1
    )
    return audio_segment

frequencies = {
    'A': 220,  'B': 270,  'C': 320,  'D': 370,  'E': 420,  'F': 470,  'G': 520,
    'H': 570,  'I': 620,  'J': 670,  'K': 720, 'L': 770, 'M': 820, 'N': 870,
    'O': 920, 'P': 970, 'Q': 1020, 'R': 1070, 'S': 1120, 'T': 1170, 'U': 1220,
    'V': 1270, 'W': 1320, 'X': 1370, 'Y': 1420, 'Z': 1470
}

tone_duration = 200    
pause_duration = 100   
pause = AudioSegment.silent(duration=pause_duration)

phonetic_alphabet = {
    'A': 'Adam',  'B': 'Bertil', 'C': 'Caesar',  'D': 'David', 'E': 'Erik',
    'F': 'Filip', 'G': 'Gustav', 'H': 'Helge',   'I': 'Ivar',  'J': 'Johan',
    'K': 'Kalle', 'L': 'Ludvig', 'M': 'Martin',  'N': 'Niklas','O': 'Olof',
    'P': 'Petter','Q': 'Qvintus','R': 'Rudolf',  'S': 'Sigurd','T': 'Tore',
    'U': 'Urban', 'V': 'Viktor', 'W': 'Wilhelm', 'X': 'Xerxes','Y': 'Yngve',
    'Z': 'Zäta'
}

def create_phonetic_pattern(phrase):
    result = AudioSegment.silent(duration=0)
    for char in phrase:
        if char == ' ':
            result += pause  
        elif char.upper() in phonetic_alphabet:
            
            freq = frequencies.get(char.upper(), 1000)  
            tone = generate_tone(freq, tone_duration)
            result += tone + pause  
    return result

swedish_code_phrase = "Adam Martin Adam Zäta Ivar Niklas Gustav  Helge Adam Rudolf Martin Olof Niklas Ivar Erik Sigurd  Helge Ivar David Erik  Tore Helge Erik  Martin Erik Ludvig Olof David Yngve  Olof Filip  Wilhelm Tore Filip Caesar Tore Filip { Tore Olof Niklas Erik Sigurd _ Caesar Adam Niklas _ Urban Niklas Ludvig Olof Caesar Kalle _ Sigurd Erik Caesar Rudolf Erik Tore Sigurd }  Wilhelm Ivar Tore Helge Ivar Niklas  Tore Helge Erik  Filip Rudolf Erik Qvintus Urban Erik Niklas Caesar Ivar Erik Sigurd ."

phonetic_pattern = create_phonetic_pattern(swedish_code_phrase)

new_dir = "C:/Users/hp/Desktop/Sheet_of_Music/"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

audio_file_path = os.path.join(new_dir, "swedish_code_pattern.wav")
phonetic_pattern.export(audio_file_path, format="wav")


os.system(f'start {audio_file_path}')

play(phonetic_pattern)

print(f"Phonetic code exported to: {audio_file_path}")
