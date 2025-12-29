<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 font-sans antialiased transition-colors duration-300">
    
    <header class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 shadow-sm sticky top-0 z-10 transition-colors duration-300">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center text-white font-bold shadow-lg shadow-indigo-500/30">
            T
          </div>
          <h1 class="text-xl font-bold text-gray-800 dark:text-white tracking-tight">Task Manager</h1>
        </div>

        <button 
          @click="toggleTheme" 
          class="p-2 rounded-lg bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-yellow-400 hover:bg-gray-200 dark:hover:bg-gray-600 transition-all focus:outline-none focus:ring-2 focus:ring-indigo-500"
          aria-label="Toggle Dark Mode"
        >
          <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>

      </div>
    </header>

    <main class="py-10 transition-colors duration-300">
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
const isDark = ref(false);

// Logic Toggle Theme
const toggleTheme = () => {
  isDark.value = !isDark.value;
  updateThemeClass();
};

// Update Class di HTML tag dan simpan ke LocalStorage
const updateThemeClass = () => {
  if (isDark.value) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
};

// Cek preference saat pertama load
onMounted(() => {
  // Cek Login
  const token = localStorage.getItem('token');
  isLoggedIn.value = !!token;

  // Cek Theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true;
  } else {
    isDark.value = false;
  }
  updateThemeClass();
});

const checkLogin = () => {
  const token = localStorage.getItem('token');
  isLoggedIn.value = !!token;
};
</script>