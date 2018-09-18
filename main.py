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
      textarea {{
          margin: 10px 0;
          width: 540px;
          height: 120px;
      }}
      
    </style>
  </head>
  <body>
    <form method="post">
      <label for="rotate-by">Rotate by:</label>
      <input id="rotate-by type="text" name="rot" />
      <input type="textarea" /"
    </form>
  </body>
</html>    
    '''  

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]


    return <h1></h1>
      

app.run()   