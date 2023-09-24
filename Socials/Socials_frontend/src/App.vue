<template>
    <nav class="py-0 px-8 border-b border-gray-200">
      <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
          <div class="menu-left m-0">
            <router-link to="/" class="text-xl" ><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR04A6E62WnY6Ft2liarukRz4_GDXKGvtFn9yo_KnZEEowkcWZ0vqqQA0mt_Go7rhgQh4A&usqp=CAU" class="w-25 h-auto rounded" ></router-link>
          </div>
  
          <div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
            <router-link to="/feed" :class="{ 'text-blue-600': $route.name === 'feed' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
              </svg>
            </router-link>
  
            <router-link to="/chat" :class="{ 'text-blue-600': $route.name === 'chat' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
              </svg>
            </router-link>
  
            <router-link to="/search" :class="{ 'text-blue-600': $route.name === 'search' }">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
              </svg>
            </router-link>
          </div>
  
          <div class="menu-right ">
            <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                        <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10">
  <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z" />
</svg>

                        </RouterLink>
            </template>
  
            <template v-else>
              <router-link to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</router-link>
              <router-link to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</router-link>
            </template>
          </div>
        </div>
      </div>
    </nav>
  
    <main class="px-8 py-6 bg-gray-100">
      <router-view />
    </main>
  
    <Toast />
  </template>
  
  <script>
  import axios from 'axios'
  import Toast from '@/components/Toast.vue'
  import { useUserStore } from '@/stores/user'
  
  export default {
    setup() {
      const userStore = useUserStore()
  
      return {
        userStore
      }
    },
  
    components: {
      Toast
    },
  
    beforeCreate() {
      this.userStore.initStore()
  
      const token = this.userStore.user.access
  
      if (token) {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
      } else {
        axios.defaults.headers.common['Authorization'] = ''
      }
    }
  }
  </script>
  