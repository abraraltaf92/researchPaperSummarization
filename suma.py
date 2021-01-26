
from summa import summarizer


def s_s(text,sum_path):
    sum_path.write(summarizer.summarize(text,words=250))
    sum_path.close()
    


