<template>
  <div>
    <div class="container">
      <div class="row">
        <MovieListItem v-for="movie in moviesList" :key="movie.pk" :movie="movie" class="col-md"/>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue';
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    moviesList() {
      return this.$store.getters.moviesList
    }
  },
}
</script>

<style>

</style>