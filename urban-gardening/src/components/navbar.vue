<template>
    <nav class="navbar">
        <div class="navbar-left">
            <h1 class="navbar-title">My App</h1>
        </div>
        <div class="navbar-middle">
            <img class="navbar-logo" src="/path/to/logo.png" alt="Logo" />
        </div>
        <div class="navbar-right">
            <CustomButton buttonName="Admin" @customClick="loginAsAdmin"></CustomButton>
        </div>
    </nav>
</template>


<script>
import CustomButton from '@/components/CustomButton.vue';
export default {
    components: {
        CustomButton,
    },
    methods: {
        loginAsAdmin() {
            alert('You are now logged in as admin');
        },
    },
};
</script>

<style lang="postcss">
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";

.navbar {
    @apply flex justify-between items-center bg-green-500 p-4;
}

.navbar-left {
    @apply flex-1;
}

.navbar-middle {
    @apply flex-1 flex justify-center;
}

.navbar-logo {
    @apply h-12;
}

.navbar-right {
    @apply flex-1 flex justify-end;
}

.navbar-admin-button {
    @apply bg-white text-green-500 border-none px-4 py-2 rounded cursor-pointer;
}
</style>
