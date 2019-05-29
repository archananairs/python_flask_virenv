from flask import Flask,render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'name':'archana','id':60,'designation':'contractor'}
   return render_template('loop_result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)


