<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
      <!-- Main Left Section -->
      <div class="main-left col-span-1">
        <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
            
            <img :src="user.get_avatar" class="mb-6 rounded-full">
          <p class="text-lg font-semibold">{{ user.name }}</p>
          <div class="mt-6 flex justify-center items-center">
  <p class="text-sm text-gray-600">{{ user.postsCount }} posts</p>
</div>
          <div class="mt-6">
            <button
              v-if="shouldShowSendMessageButton"
              class="bg-blue-500 p-3 rounded text-white"
              @click="sendDirectMessage"
            >
              Send Direct Message
            </button>
            <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-blue-800  text-white rounded-lg text-lg" 
                        to="/profile/edit"
                        v-if="userStore.user.id === user.id"
                    >
                        Edit profile
                    </RouterLink>
            
                    <button 
                        class="inline-block py-4 px-3 bg-red-600  text-white rounded-lg text-lg" 
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                    >
                        Log out
                    </button>
          </div>
        </div>
      </div>
  
      <!-- Main Center Section -->
      <div class="main-center col-span-3 space-y-4">
        <div
          class="bg-white border border-gray-200 rounded-lg p-4"
          v-if="isCurrentUser"
        >
          <form @submit.prevent="submitForm" method="post">
            <textarea
          v-model="body"
          class="w-full p-4 bg-gray-100 rounded-lg resize-y border-2 focus:border-blue-600  active:border-blue-600 border-blue-500" 
          placeholder="What are you thinking about?"
        ></textarea>
            <div class="flex justify-between items-center mt-4">
              <a href="#" class="p-4 rounded-full text-white bg-blue-500"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
</svg>
</a>
              <button class="p-4 rounded-full text-white bg-blue-500"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
</svg>
</button>
            </div>
          </form>
        </div>
  
        <div
          class="bg-white border border-gray-200 rounded-lg p-4"
          v-for="post in posts"
          :key="post.id"
        >
          <FeedItem :post="post" />
        </div>
      </div>
  
      <!-- Main Right Section -->
     
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
  import Trends from '../components/Trends.vue';
  import FeedItem from '../components/FeedItem.vue';
  import { useUserStore } from '@/stores/user';
  import { useToastStore } from '@/stores/toast';
  
  export default {
    name: 'FeedView',
  
    setup() {
      const userStore = useUserStore();
      const toastStore = useToastStore();
  
      return {
        userStore,
        toastStore,
      };
    },
  
    components: {
      PeopleYouMayKnow,
      Trends,
      FeedItem,
    },
  
    data() {
      return {
        posts: [],
        user: {
          id: null,
          postsCount: 0,
        },
        body: '',
      };
    },
  
    computed: {
      isCurrentUser() {
        return this.userStore.user.id === this.user.id;
      },
      shouldShowSendMessageButton() {
        return this.isCurrentUser ? false : true;
      },
    },
  
    watch: {
      '$route.params.id': {
        handler: 'getFeed',
        deep: true,
        immediate: true,
      },
    },
  
    methods: {
      sendDirectMessage() {
        console.log('sendDirectMessage');
  
        axios
          .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
          .then(response => {
            console.log(response.data);
  
            this.$router.push('/chat');
          })
          .catch(error => {
            console.log('error', error);
          });
      },
  
      getFeed() {
        axios
          .get(`/api/posts/profile/${this.$route.params.id}/`)
          .then(response => {
            console.log('data', response.data);
  
            this.posts = response.data.posts;
            this.user = {
              ...response.data.user,
              postsCount: response.data.posts.length,
            };
          })
          .catch(error => {
            console.log('error', error);
          });
      },
  
      submitForm() {
        console.log('submitForm', this.body);
  
        axios
          .post('/api/posts/create/', {
            body: this.body,
          })
          .then(response => {
            console.log('data', response.data);
  
            this.posts.unshift(response.data);
            this.body = '';
            this.user.postsCount++;
          })
          .catch(error => {
            console.log('error', error);
          });
      },
  
      logout() {
        console.log('Log out');
  
        this.userStore.removeToken();
  
        this.$router.push('/login');
      },
    },
  };
  </script>
  