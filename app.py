from flask import Flask, jsonify, request

app  = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/hithere")
def hi_there_everyone():
    return ("I just hit /hithere")

@app.route("/add_two_nums", methods = ["POST"])
def add_two_nums():
    #Get x,y from the posted data
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "Error", 305

    #Add x,y 
    x = dataDict["x"]
    y = dataDict["y"]


    #prepared Json "z":z
    z = x+y

    retJson = {
        "z": z
    }

    #return jsonify(map_prepared)
    return retJson,200






@app.route("/bye")
def bye():
    age = 2*5
    retJson = {
        "Name" : "Elfarouk",
        "Age" : age,
        "phones" : [
            {
                "phoneName" : "iphone8",
                "phoneNumber" : 11111111
            },
            {
                "phoneName" : "SamSungS23",
                "phoneNumber" : 22221111
            }
        ]
    }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(debug = True)