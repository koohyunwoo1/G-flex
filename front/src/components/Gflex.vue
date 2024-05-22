<template>
      <div class="welcome-section content-hidden">
        <div class="content-wrap">
          <RouterLink :to="{ name: 'HomeView' }">
            <ul class="fly-in-text">
              <li>G</li>
              <li>-</li>
              <li>F</li>
              <li>L</li>
              <li>E</li>
              <li>X</li>
            </ul>
          </RouterLink>
        </div>
      </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

onMounted(() => {
  const welcomSection = document.querySelector('.welcome-section');
  setTimeout(() => {
    welcomSection.classList.remove('content-hidden');
  }, 800);
});

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

body {
  font-weight: 700;
}

.welcome-section {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: #000;
  overflow: hidden;
}

.content-wrap {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.fly-in-text {
  list-style: none;
  font-family: sans-serif;
}

.fly-in-text li {
  display: inline-block;
  margin-right: 20px;
  font-size: 10em;
  color: #87CEEB;
  opacity: 1;
  transition: all 2s ease;
}

.fly-in-text li:nth-child(5) {
  margin-right: 0;
}

.content-hidden .fly-in-text li,
.content-hidden .enter-button {
  opacity: 0;
}

.content-hidden .fly-in-text li:nth-child(1) {
  transform: translate3d(-60000px, 0, 0);
}

.content-hidden .fly-in-text li:nth-child(2) {
  transform: translate3d(0, 0, 0);
}

.content-hidden .fly-in-text li:nth-child(3) {
  transform: translate3d(-10000px, -20000px, 0);
}

.content-hidden .fly-in-text li:nth-child(4) {
  transform: translate3d(-15000px, 20000px, 0);
}

.content-hidden .fly-in-text li:nth-child(5) {
  transform: translate3d(6000px, -9000px, 0);
}
.content-hidden .fly-in-text li:nth-child(6) {
  transform: translate3d(-15000px, 9000px, 0);
}

.content-hidden .enter-button {
  transform: translate3d(0, -30px, 0);
}
</style>
