import json
import pandas as pd
import gzip

def jsonFile_to_df(fin,fout):
    d_day = dict()
    d_tick = dict()
    for i,eachline in enumerate(fin):
        if eachline.startswith('#'):
            continue
        js = json.loads(eachline)
        print js
        for (k, v) in js.items():
            #print v
            try:
                if k == 'DAY':
                    d_day.update(v)
                if k == 'TICK':
                    d_tick.update(v)
            except:
                continue

    p_day = pd.Panel.from_dict(d_day, orient='minor').transpose(0,2,1)
    p_tick = pd.Panel.from_dict(d_tick, orient='minor').transpose(0,2,1)

    p_day.to_pickle(fout+'_day_multiIndex.pkl')
    p_tick.to_pickle(fout+'_tick_multiIndex.pkl')

    p_day.to_hdf(fout+'_day_multiIndex.h5', 'day', mode='w', complib='blosc',complevel=9)
    p_tick.to_hdf(fout+'_tick_multiIndex.h5', 'tick', mode='w', complib='blosc',complevel=9)
'''
    df_day = p_day.to_frame(filter_observations=False)
    df_tick = p_tick.to_frame(filter_observations=False)

    with gzip.open(fout+'_day_multiIndex.csv.gz', 'wb') as f_day:
        df_day.to_csv(f_day)
    with gzip.open(fout+'_tick_multiIndex.csv.gz', 'wb') as f_tick:
        df_tick.to_csv(f_tick)
'''


if __name__ == '__main__':
    filename = '2015'
    with open(filename+'.txt','r') as fin:
        jsonFile_to_df(fin,filename)

