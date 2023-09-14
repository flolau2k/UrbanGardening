<script setup lang="ts">
const props = defineProps({
  itemName: String,
  itemValue: [String, Date]
})

const formatDateTimeWithTimeZone = (date: Date) => {
  const offsetMinutes = date.getTimezoneOffset()

  const offsetHours = Math.abs(Math.floor(offsetMinutes / 60))
  const offsetMins = Math.abs(offsetMinutes % 60)
  const offsetSign = offsetMinutes > 0 ? '-' : '+'
  const offsetFormatted = `GMT ${offsetSign}${String(offsetHours).padStart(2, '0')}${String(
    offsetMins
  ).padStart(2, '0')}`

  const formattedDate = date.toLocaleDateString('en-US', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })

  return `${formattedDate} (${offsetFormatted})`
}
</script>

<template>
  <div class="flex gap-x-1 items-center mb-2">
    <div>
      <slot></slot>
    </div>
    <div class="w-[130px]">{{ props.itemName }}:</div>
    <div v-if="props.itemValue instanceof Date">
      {{ formatDateTimeWithTimeZone(props.itemValue) }}
    </div>
    <div v-else>
      {{ props.itemValue }}
    </div>
  </div>
</template>
