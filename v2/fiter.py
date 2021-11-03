
from scipy import signal
import scipy.signal
def filtered (low,high,ch):
    b,a = signal.iirdesign( wp    = [low, high],
                            ws    = [0.001, 0.001],
                            gstop = 60, 
                            gpass = 1, 
                            ftype='ellip')
    filteredBandPass = scipy.signal.lfilter(b, a,ch)
    return filteredBandPass