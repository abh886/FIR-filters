# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 04:19:08 2018

@author: Abhi
"""

from numpy import cos,log10,abs,pi,linspace
import matplotlib.pyplot as plt
from scipy.signal import freqz,lfilter
from scipy.signal import firwin,hanning,bartlett,hamming,boxcar,blackman,firwin2

fpa=int(input('enter passband edge frequency:'))
fsa=int(input('enter stopband edge frequency:'))
N=int(input('enter order of filter'))
Fs=int(input('enter sampling freq:'))
n1=linspace(0,79)
x1=cos(2*pi*100*n1/Fs)
#x2=cos(2*pi*1500*n1/Fs)
#x3=cos(2*pi*4000*n1/Fs) Does not function the same way as matlab
#x=x1+x2+x3
fc=(fpa+fsa)/2

hn=firwin(N,fc/(Fs/2),window="hanning") #good for output but not while plotting window function(Gibbs factor)
A=hanning(N+1)  #needed for plotting window function as it is

w,h=freqz(hn,1,128)
mag=20*log10(abs(h))

y=lfilter(hn,1,x1)

plt.plot((w*Fs/(2*pi)),mag)
plt.title('frequency response')
plt.xlabel('gain magnitude')
plt.grid()
plt.ylabel('amplitude')
plt.show()

plt.stem(A)
plt.title('window')
plt.xlabel('n')
plt.ylabel('w(n)')
plt.show()

plt.stem(y)
plt.title('output response')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

plt.stem(x1)
plt.title('input')
plt.xlabel('n')
plt.ylabel('hd(n)')