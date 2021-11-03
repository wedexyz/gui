
from scipy import signal
import scipy.signal
def filtered (low,high,l2,h2,ch):
    b,a = signal.iirdesign( wp    = [low, high],
                            ws    = [l2, h2],
                            gstop = 60, 
                            gpass = 1, 
                            ftype='ellip')
    filteredBandPass = scipy.signal.lfilter(b, a,ch)
    return filteredBandPass