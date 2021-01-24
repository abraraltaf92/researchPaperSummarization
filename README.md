# Research Paper Summarization

### What's left?
    Summarize important citations grouped together using , one at a time !

- [x] Text-To-Text-Transfer-Transformer 
- [ ] Summa-Library
- [ ] wordNet-Similarity-Check

# Some filePath Info :
    data/.../..._parsed_data.csv            --> Scientific Research Paper
    data/.../....annv3_parsed_data.csv      --> Respective Citation Paper
    data/.../summary_t5.txt                    --> t5 abstractive Summarization
 

#### To download google news corpus , this command works :

    brew install wget

    wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

 After downloading replace path of googleNewsCorpus in above code with your local path of googleNewsCorpus
