<template>
    <div class="status-square">
        <div class="status-line">
            <i class="fas fa-leaf"></i>
            <span class="status-text">Plants: {{ numPlants }}</span>
        </div>
        <div class="status-line">
            <i class="fas fa-tint"></i>
            <span class="status-text">Water: {{ waterLevel }}</span>
        </div>
        <div class="status-line">
            <i class="fas fa-sun"></i>
            <span class="status-text">Sunlight: {{ sunlightLevel }}</span>
        </div>
        <div class="status-line">
            <i class="fas fa-thermometer-half"></i>
            <span class="status-text">Temperature: {{ temperature }}°C</span>
        </div>
        <div class="status-line">
            <i class="fas fa-clock"></i>
            <span class="status-text">Last Updated: {{ lastUpdated }}</span>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'StatusSquare',
    props: {
        numPlants: {
            type: Number,
            required: false
        },
        waterLevel: {
            type: Number,
            required: false
        },
        sunlightLevel: {
            type: Number,
            required: false
        },
        temperature: {
            type: Number,
            required: false
        },
        lastUpdated: {
            type: String,
            required: false
        }
    }
});
</script>

<style scoped>
.status-square {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 150px;
    height: 150px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.status-line {
    display: flex;
    align-items: center;
    margin: 5px;
}

.status-line i {
    margin-right: 10px;
    color: #4caf50;
}

.status-text {
    font-size: 14px;
    color: #333;
}
</style>
