from flask import Flask,render_template

app=Flask(__name__) 
@app.route('/')
def home():
    name='sangeeth'
    return  ('login.html')

@app.route('/login', methods=['POST','GET'])
def login():
        return render_template ('index.html')

if __name__=='__main__':
    app.run(debug=True)
