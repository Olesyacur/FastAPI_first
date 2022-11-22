<template>
  <div>
    Я, {{ name }} <span id="curDT"></span>,обещаю бросить курить в 45 лет.
    <br>
    _______________/{{ name }}/
  </div>
  <div style="margin-top: 20px;">
    <input type="text" v-model="name">
    <input type="submit" value="Установить имя">
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
</script>