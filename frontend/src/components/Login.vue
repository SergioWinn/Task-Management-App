<template>
  <div class="flex items-center justify-center min-h-[80vh]">
    <div class="w-full max-w-sm bg-white dark:bg-gray-800 rounded-3xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden transition-all hover:shadow-2xl duration-300">
      
      <div class="px-8 pt-10 pb-6 text-center">
        <div class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-indigo-100 dark:bg-indigo-900 text-indigo-600 dark:text-indigo-300 mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white tracking-tight">Welcome Back</h2>
        <p class="text-gray-500 dark:text-gray-400 text-sm mt-2">Please enter your details to sign in.</p>
      </div>

      <form @submit.prevent="handleLogin" class="px-8 pb-10 space-y-5">
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wide mb-1.5 ml-1">Username</label>
            <input 
              v-model="username" 
              type="text" 
              required 
              placeholder="admin"
              class="w-full px-5 py-3 bg-gray-50 dark:bg-gray-700 border border-transparent dark:border-gray-600 rounded-xl focus:bg-white dark:focus:bg-gray-600 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all font-medium text-gray-700 dark:text-gray-200 placeholder-gray-400"
            >
          </div>

          <div>
            <label class="block text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wide mb-1.5 ml-1">Password</label>
            <input 
              v-model="password" 
              type="password" 
              required 
              placeholder="admin123"
              class="w-full px-5 py-3 bg-gray-50 dark:bg-gray-700 border border-transparent dark:border-gray-600 rounded-xl focus:bg-white dark:focus:bg-gray-600 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all font-medium text-gray-700 dark:text-gray-200 placeholder-gray-400"
            >
          </div>
        </div>

        <button 
          type="submit" 
          class="w-full py-3.5 px-4 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl shadow-lg shadow-indigo-500/30 transition-all transform active:scale-95 focus:ring-4 focus:ring-indigo-500/20"
        >
          Sign In
        </button>
        
        <div v-if="error" class="flex items-center gap-2 p-3 text-sm text-red-600 dark:text-red-300 bg-red-50 dark:bg-red-900/30 rounded-lg animate-pulse">
          {{ error }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const emit = defineEmits(['login-success']);
const username = ref('');
const password = ref('');
const error = ref('');

const handleLogin = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:5000/api/login', {
      username: username.value,
      password: password.value
    });
    localStorage.setItem('token', res.data.access_token);
    emit('login-success');
  } catch (err) {
    error.value = 'Invalid username or password';
    setTimeout(() => error.value = '', 3000);
  }
};
</script>