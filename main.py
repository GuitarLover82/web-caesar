from flask import Flask, request 
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>

<html>
  <head>
    <styles>
      form {
          background-color: #eee;
          padding: 20px;
          margin: 0 auto;
          width: 540px;
          font: 16px sans-serif;
          border-radius: 10px;
      }
      textarea {
          margin: 10px;
          width: 540px;
          height: 120px;
      }
    </style>
  </head>
  <body>
    <input name="rot" type="
  </body>
</html>    
    '''  

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    return 
      

app.run()   