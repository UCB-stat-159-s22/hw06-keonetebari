from ligotools import readligo as rl
from ligotools import utils as ul

from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
from scipy.io import wavfile
from scipy.interpolate import interp1d
import json
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.image as mpimg

def test_util():
    
    
    
    eventname = 'GW150914' 
    
    fnjson = "data/BBH_events_v3.json"
    
    events = json.load(open(fnjson,"r"))
    event = events[eventname]
    
    fn_H1 = 'data/' + event['fn_H1']          

    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    
    ### Test Whiten
    
    fs = event['fs']
    NFFT = 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    
    psd_H1 = interp1d(freqs, Pxx_H1)
    
    strain_H1_whiten = ul.whiten(strain_H1,psd_H1,dt)
    assert np.isclose(sum(strain_H1_whiten, 9.621319784353773))
    
    ### Test reqshift
    
    fs = 4096
    fshift = 400.
    speedup = 1.
    fss = int(float(fs)*float(speedup))
    
    fband = event['fband']
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[1]-fband[0])/(fs/2))

    strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
    
    strain_H1_shifted = reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
    
    assert len(strain_H1_shifted) == 131072
    
    
    ### Test write wavefile
    
    x = wavfile.read(r'audio/'+eventname+"_H1_whitenbp.wav")
    assert len(x[1]) == 16384
    
    
    ### Test plot 
    
    pic = "GW150914_ASDs.png"
    img = mpimg.imread(r'figurs/'+pic)
    imgplot = plt.imshow(img)
    assert isinstance(img, np.ndarray)
    