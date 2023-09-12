<template>
    <div class="status-square">
        <div class="status-line">
            <i class="fas fa-leaf"></i>
            <span class="status-text">Plant: {{ kindPlants }}</span>
        </div>
        <div class="status-line">
            <i class="fas fa-tint"></i>
            <span class="status-text">Water: {{ waterLevel }}%</span>
        </div>
        <div class="status-line">
            <i class="fas fa-tint"></i>
            <span class="status-text">pH: {{ ph }}</span>
        </div>
        <div class="status-line">
            <i class="fas fa-sun"></i>
            <span class="status-text">Total dissolved solids: {{ waterConductivity*0.64 }}(ppm)</span>
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
    justify-content: left;
    align-items: left;
    width: 300px;
    height: 250px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(28, 107, 176, 0.2);
}

.status-line {
    display: flex;
    align-items: left;
    margin: 5px;
}

.status-line i {
    margin-right: 10px;
    color: #47b2d6;
}

.status-text {
    font-size: 14px;
    color: #101010;
}
</style>
