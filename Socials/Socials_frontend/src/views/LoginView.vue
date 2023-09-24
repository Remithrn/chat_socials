<template>


    
    <div class="min-h-screen bg-gray-900 py-6 flex flex-col justify-center sm:py-12">
  <div class="relative py-3 sm:max-w-xl sm:mx-auto">
    <div class="absolute inset-0 bg-gradient-to-r from-blue-300 to-blue-600 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
    </div>
    <div class="relative px-4 py-10 bg-gray-800 text-white shadow-lg sm:rounded-3xl sm:p-20">
        <form  v-on:submit.prevent="submitForm" class="max-w-md mx-auto">
        <div>
          <h1 class="text-2xl font-semibold">Login</h1>
        </div>
        <div class="divide-y divide-gray-700">
          <div class="py-8 text-base leading-6 space-y-4 text-gray-300 sm:text-lg sm:leading-7">
            <div class="relative">
                <input type="email" v-model="form.email" 
                class="peer placeholder-transparent h-10 w-full bg-gray-800 text-white border-b-2 border-gray-600 focus:outline-none focus:border-blue-400"
                placeholder="Email address" />
              <label for="email"
                class="absolute left-0 -top-3.5 text-gray-500 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-300 peer-focus:text-sm">Email
                Address</label>
            </div>
            <div class="relative">
                <input type="password" v-model="form.password"
                class="peer placeholder-transparent h-10 w-full bg-gray-800 text-white border-b-2 border-gray-600 focus:outline-none focus:border-blue-600"
                placeholder="Password" />
              <label for="password"
                class="absolute left-0 -top-3.5 text-gray-500 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-300 peer-focus:text-sm">Password</label>
            </div>
            <div class="relative">
              <button class="bg-blue-500 text-white rounded px-3 py-2">Submit</button>
              <template v-if="errors.length > 0">
                        <div class="bg-red-500 mt-2 text-white rounded-xl p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>
              <p class="font-bold pt-2">
                Don't have an account? <RouterLink :to="{'name': 'signup'}"
                  class="underline text-blue-300">Click here</RouterLink> to create one!
              </p>
              
            </div>
          </div>
        </div>
    </form>
    </div>
  </div>
</div>


</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        console.log(response.data.access)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
                
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>