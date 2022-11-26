<template>
  <div>
    <div>
      <p>베스트 한줄평!</p>
      <MovieReviewListItem
      style="box-shadow: 5px 10px 20px yellow;" 
      v-for="movie_review of computed_best_movie_review_list" 
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
  name: 'BestMovieReviewList',
  props: {
    movie_id: Number,
    best_movie_review_list: Array
  },
  components: {
    MovieReviewListItem
  },
  computed: {
    computed_best_movie_review_list() {
      return this.best_movie_review_list
    }
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
    },
    likeReview(id) {
      this.$emit('like-review', id)

  }
}
}
</script>

<style>

</style>