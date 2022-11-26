<template>
  <div class="container">
    <h1>평점이 높은 영화 소개드려요!</h1>
    <MovieListItem 
    v-for="movie in voteRecommendList"
    :key="movie.pk"
    :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem';
export default {
  name: 'RecommendVote',
  props: {
    voteRecommendList: Array
  },
  components: {
    MovieListItem,
  }
}
</script>

<style>

</style>