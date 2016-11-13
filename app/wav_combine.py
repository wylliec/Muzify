import scipy
import numpy
from scipy import io
from scipy.io.wavfile import read, write

def combine_waves(wav1, wav2, out_file):
    rate1, signal1 = wav1
    rate2, signal2 = wav2
    #print(numpy.shape(signal1))
    #print(numpy.shape(signal2))
    #print(rate2)
    combined_signal = numpy.concatenate((signal1, signal2))
    return scipy.io.wavfile.write(out_file, rate2, combined_signal)

def read_wav(filename):
    return scipy.io.wavfile.read(filename)