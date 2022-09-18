from flask_restful import Api, Resource, reqparse
from flask import request

from os import listdir
from os.path import isfile, join
import json
import pandas as pd



def getByFileName(f_name):
  with open(join('data',f_name)) as f:
    dic = json.load(f)
  return dic

def changeLabel(f_name,label,score):
  with open( join('data',f_name)) as f:
    dic = json.load(f)
  dic['label'] = label
  dic['score'] = score
  with open( join('data',f_name), 'w') as f:
    json.dump(dic,f)




class GetbyPage(Resource):
  def get(self):
    page = request.args.get('page', type = int)
    strt = page*3-3
    end = page*3
    df = pd.read_csv('tracked.csv')
    result = []
    for i in range(strt,end):
      result.append(getByFileName(df.f_name.iloc[i]))
    for i,article in enumerate(result):
      article["ID"]=page*3-3+i
    return result

class GetRecommendation(Resource):
  def get(self):
    newsID = request.args.get('originalID', type=int)
    recom1 = (newsID+1)%len(news)
    recom2 = (newsID+2)%len(news)
    df = pd.read_csv('tracked.csv')
    result = [betByFileName(df.f_name.iloc[recom1]),getByFileName(df.f_name.iloc[recom2])]
    result[0]['ID'] = recom1
    result[1]['ID'] = recom2
    return result

