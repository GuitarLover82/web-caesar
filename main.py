from flask import Flask, request 

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
    '''  

@app.route("/")
def index():
    return

app.run()   