from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

if __name__=='__main__':
    app.run(debug=True)#,host='0.0.0.0',port=8080