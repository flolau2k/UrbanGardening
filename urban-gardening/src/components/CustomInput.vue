<script setup lang="ts">

let localValue: String  = " ";

const emitInput = () => {
  console.log(localValue);
} 

defineProps({
  name: String,
  label: String,
  isRequired: Boolean,
  inputType: String,

})

</script>

<template>
  <div class="relative w-full">
  <input
   autocomplete="off"
   :name="name"
   v-model="localValue"
   :type="inputType"
   @input="emitInput"
   :id="label"
   class="block px-2.5 pb-2.5 pt-4 w-full text-light bg-transparent rounded-lg border-2 border-gray-400 appearance-none focus:outline-none focus:ring-0 focus:border-green-600 peer text-white"
   placeholder=""
/>
    <label
      for={{label}}
      class="absolute text-gray-400 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-darkBlack px-2 peer-focus:px-2 peer-focus:text-green-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 left-1"
    >
      {{label}}
    </label>
  </div>
</template>
