from flask import Flask , jsonify ,render_template

import socket
app = Flask(__name__)

HOST_IP = '10.2.1.190'

@app.route('/')
def hello():
    return 'Hello World!'



@app.route('/get_data')
def get_realtime_data_js():
    try:
        f1 = open("C1.txt",'r')
        LDR1 = f1.readline()
        f1.close()
        LDR1= float(LDR1)
    except:
        LDR1=0.0
    try:
        f1 = open("C2.txt",'r')
        LDR2 = f1.readline()
        f1.close()
        LDR2= float(LDR2)
    except:
        LDR2=0.0
    return jsonify({
        "LDR1":LDR1,
        "LDR2":LDR2
    })
    
@app.route('/stats')
def show_stats():
    return render_template('UI.html', HOST =HOST_IP )


if __name__ == '__main__':
    app.run(host= HOST_IP , port =5000)
