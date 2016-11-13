import scipy
import numpy
from scipy import io
from scipy.io.wavfile import read, write

def combine_waves(wav1, wav2):
    rate1, signal1 = scipy.io.wavfile.read(wav1)
    rate2, signal2 = scipy.io.wavfile.read(wav2)
    combined_signal = numpy.concatenate((signal1, signal2))
    return scipy.io.wavfile.write("combined_wav.wav", rate1, combined_signal)
