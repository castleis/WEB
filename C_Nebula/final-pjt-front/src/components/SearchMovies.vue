<template>
  <div>
    <div>
      <input @input="searchMovies" class="form-control me-2" type="search" placeholder="영화 검색" aria-label="Search">
    </div>
    <div>
      <SearchResultList :result_list="result_list" :searchWord="searchWord"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchResultList from '@/components/SearchResultList'
export default {
  name: 'SearchMovies',
  data() {
    return {
      searchWord: null,
      result_list: null
    }
  },
  components: {
    SearchResultList
  },
  methods: {
    searchMovies(event) {
      const search_word = event.target.value.trim()
      this.searchWord = search_word

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
    }
  }


}
</script>

<style>

</style>