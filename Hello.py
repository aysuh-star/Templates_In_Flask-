from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html',name=name) 

# @app.route('/user/<comments>') 
# def com(comments):
#     return render_template('user.html',comments=comments)
if __name__ == '__main__':
    app.run(debug=True)
