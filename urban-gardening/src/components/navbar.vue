<script setup lang="ts">
import UserIcon from './icons/UserIcon.vue';
import ArrowIcon from "./icons/ArrowIcon.vue";
import { ref } from 'vue';

const isActive = ref<Boolean>(true);

const toggleNavbar = () => {
    isActive.value = !isActive.value
}
</script>

<template>
    <div :class="isActive ? 'w-60' : 'w-20'" class="bg-green-500 p-4 text-white shadow-md h-screen relative transition-width duration-200">
    <div @click="toggleNavbar" class="absolute -right-3 bg-green-500 rounded-full p-1 border">
        <ArrowIcon :class="`w-4 h-4 text-light duration-300 ease-in-out ${isActive ? '' : '-rotate-180'}`" />
    </div>
      <div class="flex flex-col">
          <div class="w-full text-center">
            <div class="flex gap-x-2 items-center">
                <img class="w-10 h-10 rounded-full" src="../assets/navbar-logo.png" />
                <a href="/" :class="`${isActive ? 'visible': 'invisible'} font-bold`">Urban Gardening</a>
            </div>
              <div class="bg-white my-5 w-full" style="height: 1px;"></div>
              <a href="/" class="flex gap-x-5 items-center group">
                <div>
                    <UserIcon class="w-5 h-5 text-white" />
                </div>
                <div :class="isActive ? 'inline-block group-hover:underline' : 'invisible'">Profile</div>
            </a>
          </div>
      </div>
    </div>
</template>
