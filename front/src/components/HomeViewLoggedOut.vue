<template>
    <div class="container fade-in">
        <h1 style="font-size: 60px;">Movies bring our adventures to life.</h1>
        <div class="g">
            <h4>Christopher Nolan</h4>
        </div>
        <div>
            <h3 style="font-size: 25px;">G-Flex is a service that recommends movies according to the user's preferred genres and moods.</h3>
        </div>
        <div>
            <!-- <h3>Made by </h3> -->
            <h3 style="font-size: 20px;">Made by Hyunwoo Koo and Gootea Kim</h3>
        </div>
        <div>
            <h3 style="font-size: 20px;">SSAFY 11th, Busan 1st class</h3>
        </div>
        <div>
            <h4>Busan, Republic of Korea</h4>
        </div>
    </div>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .fade-in {
      animation: fadeInAnimation 1s ease-in forwards;
  }
  
  @keyframes fadeInAnimation {
      from {
          opacity: 0;
      }
      to {
          opacity: 1;
      }
  }
  
  .g {
    margin-left: 600px;
  }
  
  .container {
      text-align: center;
      margin-top: 250px;
      font-family: Arial, sans-serif;
  }
  
  h1 {
      font-size: 45px;
      margin-bottom: 20px;
  }
  
  h3 {
      font-size: 20px;
      margin-bottom: 10px;
  }
  
  h4 {
      font-size: 16px;
      color: #888;
  }
  </style>
  