
from numpy.core.numeric import outer
from scipy import signal
import scipy.signal

samp_freq = 200 
notch_freq = 60.0  # Frequency to be removed from signal (Hz)
quality_factor = 100.0 # Quality factor
def bp (chanel,pole,low,high):
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
    dn = signal.filtfilt(b_notch, a_notch, chanel)
    b, a = scipy.signal.butter(pole, [low, high], 'band')
    df = scipy.signal.lfilter(b, a, dn)
    return df
 


