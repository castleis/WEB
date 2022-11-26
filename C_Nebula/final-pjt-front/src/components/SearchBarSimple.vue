<template>
  <div>
    <div>
      <input @input="searchMovies" class="form-control me-2" type="search" placeholder="영화를 검색하세요" aria-label="Search">
    </div>
    <div>
      <SearchResultSimpleList
       :result_list="result_list"
       @check-this-movie="checkThisMovie"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchResultSimpleList from '@/components/SearchResultSimpleList'
export default {
  name: 'SearchBarSimple',
  data() {
    return {
      searchWord: null,
      result_list: null
    }
  },

  components: {
    SearchResultSimpleList
  },
  methods: {
    searchMovies(event) {
      const search_word = event.target.value.trim()
      if (search_word)
      axios({
        method: 'get',
        url: this.$store.state.URL + '/movies/search/',
        params: {
          search_word
        }
      }).
      then((res) => {
        this.result_list = res.data
      })
      .catch((err) => {
        this.result_list = null
        console.log(err)
      })
    },
    checkThisMovie(index) {
      this.$emit('check-this-movie', index)
    }
  }


}
</script>

<style>

</style>