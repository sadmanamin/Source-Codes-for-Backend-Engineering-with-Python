from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "hello from service - port "+str(os.getenv("PORT"))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv("PORT"))



