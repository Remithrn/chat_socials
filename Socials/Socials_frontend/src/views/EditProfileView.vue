<template>
    <div class="max-w-7xl mx-auto">
      <div class="main-right m-auto">
        <div class="p-8 bg-white border border-gray-200 rounded-lg">
          <form @submit.prevent="submitForm" class="space-y-6">
            <!-- Name Input -->
            
        <p class="text-lg font-semibold text-center">Edit</p>
            <div>
              <label for="name">Name</label>
              <input
                id="name"
                type="text"
                v-model="form.name"
                placeholder="Your full name"
                class="w-full mt-2 p-4 border border-gray-200 rounded-lg"
              >
            </div>
  
            <!-- Email Input -->
            <div>
              <label for="email">E-mail</label>
              <input
                id="email"
                type="email"
                v-model="form.email"
                placeholder="Your e-mail address"
                class="w-full mt-2 p-4 border border-gray-200 rounded-lg"
              >
            </div>
  
            <!-- Avatar Input -->
            <div>
              <label for="avatar">Avatar</label>
              <input
                id="avatar"
                type="file"
                ref="file"
                accept="image/*"
                class="w-full mt-2 p-4 border border-gray-200 rounded-lg"
              >
            </div>
  
            <!-- Display Errors -->
            <template v-if="errors.length > 0">
              <div class="bg-red-300 text-white rounded-lg p-4">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>
            </template>
  
            <!-- Save Button -->
            <div>
              <button
                class="py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
              >
                Save changes
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { useToastStore } from '@/stores/toast'
  import { useUserStore } from '@/stores/user'
  
  export default {
    setup() {
      const toastStore = useToastStore()
      const userStore = useUserStore()
  
      return {
        toastStore,
        userStore,
      }
    },
  
    data() {
      return {
        form: {
          email: this.userStore.user.email,
          name: this.userStore.user.name,
        },
        errors: [],
      }
    },
  
    methods: {
      submitForm() {
        this.errors = []
  
        if (this.form.email === '') {
          this.errors.push('Your e-mail is missing')
        }
  
        if (this.form.name === '') {
          this.errors.push('Your name is missing')
        }
  
        if (this.errors.length === 0) {
          let formData = new FormData()
          formData.append('avatar', this.$refs.file.files[0])
          formData.append('name', this.form.name)
          formData.append('email', this.form.email)
  
          axios
            .post('/api/editprofile/', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              },
            })
            .then(response => {
              if (response.data.message === 'information updated') {
                this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')
  
                this.userStore.setUserInfo({
                  id: this.userStore.user.id,
                  name: this.form.name,
                  email: this.form.email,
                  avatar: response.data.user.get_avatar,
                })
  
                this.$router.back()
              } else {
                this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
              }
            })
            .catch(error => {
              console.log('error', error)
            })
        }
      },
    },
  }
  </script>
  