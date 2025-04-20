from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{ "label": "Limpiar setup", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    if isinstance(request_body, dict):
        todos.append(request_body)
    else:
        # Si no es un diccionario, convertirlo a uno
        todos.append({"label": str(request_body), "done": False})
    
    # Devolver la lista actualizada convertida a JSON
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    

    if position >= 0 and position < len(todos):
       deleted_todo = todos.pop(position)
       print(f'Se elimino correctamente: {deleted_todo}')

       return jsonify(todos)
    else:
       return jsonify({'error': 'Posicion ivalidada'}), 400


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)