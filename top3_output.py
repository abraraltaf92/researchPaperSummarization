import pandas as pd


def top_3(ref,f_name):

    ref_new = pd.read_csv(ref)
    df = pd.read_csv(f_name+ '/output_file.csv')
    for i in range(1, len(df.columns)):
        df_new = df[[df.columns[0], df.columns[i] ]]
        df_new = df_new.sort_values([df_new.columns[1]],ascending=True)
        n = 3
        df_new = df_new[:n]
        for j in range(n):
            df_new.iloc[j] = [ ref_new[ref_new.columns[1]].loc[int(df_new.iloc[j]['ref'].lstrip('reference_'))]
                               , df_new.iloc[j][df_new.columns[1]]]
            df_new['reference_id'] = df['ref']

            df_new.to_csv( f_name + '/' + df_new.columns[1] + '.csv' , index=False )  #  ../citation_i.csv
# top_3('/Users/abraraltaflone/code/python/researchInternship(IITPATNA)/textSummarization/code_data/wmd_2016/data/C00-2123/C00-2123_parsed_data.csv', '/Users/abraraltaflone/code/python/researchInternship(IITPATNA)/textSummarization/code_data/wmd_2016/data/C00-2123')