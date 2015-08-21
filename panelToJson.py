import pandas as pd
import json

def panelTojson(p_tick):
     #for ts,df in p_tick.transpose(1,2,0).iteritems():
     #   print "\"" + ts + "\":" + df.dropna(axis=1).to_json()
     l = ["\"" + str(ts) + "\":" + df.dropna(axis=1).to_json() for ts,df in p_tick.transpose(1,2,0).iteritems()]
     return ','.join(l)

if __name__ == '__main__':
    p_tick = pd.read_hdf("2015_tick_multiIndex.h5",'tick')
    p_tick.major_axis = pd.to_datetime(p_tick.major_axis)
    for index,p in p_tick.groupby([p_tick.major_axis.date,p_tick.major_axis.hour]):
        print panelTojson(p)
    #panelTojson(p_tick)
    #l = ["\"" + ts + "\":" + df.dropna(axis=1).to_json() for ts,df in p_tick.transpose(1,2,0).iteritems()]
    #print ','.join(l)