from ligotools import readligo as rl
import numpy as np
import json

# Setup
def test_rl():
    
    eventname = 'GW150914' 
    
    fnjson = "data/BBH_events_v3.json"
    
    events = json.load(open(fnjson,"r"))
    event = events[eventname]
    
    fn_H1 = 'data/' + event['fn_H1']          

    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    assert isinstance(time_H1, np.ndarray)
    assert time_H1.shape[0] == 131072
    assert np.isclose(sum(time_H1), 147621080203232.25)
    assert np.isnan(time_H1).any() == False