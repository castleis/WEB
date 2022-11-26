<template>
  <div @click="checkThisMovie" @mouseover="isMouse" @mouseout="isMouse" :class="{'onMouse':is_mouse}">
    <p>{{ title }}</p>
  </div>
</template>

<script>
export default {
  name: 'SearchResultSimpleListItem',
  props:{
    movie : Object,
  },
  data() {
    return{
      index : this.movie.id,
      title : this.movie.title,
      poster : "https://image.tmdb.org/t/p/w200/" + this.movie.poster_path,
      is_mouse : false
    }
  },
  methods: {
    checkThisMovie() {
      this.$emit('check-this-movie', {title: this.title, index: this.index, poster: this.poster})

    },
    isMouse() {
      this.is_mouse = !this.is_mouse
    }
  }
}
</script>

<style>
  .onMouse {
    background-color: blue;
    color: white
  }
</style>