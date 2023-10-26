from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/login/', methods =["GET", "POST"])
def login():
   if request.method=='POST':
      global a
      a=request.form.get('user')
      global b
      b=request.form.get('email')
      global c
      c=request.form.get('pass')
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug=True)

print(a,b,c)

# @app.route('/signup/', methods =["GET", "POST"])
# def signup():
#    if request.method=='POST':
#       global d
#       d=request.form.get('user')
#       global e
#       e=request.form.get('email')
#       global f
#       f=request.form.get('pass')
#       global g
#       g=request.form.get('Cpass')
#    return render_template('signup.html')

# print(d,e,f,g)