<script setup lang="ts">
import UserIcon from './icons/UserIcon.vue';
import { ref } from 'vue';

const isActive = ref<Boolean>(true);

</script>

<template>
    <div class="background-color w-60 p-4 text-white shadow-md h-screen relative">
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


<style>
.background-color {
    background: linear-gradient(107deg, rgb(13, 198, 180) 8.1%, rgb(33, 198, 138) 79.5%);
    /* background: linear-gradient(180deg, #00cdac 0%, #8ddad5 100%); */
    /* background: linear-gradient(20deg, rgb(224, 235, 213) 8.1%, rgb(37, 148, 141) 91.2%); */
}
</style>