<template>
  <div class="inner ">
    <div class="star-rating d-flex justify-content-center">
      <div class="star" v-for="index in 5" :key="index" @click="check(index)">
        <span v-if="index < score">★</span>
        <span v-if="index >= score">☆</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "starRanking",
  data() {
    return {
      score: 0,
    };
  },
  methods: {
    check(index) {
      this.score = index + 1
      this.$emit('star-ranking', this.score - 1)
    },
  },
};
</script>

<style>
</style>