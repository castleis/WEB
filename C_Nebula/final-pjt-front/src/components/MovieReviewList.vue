<template>
  <div>
    <div>
      <p>한줄평</p>
      <MovieReviewListItem 
      v-for="movie_review of computed_movie_review_list" 
      :key="movie_review.id"
      :movie_review="movie_review"
  
      @delete-review="deleteReview"
      @update-review="updateReview"
      @like-review="likeReview"/>
    </div>
  </div>
</template>

<script>
import MovieReviewListItem from '@/components/MovieReviewListItem'


export default {
  name: 'MovieReviewList',
  components: {
    MovieReviewListItem
  },
  props: {
    movie_id: Number,
    movie_review_list: Array,
  },
  computed: {
    computed_movie_review_list() {
      return this.movie_review_list
    },
  },
  methods: {
    movieReviewList(data) {
      this.$emit('movie-review-list', data)
    },
    deleteReview(id) {
      this.$emit('delete-review', id)
    },
    updateReview(context) {
      this.$emit('update-review', context)
      console.log('MovieReviewList')
    },
    likeReview(id) {
      this.$emit('like-review', id)

  }
}
}
</script>

<style>

</style>