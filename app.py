from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las tareas (en una aplicación real, usarías una base de datos)
tasks = []

@app.route('/')
def index():
    """Muestra la lista de tareas."""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Agrega una nueva tarea a la lista."""
    task_content = request.form['content']
    if task_content: # Asegúrate de que la tarea no esté vacía
        tasks.append({'id': len(tasks) + 1, 'content': task_content, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Elimina una tarea de la lista."""
    global tasks
    # Filtra la lista para excluir la tarea con el id especificado
    # Nota: Los IDs aquí son simples índices + 1, en una app real serían más robustos.
    tasks = [task for task in tasks if task['id'] != task_id]
    # Re-indexar IDs después de eliminar para evitar problemas (simplificación)
    for i, task in enumerate(tasks):
        task['id'] = i + 1
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Cambia el estado de 'done' de una tarea."""
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)