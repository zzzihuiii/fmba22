#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask


# In[10]:


app = Flask(__name__)


# In[11]:


from flask import request, render_template
import joblib 
@app.route("/", methods=["GET","POST"])

def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSreg")
        pred = model.predict([[float(rates)]])
        s1 = "Predicted DBS Share price based on Linear Regression Model is: " + str(pred)
        model = joblib.load("DBSDT")
        pred = model.predict([[float(rates)]])
        s2 = "Predicted DBS Share price based on Decision Tree Model is: " + str(pred)
        model = joblib.load("DBSNN")
        pred = model.predict([[float(rates)]])
        s3 = "Predicted DBS Share price based on Neural Network Model is: " + str(pred)
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:




