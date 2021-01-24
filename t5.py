import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


def t5_summary(txt, sum_path):
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')

    # file = open(imp_sent_path, mode='r')  # path of file to be read
    processing_text = txt

    text = ''
    for each in processing_text:  # converting list into string
        text += each

    preprocess_text = text.strip().replace("\n", "")

    t5_prepared_Text = "summarize: " + preprocess_text
    print("original text preprocessed: \n", preprocess_text)
    count = 0
    for _ in preprocess_text.split(" "):
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
    for _ in summary.split(' '):
        count += 1

    # file = open(sum_path, mode="w")  # path of summary which will be build
    sum_path.write(summary)
    sum_path.close()
    print(f"\n No. of words  :\n {count}")
    print(len(summary))
