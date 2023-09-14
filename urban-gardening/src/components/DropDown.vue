<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import ChevronIcon from '../components/icons/ChevronIcon.vue'
import { DropDownData } from '../../types/DropDownData'

const props = defineProps<{
  data: Array<DropDownData>
  dropdownName: string
}>()
const emit = defineEmits<{
  (event: 'selected-item', payload: DropDownData): void
}>()

const isActive = ref<boolean>(false)
const selectedValue = ref<string | null>(null)
const dropdownRef = ref<HTMLDivElement | null>(null)

const toggleDropDown = (): void => {
  isActive.value = !isActive.value
}

const handleOutsideClick = (event: MouseEvent) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    isActive.value = false
  }
}

onMounted(() => { 
  document.addEventListener('click', handleOutsideClick)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleOutsideClick)
})

const emitDropdownItem = (item: DropDownData): void => {
  selectedValue.value = item.displayLabel
  emit('selected-item', item)
  toggleDropDown()
}
</script>

<template>
  <div class="relative" ref="dropdownRef">
    <button
      @click="toggleDropDown"
      :title="selectedValue ? selectedValue : dropdownName"
      class="text-white z-10 w-36 hover:bg-green-800 bg-green-600 focus:outline-none font-medium rounded-lg text-sm px-3 py-1.5"
    >
      <div class="flex items-center justify-between gap-x-4">
        <div class="truncate">
          {{ selectedValue ? selectedValue : dropdownName }}
        </div>
        <div>
          <ChevronIcon :class="`ease-in-out duration-200 ${isActive ? 'rotate-180' : ''}`" />
        </div>
      </div>
    </button>

    <!-- Dropdown menu -->
    <div v-if="isActive" class="text-black top-9 absolute w-36 h-40 z-30">
      <div class="py-1 text-sm bg-white rounded-lg border border-green-500 overflow-y-auto">
        <div v-if="props.data?.length > 0">
          <div v-for="(item, index) in props.data" :key="item.id">
            <div
              :title="item.displayLabel"
              @click="emitDropdownItem(item)"
              :class="`${
                index == props.data.length - 1 ? '' : 'border-b border-gray-200'
              } block px-2 py-1 dark:hover:bg-gray-200 cursor-pointer truncate`"
            >
              {{ item.displayLabel }}
            </div>
          </div>
        </div>
        <div class="text-center p-1" v-else>No items</div>
      </div>
    </div>
  </div>
</template>
