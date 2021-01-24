import pandas as pd
import glob

def imp_sent(f_name):
    cit_files = list(glob.glob(f_name+"/citation*.csv"))
    df = pd.DataFrame( columns = [ 'reference_id', 'reference' ])
    
    ref_id = []
    ref_txt = []
    
    for file in cit_files:
        df_ = pd.read_csv(file)
        
        for Id,txt in zip(list(df_.reference_id), list(df_.ref)):
            if Id not in ref_id:
                ref_id.append(Id)
                ref_txt.append(txt)
                
    df['reference_id'] = ref_id
    df['reference'] = ref_txt
    df['temp_col'] = [ int(i.lstrip('reference_'))for i in ref_id]
    df.sort_values(['temp_col'],ascending=True,inplace=True)
    df.drop(["temp"],axis=1,inplace=True)
    
    df.to_csv(f_name + '/important_sentences.csv',index=False)

    with open(f_name + '/important_sentences.txt', 'w',encoding= 'utf-8') as filehandle:
        text = "\n".join(map(lambda x: x.replace("\n", " "), df.reference))
        filehandle.write(text)

