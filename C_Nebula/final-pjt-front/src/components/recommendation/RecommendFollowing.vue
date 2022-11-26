<template>
  <div>
    <!-- <div v-if="followRecommendList"> -->
      <h1>팔로워들의 추천영화!</h1>
      <MovieListItem 
      v-for="movie in followRecommendList"
      :key="movie.pk"
      :movie="movie"
      />
    </div>
  <!-- </div> -->
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem';
export default {
  name:'RecommendFollowing',
  props: {
    followRecommendList: Array
  },
  components: {
    MovieListItem,
  },
}
</script>

<style>

</style>