import pandas as pd
import json

def panelTojson(p_tick):
     l = ["\"" + str(ts) + "\":" + df.dropna(axis=1).to_json() for ts,df in p_tick.transpose(1,2,0).iteritems()]
     return ','.join(l)

def h5ToPanel(filename, type):
    p = pd.read_hdf(filename, type)
    p.major_axis = pd.to_datetime(p.major_axis)
    return p

def csvToPanel(filename):
    df = pd.read_csv(filename,index_col=[0,1],parse_dates=[0])
    return df.to_panel()
    
if __name__ == '__main__':
    #p_tick = h5ToPanel("2015_tick_multiIndex.h5","tick")
    p_tick = csvToPanel("all_tick_multiIndex.csv.gz")
    for index,p in p_tick.groupby([p_tick.major_axis.date,p_tick.major_axis.hour]):
        print panelTojson(p)
