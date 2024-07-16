from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div><h1>HELLO Friends!!!</h1><br><h1>hai!</h1></div"
if __name__=='__main__':
    app.run(debug=True)

