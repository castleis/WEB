<template>
  <div>
    <h1>이번주 C_Nebula의 인기 영화는 어떠신가요?</h1>
    <MovieListItem 
    v-for="movie in weeklyRecommendList"
    :key="movie.pk"
    :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem';
export default {
  name: 'RecommendHot',
  props: {
    weeklyRecommendList: Array
  },
  components: {
    MovieListItem,
  }
}
</script>

<style>

</style>