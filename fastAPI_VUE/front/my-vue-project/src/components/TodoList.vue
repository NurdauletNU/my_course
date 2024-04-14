<template>
  <div>
    <h1>Todo List</h1>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" :checked="todo.completed" @change="updateStatus(todo.id, !todo.completed)">
        <span :class="{ completed: todo.completed }">{{ todo.title }}</span>
      </li>
    </ul>
    <input type="text" v-model="newTodo" placeholder="Add new todo">
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
      newTodo: ''
    };
  },
  mounted() {
    this.fetchTodos();
  },
  methods: {
    fetchTodos() {
      fetch('http://localhost:8000/todos')
        .then(response => response.json())
        .then(data => {
          this.todos = data;
        });
    },
    updateStatus(todoId, completed) {
      fetch(`http://localhost:8000/todos/${todoId}?completed=${completed}`, { method: 'PUT' })
        .then(response => response.json())
        .then(updatedTodo => {
          const index = this.todos.findIndex(todo => todo.id === updatedTodo.id);
          if (index !== -1) {
            this.todos.splice(index, 1, updatedTodo);
          }
        });
    },
    addTodo() {
      if (!this.newTodo.trim()) return;
      fetch('http://localhost:8000/todos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: this.newTodo.trim() })
      })
        .then(response => response.json())
        .then(newTodo => {
          this.todos.push(newTodo);
          this.newTodo = '';
        });
    }
  }
};
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>
