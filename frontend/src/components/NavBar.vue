<script setup lang="ts"></script>

<template>
  <div class="w-full py-2 px-10 text-white h-14 border-b fixed z-50 bg-[#03c8a8]">
    <div class="w-full flex items-center">
      <div class="flex flex-grow gap-x-2 items-center">
        <img class="w-10 h-10 rounded-full" src="/src/assets/navbar-logo.png" />
        <router-link to="/dashboard" class="font-bold">Urban Gardening</router-link>
      </div>
      <router-link to="/profile">
        <div class="flex gap-x-1 items-center">
          <img src="/src/assets/login-picture.png" class="h-10 w-10 rounded-full" />
          <div>User</div>
        </div>
      </router-link>
    </div>
  </div>
</template>
