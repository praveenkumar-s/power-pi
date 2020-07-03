from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<c>')
def realtime(c):
    f=open(c+'.txt','r')
    o = f.readline()
    f.close()
    return o

if __name__ == '__main__':
    app.run(host= socket.gethostname())
