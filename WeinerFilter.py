# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:31:01 2023

@author: prash
"""

import os
import numpy as np
import scipy.io
import matplotlib.pyplot as plt

def wiener(im, mysize = None, noise = None):
    im = np.asarray(im)
    if mysize is None:
        mysize = [3] * im.ndim
    mysize = np.asarray(mysize)
    if mysize.shape == ():
        mysize = np.repeat(mysize.item(), im.ndim)

    lMean = np.correlate(im, np.ones(mysize), 'same') / np.prod(mysize, axis=0)

    lVar = (np.correlate(im ** 2, np.ones(mysize), 'same') /
            np.prod(mysize, axis=0) - lMean ** 2)

    if noise is None:
        noise = np.mean(np.ravel(lVar), axis=0)

    res = (im - lMean)
    res *= (1 - noise / lVar)
    res += lMean
    out = np.where(lVar < noise, lMean, res)

    return out

if __name__ == '__main__':
    samplerate, data = scipy.io.wavfile.read("science.wav")
    out = wiener(data, 50)
    plt.plot(out)
    scipy.io.wavfile.write(os.path.join('.', 'test_science.wav'), samplerate, out)