<script setup lang="ts">
import UserIcon from './icons/UserIcon.vue';
import { ref } from 'vue';

const isActive = ref<Boolean>(true);

</script>

<template>
  <div class="w-full py-2 px-10 text-white h-14 border-b fixed">
    <div class="w-full flex items-center">
      <div class="flex flex-grow gap-x-2 items-center">
          <img class="w-10 h-10 rounded-full" src="../assets/navbar-logo.png" />
          <router-link to="/" class="font-bold">Urban Gardening</router-link>
      </div>
        <router-link to="/profile">
          <div class="text-lg hover:underline ease-in-out duration-300">Profile</div>
      </router-link>
    </div>
  </div>
</template>
<!-- <template>
    <div class="background-color w-60 p-4 text-white shadow-md h-screen relative">
      <div class="flex flex-col">
          <div class="w-full text-center">
            <div class="flex gap-x-2 items-center">
                <img class="w-10 h-10 rounded-full" src="../assets/navbar-logo.png" />
                <router-link to="/" class="font-bold">Urban Gardening</router-link>
            </div>
              <div class="bg-white my-5 w-full" style="height: 1px;"></div>
              <router-link to="/profile" class="flex gap-x-5 items-center group">
                <div>
                    <UserIcon class="w-5 h-5 text-white" />
                </div>
                <div class="inline-block group-hover:underline">Profile</div>
            </router-link>
          </div>
      </div>
    </div>
</template> -->


<style>
.background-color {
  background-color: #03c8a8;
  /* background-image: linear-gradient(315deg, #89d8d3 0%, #03c8a8 74%); */
    /* background: linear-gradient(107deg, rgb(13, 198, 180) 8.1%, rgb(33, 198, 138) 79.5%); */
    /* background: linear-gradient(180deg, #00cdac 0%, #8ddad5 100%); */
    /* background: linear-gradient(20deg, rgb(224, 235, 213) 8.1%, rgb(37, 148, 141) 91.2%); */
}
</style>