from flask import Flask, render_template, request
import os
from hash import generateHash

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}
encryptedData ={}

@app.route("/", methods= ["GET", "POST"])
def home():
    print("running")
    print(request.args.get("form"))
    global blockData, encryptedData
    validation = None
    if request.method == "GET":
        return render_template('index.html')
    elif request.args.get("form") == "f1":
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
       
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }

        sender = generateHash(sender)
        receiver = generateHash(receiver)
        blockHash = generateHash(sender+receiver+amount)

        encryptedData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
                "hash" : blockHash
            }
    else:        
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        hash = request.form.get("hash")
        
        validationHash = generateHash(sender+receiver+amount)

        if validationHash == hash:
            message= "Success"   
        else: 
            message = "Failed"

        validation = { 
               "message": message,
               "blockHash": hash,
               "validationHash": validationHash 
        }    

    return render_template('index.html', blockData = blockData, encryptedData = encryptedData, validation = validation)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)