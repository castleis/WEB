<template>
  <div>
    <MovieList :my_movies="my_movies"/>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'

export default {
  name: 'MyMovie',
  props: {
    my_movies: Array
  },

  components: {
    MovieList
  },
  methods: {

  },
  created() {
    return
  }
}
</script>

<style>

</style>