<template>
  <div class="min-h-screen bg-gray-50 text-gray-900 font-sans antialiased">
    
    <header class="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-10">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center text-white font-bold">
            T
          </div>
          <h1 class="text-xl font-bold text-gray-800 tracking-tight">Task Manager</h1>
        </div>
      </div>
    </header>

    <main class="py-10">
      <Login v-if="!isLoggedIn" @login-success="checkLogin" />
      <TaskManager v-else />
    </main>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Login from './components/Login.vue';
import TaskManager from './components/TaskManager.vue';

const isLoggedIn = ref(false);

const checkLogin = () => {
  const token = localStorage.getItem('token');
  isLoggedIn.value = !!token;
};

onMounted(checkLogin);
</script>