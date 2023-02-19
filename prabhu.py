from flask import *
import matplotlib
app=Flask(__name__)
@app.route('/name')
def index():

 return render_template("")

if __name__ == '__main__':
 app.run(debug=True)