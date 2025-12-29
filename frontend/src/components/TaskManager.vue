<template>
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
      <div>
        <h2 class="text-3xl font-bold text-gray-900 tracking-tight">My Tasks</h2>
        <p class="text-gray-500 mt-1">Organize your daily jobs and projects.</p>
      </div>
      <button 
        @click="logout" 
        class="px-5 py-2 text-sm font-medium text-red-600 bg-white border border-gray-200 rounded-xl hover:bg-red-50 hover:border-red-100 hover:text-red-700 transition-all shadow-sm"
      >
        Sign Out
      </button>
    </div>

    <div class="bg-white rounded-2xl p-1 shadow-sm border border-gray-200 mb-10 transition-shadow hover:shadow-md">
      <form @submit.prevent="addTask" class="flex flex-col md:flex-row gap-0 md:gap-2">
        
        <input 
          v-model="newTask.title" 
          placeholder="What needs to be done?" 
          required 
          class="flex-1 px-6 py-4 bg-transparent outline-none text-gray-700 placeholder-gray-400 font-medium" 
        />
        
        <div class="w-px bg-gray-200 my-2 hidden md:block"></div> <input 
          v-model="newTask.description" 
          placeholder="Add details..." 
          class="flex-1 px-6 py-4 bg-transparent outline-none text-gray-600 placeholder-gray-400" 
        />
        
        <div class="w-px bg-gray-200 my-2 hidden md:block"></div>

        <select 
          v-model="newTask.status" 
          class="px-6 py-4 bg-transparent outline-none text-gray-600 cursor-pointer md:w-40"
        >
          <option>To Do</option>
          <option>In Progress</option>
          <option>Done</option>
        </select>

        <button 
          type="submit" 
          class="m-2 px-8 py-3 bg-indigo-600 text-white font-semibold rounded-xl hover:bg-indigo-700 transition-all shadow-md hover:shadow-lg transform active:scale-95"
        >
          Add
        </button>
      </form>
    </div>

    <div v-if="tasks.length === 0" class="text-center py-20 bg-white rounded-3xl border border-dashed border-gray-300">
      <p class="text-gray-400 text-lg">No tasks yet. Add one above!</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      
      <div 
        v-for="task in tasks" 
        :key="task.id" 
        class="group bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between h-full"
      >
        
        <div v-if="editingId === task.id" class="space-y-3 animate-fade-in">
          <input v-model="editForm.title" class="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none text-sm font-bold" />
          <textarea v-model="editForm.description" rows="3" class="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none text-sm"></textarea>
          <select v-model="editForm.status" class="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm">
             <option>To Do</option>
             <option>In Progress</option>
             <option>Done</option>
          </select>
          <div class="flex gap-2 pt-2">
            <button @click="updateTask(task.id)" class="flex-1 bg-emerald-500 text-white py-2 rounded-lg text-sm font-medium hover:bg-emerald-600 transition">Save</button>
            <button @click="editingId = null" class="flex-1 bg-gray-100 text-gray-600 py-2 rounded-lg text-sm font-medium hover:bg-gray-200 transition">Cancel</button>
          </div>
        </div>

        <div v-else class="flex flex-col h-full">
          <div class="flex justify-between items-start mb-4">
            <h3 class="text-lg font-bold text-gray-800 leading-tight group-hover:text-indigo-600 transition-colors">
              {{ task.title }}
            </h3>
            <span :class="`px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(task.status)}`">
              {{ task.status }}
            </span>
          </div>
          
          <p class="text-gray-500 text-sm leading-relaxed mb-6 line-clamp-4 flex-grow">
            {{ task.description || 'No description provided.' }}
          </p>
          
          <div class="flex items-center justify-end gap-4 pt-4 border-t border-gray-50 mt-auto opacity-80 group-hover:opacity-100 transition-opacity">
            <button 
              @click="startEdit(task)" 
              class="flex items-center gap-1 text-sm font-medium text-gray-500 hover:text-indigo-600 transition-colors"
            >
              <span>Edit</span>
            </button>
            <button 
              @click="deleteTask(task.id)" 
              class="flex items-center gap-1 text-sm font-medium text-gray-500 hover:text-red-500 transition-colors"
            >
              <span>Delete</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Badge Color
const getStatusColor = (status) => {
  switch (status) {
    case 'Done':
      return 'bg-emerald-50 text-emerald-700 border border-emerald-100'; 
    case 'In Progress':
      return 'bg-blue-50 text-blue-700 border border-blue-100';
    default: 
      return 'bg-gray-100 text-gray-600 border border-gray-200';
  }
};

// CRUD
const tasks = ref([]);
const newTask = ref({ title: '', description: '', status: 'To Do' });
const editingId = ref(null);
const editForm = ref({});

const getAuthHeader = () => {
  return { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } };
};

const fetchTasks = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:5000/api/tasks', getAuthHeader());
    tasks.value = res.data;
  } catch (error) { console.error(error); }
};

const addTask = async () => {
  if (!newTask.value.title) return; // Validasi sederhana
  await axios.post('http://127.0.0.1:5000/api/tasks', newTask.value, getAuthHeader());
  newTask.value = { title: '', description: '', status: 'To Do' };
  fetchTasks();
};

const startEdit = (task) => {
  editingId.value = task.id;
  editForm.value = { ...task };
};

const updateTask = async (id) => {
  await axios.put(`http://127.0.0.1:5000/api/tasks/${id}`, editForm.value, getAuthHeader());
  editingId.value = null;
  fetchTasks();
};

const deleteTask = async (id) => {
  if(confirm('Are you sure you want to delete this task?')) {
    await axios.delete(`http://127.0.0.1:5000/api/tasks/${id}`, getAuthHeader());
    fetchTasks();
  }
};

const logout = () => {
  localStorage.removeItem('token');
  location.reload();
};

onMounted(fetchTasks);
</script>