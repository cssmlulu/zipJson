import json
import pandas as pd

def jsonFile_to_df(fin):
    df_day = pd.DataFrame()
    df_tick = pd.DataFrame()
    for eachline in fin:
        if eachline.startswith('#'):
            continue
        js = json.loads(eachline)
        print js
        for (k, v) in js.items():
            try:
                if k == 'DAY':
                    df_day = pd.concat([df_day, pd.read_json(json.dumps(v), orient="index")], axis=0, verify_integrity=True)
                if k == 'TICK':
                    df_tick = pd.concat([df_tick, pd.read_json(json.dumps(v), orient="index")], axis=0, verify_integrity=True)
            except:
                continue

    df_day = df_day.applymap(lambda x: json.dumps(x))
    df_tick = df_tick.applymap(lambda x: json.dumps(x))
    return df_day, df_tick

def df_to_csv(df,name):
    df.to_csv(name,mode='w')

def df_to_hdf(df,name):
    df.to_hdf(name,name,mode='w',complib='blosc')

def csv_to_df(file):
    return pd.read_csv(file,index_col=0)

def df_to_json(df):
    return df.to_json(orient="index",default_handler=str)

if __name__ == '__main__':
    '''
    fin = open('2014.txt','r')
    df_day, df_tick = jsonFile_to_df(fin)
    print df_day.info()
    print df_tick.info()
    df_to_csv(df_day,'2014_day.csv')
    df_to_csv(df_tick,'2014_tick.csv')
    '''
    f_day_csv = '2015_tick.csv'
    df_day = csv_to_df(f_day_csv)
    df_to_hdf(df_day,'2015_tick.h5')
    #j_day = df_to_json(df_day)
    #print j_day
    #with open('out.txt','w') as fout:
    #    fout.write(j_day)