import numpy as np
import matplotlib.pyplot 
from helper import *
from scipy.signal import hilbert


class SignalProcessing():

    def __init__(self,result_dir:str, signal_row:list[dict],fov:float=20.0):
        self.result_dir=result_dir
        self.fov = float(fov)
        self.signal=signal_row

    def FFT(self):
        signal_freq=np.fft.fftfreq(len(self.signal))
        signal_fft=np.fft.fft(self.signal)*(signal_freq/(signal_freq+1e-10))
        # no_base_signal=np.fft.ifft(signal_fft)
        return signal_freq,signal_fft
    
    def iFFT(self,fft_signal:np.ndarray):
        return np.fft.ifft(fft_signal)
    
    def medium_filter(self,Low_Ratio:float=0.01/20,High_Ratio:float=0.3/20)->np.ndarray:
        fft_freq, fft_result=self.FFT()
        lower_bound=Low_Ratio*self.fov
        hyper_bound=High_Ratio*self.fov
        
        processed_output_fft=np.zeros(fft_result.shape[0],dtype=complex)

        for i in range(fft_result.shape[0]):
            if fft_freq[i]<=-lower_bound and fft_freq[i] >= -hyper_bound:
                processed_output_fft[i]=fft_result[i]
            elif fft_freq[i]>=lower_bound and fft_freq[i] <= hyper_bound:
                processed_output_fft[i]=fft_result[i]
        
        plt.plot(fft_freq,np.abs(fft_result),label="FFT")
        plt.plot(fft_freq,np.abs(processed_output_fft),label="clip FFT")
        plt.legend()
        plt.savefig(os.path.join(self.result_dir,"FFT.png"),dpi=600)
        plt.close()


        processed_output_ifft=self.iFFT(processed_output_fft)
        plt.plot(self.signal,label="original signal")
        plt.plot(np.real(processed_output_ifft),label="clip FFT_iFFT")
        plt.legend()
        plt.savefig(os.path.join(self.result_dir,"clip_signal.png"),dpi=600)
        plt.close()
        return processed_output_ifft
    
    def hilbert_phase(self,processed_output_ifft:np.ndarray):
        hilbert_output=hilbert(np.real(processed_output_ifft))
        output_angle=np.angle(hilbert_output)
        plt.plot(output_angle)
        plt.savefig(os.path.join(self.result_dir,"phase.png"),dpi=600)
        plt.close()
        np.save(os.path.join(self.result_dir,"phase.npy"),output_angle)
        return output_angle


    


# generate_signal=np.cos(np.linspace(0,1199,1199)*2*np.pi/20)

# test_signal=np.load("/home/mcyinsz/python_projects/peem_phase/result/laser435nm_x-1.029y0.517fov10um_exp2s_avr8_obj2041/558/origin_signal.npy")
# test_plot(test_signal)
# generate=SignalProcessing(generate_signal)
# test=SignalProcessing(test_signal)
# # plt.plot(test.FFT()[0],test.FFT()[1])
# # plt.plot(generate.FFT()[0],generate.FFT()[1])
# test_plot(np.real(test.medium_filter()))


