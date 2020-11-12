from flask import Flask,render_template, request, Markup
from flask_pymongo import PyMongo
from bson import ObjectId


import pymongo
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.Patient

mycollection = mydb.Doctor

#mongo = PyMongo(app)
#result=list(mycollection.find({}))



    


@app.route("/",methods=['GET','POST'])
def start():
    #print(result)
    if request.method == 'POST':
        pid = request.form['patientid']
        disease = request.form['disease']
        #cur = db.mycoltech.cursor()
        #result=mycoltech.update({"PatientID":pid}, {'$set':{ "Result":disease}})
        mycoltech.update({"PatientID":pid},{'$set':{ "Result":disease}})

        #if result: 

        return ("success")   
           


        
        #cur = mongo.mycoltech.cursor()



    #print(result)
    return render_template("index1.html")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


 







    #try:

      #  Project_List_Col = db.Doctor.find()
      #  return render_template('index1.html',tasks=Project_List_Col)
    #except Exception as e:
        #return dumps({'error': str(e)})
    #pid = patientid
    #disease = disease
    #print(list(mycoltech.find({})))

    #return render_template('index1.html')

#if __name__ == "__main__":
#   app.run(debug=True)
