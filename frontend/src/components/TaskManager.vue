<template>
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
      <div>
        <h2 class="text-3xl font-bold text-gray-900 dark:text-white tracking-tight">My Tasks</h2>
        <p class="text-gray-500 dark:text-gray-400 mt-1">Organize your daily jobs and projects.</p>
      </div>
      <button 
        @click="logout" 
        class="px-5 py-2 text-sm font-medium text-red-600 dark:text-red-400 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl hover:bg-red-50 dark:hover:bg-red-900/20 transition-all shadow-sm"
      >
        Sign Out
      </button>
    </div>

    <div class="bg-white dark:bg-gray-800 rounded-2xl p-1 shadow-sm border border-gray-200 dark:border-gray-700 mb-8 transition-colors hover:shadow-md">
      <form @submit.prevent="addTask" class="flex flex-col md:flex-row gap-0 md:gap-2">
        <input v-model="newTask.title" placeholder="What needs to be done?" required class="flex-1 px-6 py-4 bg-transparent outline-none text-gray-700 dark:text-gray-200 placeholder-gray-400 font-medium" />
        <div class="w-px bg-gray-200 dark:bg-gray-700 my-2 hidden md:block"></div>
        <input v-model="newTask.description" placeholder="Add details..." class="flex-1 px-6 py-4 bg-transparent outline-none text-gray-600 dark:text-gray-300 placeholder-gray-400" />
        <div class="w-px bg-gray-200 dark:bg-gray-700 my-2 hidden md:block"></div>
        <select v-model="newTask.status" class="px-6 py-4 bg-transparent outline-none text-gray-600 dark:text-gray-300 cursor-pointer md:w-40 bg-none">
          <option class="dark:bg-gray-800">To Do</option>
          <option class="dark:bg-gray-800">In Progress</option>
          <option class="dark:bg-gray-800">Done</option>
        </select>
        <button type="submit" class="m-2 px-8 py-3 bg-indigo-600 text-white font-semibold rounded-xl hover:bg-indigo-700 transition-all shadow-md hover:shadow-lg transform active:scale-95">Add</button>
      </form>
    </div>

    <div class="flex flex-col sm:flex-row gap-4 mb-6">
      <div class="relative flex-1 group">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="h-5 w-5 text-gray-400 group-focus-within:text-indigo-500 transition-colors" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
          </svg>
        </div>
        <input 
          v-model="searchQuery" 
          type="text" 
          placeholder="Search tasks by title..." 
          class="block w-full pl-10 pr-3 py-2.5 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl leading-5 text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all shadow-sm"
        >
      </div>

      <div class="relative min-w-[180px]">
        <select 
          v-model="filterStatus" 
          class="block w-full pl-4 pr-10 py-2.5 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl leading-5 text-gray-700 dark:text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all shadow-sm appearance-none cursor-pointer"
        >
          <option value="">All Status</option>
          <option value="To Do">To Do</option>
          <option value="In Progress">In Progress</option>
          <option value="Done">Done</option>
        </select>
        <div class="absolute inset-y-0 right-0 flex items-center px-3 pointer-events-none text-gray-500">
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>
      </div>
    </div>

    <div v-if="filteredTasks.length === 0" class="text-center py-16 bg-white dark:bg-gray-800 rounded-3xl border border-dashed border-gray-300 dark:border-gray-700">
      <div v-if="tasks.length === 0">
        <p class="text-gray-400 text-lg">No tasks yet. Start by adding one!</p>
      </div>
      <div v-else>
        <p class="text-gray-400 text-lg">No tasks found matching your search.</p>
        <button @click="clearFilters" class="mt-2 text-indigo-600 hover:text-indigo-500 font-medium">Clear filters</button>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div 
        v-for="task in filteredTasks" 
        :key="task.id" 
        class="group bg-white dark:bg-gray-800 rounded-2xl p-6 border border-gray-100 dark:border-gray-700 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between h-full"
      >
        <div v-if="editingId === task.id" class="space-y-3 animate-fade-in">
          <input v-model="editForm.title" class="w-full px-4 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none text-sm font-bold" />
          <textarea v-model="editForm.description" rows="3" class="w-full px-4 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg text-gray-900 dark:text-white focus:ring-2 focus:ring-indigo-500 outline-none text-sm"></textarea>
          <select v-model="editForm.status" class="w-full px-4 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg text-gray-900 dark:text-white text-sm">
             <option class="dark:bg-gray-800">To Do</option>
             <option class="dark:bg-gray-800">In Progress</option>
             <option class="dark:bg-gray-800">Done</option>
          </select>
          <div class="flex gap-2 pt-2">
            <button @click="updateTask(task.id)" class="flex-1 bg-emerald-500 text-white py-2 rounded-lg text-sm font-medium hover:bg-emerald-600 transition">Save</button>
            <button @click="editingId = null" class="flex-1 bg-gray-100 dark:bg-gray-600 text-gray-600 dark:text-gray-200 py-2 rounded-lg text-sm font-medium hover:bg-gray-200 dark:hover:bg-gray-500 transition">Cancel</button>
          </div>
        </div>

        <div v-else class="flex flex-col h-full">
          <div class="flex justify-between items-start mb-4">
            <h3 class="text-lg font-bold text-gray-800 dark:text-gray-100 leading-tight group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
              {{ task.title }}
            </h3>
            <span :class="`px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(task.status)}`">
              {{ task.status }}
            </span>
          </div>
          <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed mb-6 line-clamp-4 flex-grow">
            {{ task.description || 'No description provided.' }}
          </p>
          <div class="flex items-center justify-end gap-4 pt-4 border-t border-gray-50 dark:border-gray-700 mt-auto opacity-80 group-hover:opacity-100 transition-opacity">
            <button @click="startEdit(task)" class="text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Edit</button>
            <button @click="deleteTask(task.id)" class="text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-red-500 dark:hover:text-red-400 transition-colors">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'; // Import computed
import axios from 'axios';

// --- SEARCH & FILTER LOGIC ---
const searchQuery = ref('');
const filterStatus = ref(''); // Default kosong (All)

// Computed Property: Memfilter tasks secara real-time
const filteredTasks = computed(() => {
  return tasks.value.filter(task => {
    // 1. Cek kecocokan Title (Case Insensitive)
    const matchesSearch = task.title.toLowerCase().includes(searchQuery.value.toLowerCase());
    // 2. Cek kecocokan Status
    const matchesFilter = filterStatus.value === '' || task.status === filterStatus.value;
    
    return matchesSearch && matchesFilter;
  });
});

const clearFilters = () => {
  searchQuery.value = '';
  filterStatus.value = '';
};

// --- LOGIC LAINNYA (SAMA SEPERTI SEBELUMNYA) ---
const getStatusColor = (status) => {
  switch (status) {
    case 'Done': return 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300 border border-emerald-100 dark:border-emerald-800'; 
    case 'In Progress': return 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 border border-blue-100 dark:border-blue-800';
    default: return 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-600';
  }
};

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
  if (!newTask.value.title) return;
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