#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home directory
def hello():
    return "Hello DS_C23_NLP_DL Learners. Welcome to the Deployment class."

# If you want to run this app, you must call the run()
if __name__=='__main__':
    app.run(debug=True)

# To execute this file, do as below after opening Anaconda prompmpt
# python BasicFlask.py