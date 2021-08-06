from flask import Flask,render_template,request
import joblib
# initialse the app
app = Flask(__name__)

#load the model
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return render_template ('form.html')

@app.route('/submit',methods=["POST"])
def form_data():
    print('here')
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    test=request.form.get('test')
    output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])


    # print(output)
    output
    if output[0]== 1:
        out='diabetic'
    else:
        out='notdiabetic'

    return render_template('Predict.html',data={out})

if __name__ == '__main__':
    app.run(debug=True) 