import pandas as pd
import sys
import sklearn
import os
import gensim




# preprocessing a bit - stopwords

from nltk.corpus import stopwords
from nltk import download
download('stopwords')    # download stopwords list

stopWords = stopwords.words('english')  #selecting language




googleNewsCorpus_path = '/Users/abraraltaflone/code/python/GoogleNews-vectors-negative300.bin.gz'
if not os.path.exists(googleNewsCorpus_path):
    raise ValueError(" Alert : You need to download the google news corpus")

model = gensim.models.KeyedVectors.load_word2vec_format(googleNewsCorpus_path, binary=True)

def calc_dist(citation,reference):
    citation = citation.lower().split()
    reference = reference.lower().split()
    print( 'before processing text : \n' )
    print(f'citation : {citation}')
    print(f'reference :{reference}')

    citation = [ x for x in citation if x not in stopWords ]
    reference = [ x for x in reference if x not in stopWords ]


    distance = model.wmdistance(citation,reference)

    print(' after processing text : \n ')
    print(f'citation : {citation}')
    print(f'reference :{reference}')
    print('\n distance : %.4f' %distance)

    return distance

def dist(rp,cp,f_name):
    ref = pd.read_csv(rp)
    cit = pd.read_csv(cp)
    df = pd.DataFrame( columns=['ref'] + ['citation_' + str(i) for i in range(len(cit)) ])

    for i in range(len(ref)):
        ref_txt = ref.loc[i][ref.columns[1]]
        print(f'calculating distances for refernce {i} ...')
        col = [ f'reference_{i}' ] + [ calc_dist(j,ref_txt) for j in list( cit[cit.columns[1] ] )  ]

        df.loc[i] = col
        print(f' distance calculated for reference number {i}')

    file_name = f_name+'/output_file.csv'
    df.to_csv(file_name,index=False)





