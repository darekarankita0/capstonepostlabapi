#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS, cross_origin
import json
import requests
import pandas as pd
import random

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET','POST'])
def que():
    data = pd.read_csv('Post_Lab_Questions.csv')
    que = list(data['Questions'])
    a = (random.sample(que,5))
    #listToStr = ' '.join([str(elem) for elem in a])
    qs = ""
    for (i,ele) in enumerate(a):
        qs = qs + str(i+1)+ str(ele)
    #print(listToStr)
    data = {
       'postlab_questions' : qs,
    }
    data = json.dumps(data)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=False)


# In[ ]:




