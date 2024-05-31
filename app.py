from flask import Flask, request, jsonify
from moldels.task  import Task

app = Flask(__name__)

#CRUD
#Create, Read, Update and Delete = Criar, Ler, Atualizar E Deletar 
# Tarefas
tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control+= 1 
    print(tasks)
    tasks.append(new_task)

    return jsonify({"mensagem" : "Nova tarefa criada com sucesso "})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"mensagem" : "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({'mensagem': 'Não foi possível encontrar a ativide'}), 404        

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({'mensagem' : 'Tarefa atualizada com sucesso'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_taske(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    if not task:        
        return jsonify({'mansegam' :'Não foi possível encontrar a ativide'}), 404
    
    tasks.remove(task)
    return jsonify({'mensagem' : 'Tarefa deletada com sucesso'})
    
if __name__ == "__main__":
 app.run(debug=True)

