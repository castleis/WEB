<template>
  <div class="row">
    <p v-if="result_list !== 0">
      <span>
        {{theWord}}에 대한 검색 결과
      </span>
      <span>
        ({{result_list.length}} 건)
      </span>
    </p>
    <MovieListItem
      v-for="movie in result_list"
      :key="movie.id"
      :movie="movie"
      @check-this-movie="checkThisMovie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem'
export default {
  name: 'SearchResultList',
  props:{
    result_list: Array,
    searchWord: String
  },
  computed : {
    theWord() {
      return this.searchWord
    }
  },
  components: {
    MovieListItem,
  },
  methods: {
    checkThisMovie(index) {
      this.$emit('check-this-movie', index)
    }
  }
}
</script>

<style>

</style>