from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.ApiHandler import GetbyPage, GetRecommendation, getByFileName, changeLabel
from os import listdir
from os.path import isfile, join, exists
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

#track all files in the data folder, make prediction if it is newly added

mypath = 'data'
file_names = pd.Series([f for f in listdir(mypath) if isfile(join(mypath, f))])
if not exists('tracked.csv'):
    df = pd.DataFrame({'f_name':[]})
    df.to_csv('tracked.csv',index=False)
df = pd.read_csv('tracked.csv')
tracked_or_not = file_names.isin(df['f_name'])  #the column that stores file names
untracked = file_names[~tracked_or_not.values]
if untracked.size > 0:
    from transformers import BertTokenizer, BertForSequenceClassification
    import torch
    model = BertForSequenceClassification.from_pretrained("model", num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    count = 0
    proceed = True
    while(proceed):
        start = count
        raw_input = []
        for i in range(8):
            content = getByFileName(untracked[count])['content']
            raw_input.append(content)
            count+=1
            if count == untracked.size:
                proceed = False
                break
        batch = tokenizer(raw_input, padding='max_length', truncation=True, max_length=512,return_tensors="pt")
        outputs = model(**batch)
        logits = outputs.logits
        prediction_label = torch.argmax(logits, dim = -1)
        prediction_score = torch.nn.functional.softmax(logits, dim=-1)
        for i in range(start,count):
            label = prediction_label[i-start].item()
            score = prediction_score[i-start, label].item()
            changeLabel(untracked[i], label, score)
    df_untracked = pd.DataFrame({ 'f_name' : untracked })
    df = pd.concat([df,df_untracked])
    df.to_csv('tracked.csv',index=False)
print('initialized')




api.add_resource(GetbyPage, '/page')
api.add_resource(GetRecommendation, '/recommend')
