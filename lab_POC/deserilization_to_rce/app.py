import base64 
from flask import Flask, flash, request, redirect, render_template 
import yaml 
from base64 import b64decode 
import binascii 
 
app = Flask(__name__) 
app.secret_key = "secret key"  # for encrypting the session 
 
 
@app.route("/") 
def index(): 
    return """  
    <!DOCTYPE html> 
<html> 
<head> 
<title>Page Title</title> 
</head> 
<body> 
<h1>Hi! Deserialize to me</h1> 
<p>Go to /data path</p> 
</body> 
</html> 

    """ 

 
@app.route("/data", methods=["GET", "POST"]) 
def data(): 
    if request.method == "GET":
        return ''' 
    <!DOCTYPE html> 
<html> 
<body>
<form action="/data" method="post"> Data in Base64<br><input type="text" name="data" value=""><br><br><input type="submit" value="submit"></form> 
</body> 
</html> 
    ''' 
    else: 
        try: 
            data = str( 
                yaml.dump(yaml.load(b64decode(request.form.get("data")), Loader=yaml.Loader))) 
            return '''<!DOCTYPE html> 
<html> 
<body> 
<form action="/data" method="post"> Data in Base64<br><input type="text" name="data" value=""><br><br><input type="submit" value="submit"></form>'''+data+'''</body> 
</html>''' 
        except binascii.Error: 
            return ''' 
    <!DOCTYPE html> 
<html> 
<body> 
<form action="/data" method="post"> Data in Base64<br><input type="text" name="data" value=""><br><br><input type="submit" value="submit"></form> 
</body> 
</html> 
    ''' 
 
 
app.run(debug=True, host="0.0.0.0", port=1234)