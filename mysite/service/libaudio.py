import librosa

from scipy.io import wavfile
import scipy.io

import wavio
import pydub

#y, sr = librosa.load('/home/tawfik/Documents/dev/DjangoExemple/mysite/service/audiofile.mp3')
#wavio.readfile('/home/tawfik/Documents/dev/DjangoExemple/mysite/service/audiofile.wav')
res2 = pydub.AudioSegment.from_mp3('/home/tawfik/Documents/dev/DjangoExemple/mysite/service/file_example_MP3_700KB.mp3')
res = pydub.AudioSegment.from_ogg('/home/tawfik/Documents/dev/DjangoExemple/mysite/service/audiofile.ogg')

print("ok")
