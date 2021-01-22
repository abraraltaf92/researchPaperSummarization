import torch
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-large')
tokenizer = T5Tokenizer.from_pretrained('t5-large')
device = torch.device('cpu')

file = open("/Users/abraraltaflone/code/prepocessed_text.txt", mode='r')
processing_text = file.readlines()
file.close()
text = ''
for each in processing_text:  # converting list into string
    text += each

preprocess_text = text.strip().replace("\n", "")

t5_prepared_Text = "summarize: " + preprocess_text
print("original text preprocessed: \n", preprocess_text)
count = 0
for each in preprocess_text.split(" "):
    count += 1
print(f"\n No. of words: \n {count}")
summary = ""

for i in range(len(t5_prepared_Text) // 512):
    tokenized_text = tokenizer.encode(t5_prepared_Text[i:i + 512], return_tensors="pt").to(device)

    summary_ids = model.generate(tokenized_text, num_beams=4, no_repeat_ngram_size=2, min_length=25, max_length=30,
                                 early_stopping=True)
    
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary = summary + output
    i += 512

print("\n\nSummarized text: \n", summary)
count = 0
for each in summary.split(' '):
    count += 1

file = open("/Users/abraraltaflone/code/summary.txt", mode="w")
file.write(summary)
file.close()
print(f"\n No. of words  :\n {count}")
print(len(summary))
