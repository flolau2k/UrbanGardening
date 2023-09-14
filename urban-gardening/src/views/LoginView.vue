<script setup lang="ts">
import { useRouter } from 'vue-router';
import CustomButton from '../components/CustomButton.vue';
import CustomInput from '../components/CustomInput.vue';

const router = useRouter();

const login = (): void => {
  router.push('/');
}

</script>
<template>
    <div class="flex justify-center items-center w-full h-full">
      <div class="w-1/2 h-1/2 bg-white rounded-lg grid grid-cols-2">
        <div
          class="col-span-1 bg-center bg-cover rounded-l-lg" 
          style="background-image: url('../../src/assets/login-picture.png')">
        </div>

        <div class="flex justify-center col-span-1 pt-5">
          <div>
            <div class="text-4xl font-bold text-center text-teal-600">
              Urban Gardening
            </div>
            <div class="pt-10">
              <div>
                <CustomInput label="Username" input-type="text" :is-required="true" />
              </div>
              <div class="pt-5">
                <CustomInput label="Password" input-type="password" :is-required="true" />
              </div>
            </div>
            <div class="pt-10 pb-2 w-full flex justify-center">
              <div class="w-40">
                <CustomButton @customClick="login" button-name="Login" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
