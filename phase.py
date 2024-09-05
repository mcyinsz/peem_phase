import numpy as np
import matplotlib.pyplot 
from helper import *


class SignalProcessing():

    def __init__(self, signal_row:list[dict]):
        self.signal=signal_row

    def FFT(self):
        signal_freq=np.fft.fftfreq(len(self.signal))
        signal_fft=np.fft.fft(self.signal)
        test_plot(np.abs(signal_fft))


x=np.linspace(0,1200,1200,dtype=np.int16)
test_signal=np.cos(x)
test=SignalProcessing(test_signal)
test.FFT()


