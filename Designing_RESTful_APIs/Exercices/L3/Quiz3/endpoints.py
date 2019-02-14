#THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM AN API ENDPOINT
from flask import Flask
app = Flask(__name__)

@app.route('/puppies')
def puppiesFunction():
	return "Yes, puppies!"
	
@app.route('/puppies/<int:id>')
def poppiesFunctionId(id):
	return "This meethod will act on the puppy with id {}".format(id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
