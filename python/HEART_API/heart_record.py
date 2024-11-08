from flask import Flask, jsonify, request

app = Flask(__name__)
hearts = [
    {
        "heart_id" : "1",
        "date" : ["November 08,2024"],
        "heart_rate" : ["120/90"]
    },

]

@app.route('/hearts', methods = ['GET'])
def gethearts():
    return jsonify(hearts)

@app.route('/hearts', methods=['POST'])
def addhearts():
   new_hearts = request.get_json()
   hearts.append(new_hearts)
   return jsonify({'message':'Successfull'}), 200

@app.route('/hearts/<int:index>', methods = ['DELETE'])
def deletehearts(index):
    hearts.pop(index)
    return 'The Heart Record has been deleted', 200

@app.route('/hearts/<int:index>', methods=['PUT'])
def update_hearts(index):
   heart = request.get_json()
   hearts[index] = heart
   return jsonify(hearts[index]), 200

if __name__ == '__main__':
    app.run()
