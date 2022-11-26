<template>
  <div>
    <!-- <div class="container" v-if="is_genre"> -->
      <h1>좋아하는 장르에서 인기있는 영화들이예요!</h1>
      <MovieListItem 
      v-for="movie in genreRecommendList"
      :key="movie.pk"
      :movie="movie"
      />
    </div>
  <!-- </div> -->
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem';
export default {
  name: 'RecommendGenre',
  props: {
    genreRecommendList: Array
  },
  components: {
    MovieListItem,
  },
  computed: {
    is_genre() {
      if (this.genreRecommendList.length() === 0) {
        return false
      } else {
        return true
      }
    }
  },
}
</script>

<style>

</style>