import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output>= 0.50:
        return render_template('index.html', prediction_text='Affecting with heart disease, contact doctor immediately')
  
    else:
        return render_template('index.html', prediction_text='You are not affected with any heart disease , take care of your health')

    

    

if __name__ == "__main__":
    app.run(debug=True)