<script setup lang="ts">
import { ref } from 'vue';
import ChevronIcon from "../components/icons/ChevronIcon.vue";
import { DropDownData } from '../../types/DropDownData';

const props = defineProps<{ 
    data: Array<DropDownData>,
    dropdownName: String,
  }>();
const emit = defineEmits<{
  (event: 'customClick', payload: DropDownData): void;
}>();

const isActive = ref<boolean>(false);

const toggleDropDown = (): void => {
  isActive.value = !isActive.value;
}

const emitDropdownItem = (item: DropDownData): void => {
  emit("customClick", item);
  toggleDropDown();
}

</script>

<template>
<div class="z-20 relative">
  <button @click="toggleDropDown" class="text-white hover:bg-green-800 bg-green-600 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5">
    <div class="flex items-center gap-x-4">
      <div>
        {{ dropdownName }}
      </div>
      <div>
        <ChevronIcon :class="`ease-in-out duration-200 ${isActive ? 'rotate-180' : ''}`" />
      </div>
    </div> 
  </button>
  
  <!-- Dropdown menu -->
  <div v-if="isActive" id="dropdown" class="text-black top-11 absolute h-40 z-10 shadow w-44">
    <div class="py-2 text-sm bg-white rounded-lg">
      <div  v-if="props.data?.length > 0">
        <div v-for="item in props.data" :key="item.id">
          <div @click="emitDropdownItem(item)" class="block px-4 py-2 dark:hover:bg-gray-200 cursor-pointer">{{ item.itemName }}</div>
        </div>
      </div>
      <div v-else>
        No items to display!
      </div>
    </div>
  </div>
</div>
</template>
