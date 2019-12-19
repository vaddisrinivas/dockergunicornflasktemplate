from flask import Flask
import configparser,sys,os
app = Flask(__name__)

#setting configuration
#conf = configparser.ConfigParser()
#conf.read(filenames=os.environ["pyconf"])

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()