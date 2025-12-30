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
              placeholder="Enter your username"
              class="w-full px-5 py-3 bg-gray-50 dark:bg-gray-700 border border-transparent dark:border-gray-600 rounded-xl focus:bg-white dark:focus:bg-gray-600 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all font-medium text-gray-700 dark:text-gray-200 placeholder-gray-400"
            >
          </div>

          <div>
            <label class="block text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wide mb-1.5 ml-1">Password</label>
            <div class="relative">
              <input 
                v-model="password" 
                :type="showPassword ? 'text' : 'password'" 
                required 
                placeholder="Enter your password"
                class="w-full px-5 py-3 pr-12 bg-gray-50 dark:bg-gray-700 border border-transparent dark:border-gray-600 rounded-xl focus:bg-white dark:focus:bg-gray-600 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/10 outline-none transition-all font-medium text-gray-700 dark:text-gray-200 placeholder-gray-400"
              >
              
              <button 
                type="button" 
                @click="showPassword = !showPassword"
                class="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors focus:outline-none"
              >
                <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3l18 18M10.5 10.677a2.121 2.121 0 002.823 2.823M7.362 7.362A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.542 7-.302.966-.802 1.882-1.49 2.71m-2.35 2.35A9.956 9.956 0 0112 19c-4.478 0-8.268-2.943-9.542-7a9.953 9.953 0 011.49-2.71" />
                </svg>
              </button>
            </div>
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
const showPassword = ref(false);

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