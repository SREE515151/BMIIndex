from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/home')
def homepage():
    print('<p>Welcome to calculation of BMI index</p>')

@app.route('/home/welcome')
def welcome ():
    return render_template('welcome.html')

@app.route('/home/welcome/bmi', methods = ['POST','GET'])
def calcuate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        Height = request.form['height in m']
        Weight = request.form['weight in kg']
        Age = request.form['Age']

    formula = int(Weight * (Height**2))
    result = ""

    if formula > 75 :
        result = "Over weight"
    elif formula < 40 :
        result =" Under weight"
    else:
        result =" Good BMI index"
    
    return render_template('display.html', result = formula )




@app.route('/home/welcome/bmi/verified/<int:score>')
def verified(score):
    return render_template('display.html')


if __name__ == '__main__':
    app.run(debug= True)