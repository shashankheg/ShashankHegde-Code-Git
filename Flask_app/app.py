from flask import Flask,render_template,request
# initialse the app
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template ('form.html')
@app.route('/home')
def home():
    # return 'Home'
    return render_template('index.html')    
    

# @app.route('/home')
# def home():
#     return render_template('index.html')

@app.route('/contact')
def contact():
     return 'contact page'
@app.route('/submit' , methods= ["POST"])
def form_data():
    fname=request.form.get('fname')
    sname=request.form.get('sname')
    phonenum=request.form.get('phone')
    mail=request.form.get('email')
    print(fname,sname,phonenum,mail)
    return 'form submitted'

if __name__ == '__main__':
    app.run(debug=True) 