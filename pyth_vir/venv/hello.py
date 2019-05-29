from flask import Flask,render_template
app = Flask(__name__)

#@app.route('/')
#def index():
  # return render_template('hello.html')

#@app.route('/hello/<user>')
#def hello_name(user):
   
   #return render_template('hello.html', name = user)

@app.route('/intparam/<int:value>')
def url_with_intparam(value):
    return render_template('hello.html',inputvalue=value)

if __name__ == '__main__':
   app.run(debug = True)