import numpy as np
import matplotlib.pyplot 
from helper import *


class SignalProcessing():

    def __init__(self, signal_row:list[dict]):
        self.signal=signal_row

    def FFT(self):
        signal_freq=np.fft.fftfreq(len(self.signal))
        signal_fft=np.fft.fft(self.signal)
        return signal_freq,signal_fft
    


generate_signal=np.cos(np.linspace(0,1199,1199)*2*np.pi/20)

test_signal=np.load("/home/mcyinsz/python_projects/peem_phase/result/laser435nm_x-1.029y0.517fov10um_exp2s_avr8_obj2041/558/origin_signal.npy")
test_plot(test_signal)
generate=SignalProcessing(generate_signal)
test=SignalProcessing(test_signal)
plt.plot(generate.FFT()[0],np.abs(generate.FFT()[1]))
plt.plot(test.FFT()[0],np.abs(test.FFT()[1]))
plt.show()


