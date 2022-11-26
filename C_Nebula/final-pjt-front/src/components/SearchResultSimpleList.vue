<template>
  <div v-show="toggle">
    <SearchResultSimpleListItem
      v-for="movie in result_list"
      :key="movie.id"
      :movie="movie"
      @check-this-movie="checkThisMovie"
    />
  </div>
</template>

<script>
import SearchResultSimpleListItem from '@/components/SearchResultSimpleListItem'
export default {
  name: 'SearchResultList',
  props:{
    result_list: Array
  },
  data() {
    return {
      toggle : true
    }
  },
  watch: {
    result_list: function(value, oldvalue) {
      value, oldvalue
      this.toggle = true
    }
  },
  components: {
    SearchResultSimpleListItem,
  },
  methods:{
    checkThisMovie(context){
      this.$emit('check-this-movie', context)
      this.toggle = false
  }
}
}
</script>

<style>

</style>