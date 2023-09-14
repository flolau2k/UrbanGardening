<template>
  <div class="camera">
    <div class="camera-square" style="backgroundimage: url('../src/assets/navbar-logo.png')">
      <div class="camera-buttons">
        <button class="camera-button" @click="takePhoto">Take Photo</button>
        <button class="camera-button" @click="startTimelapse">Timelapse</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'

export default defineComponent({
  name: 'CameraComponent',
  setup() {
    const image = ref('')

    const takePhoto = () => {
      // Code to take photo and update image variable with the new photo
    }

    const startTimelapse = () => {
      // Code to start timelapse and download it
    }

    return {
      image,
      takePhoto,
      startTimelapse
    }
  }
})
</script>

<style>
.camera {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.camera-square {
  position: relative;
  width: 300px;
  height: 300px;
  background-size: cover;
  background-position: center;
}

.camera-buttons {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: rgba(16, 141, 243, 0);
}

.camera-button {
  margin: 0 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #9fe2d5a0;
  color: #333;
  font-size: 16px;
  cursor: pointer;
}
</style>
