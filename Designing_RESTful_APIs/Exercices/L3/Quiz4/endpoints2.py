from flask import Flask, request


app = Flask(__name__)

def getAllPuppies():
    return "Getting All the puppies!"
def makeANewPuppy():
    return "Creating A New Puppy!"
def getPuppy(id):
    return "Getting Puppy with id {}".format(id)
def updatePuppy(id):
    return "Updating Puppy with id {}".format(id)
def deletePuppy(id):
    return "Removing Puppy with id {}".format(id)

@app.route('/puppies', methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
        return getAllPuppies()
    elif request.method  == 'POST':
        return makeANewPuppy()
    else:
        print("This is a diffren request {}".format(request.method))

@app.route('/puppies/<int:id>',methods=['GET','PUT','DELETE'])
def puppiesFunctionId(id):
    if request.method  == 'GET':
        return getPuppy(id)
    elif request.method  == 'PUT':
        return updatePuppy(id)
    elif request.method  == 'DELETE':
        return deletePuppy(id)
    else:
        print("This is a diffrent request {}".format(request.method))

if __name__ ==  '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
