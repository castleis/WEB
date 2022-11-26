<template>
  <div class="m-3 shadow-lg p-3 mb-5 bg-body rounded">
    <br>
    <h3 class="d-flex justify-content-start">한 줄 평</h3>
    <form @submit.prevent="createReview">
      <div class="mb-3">
        <star-rating v-model="rank" :increment=0.5 :animate="true" :glow="5"  active-color="#f001"></star-rating>
      </div>
      <div class="row">
        <div class="col-8 mb-3">
          <textarea
          class="form-control"
          id="content"
          rows="3"
          placeholder="리뷰 내용을 입력하세요"
          v-model="content"
          ></textarea>
        </div>
      </div>
      <span class="d-flex justify-content-end">
        <button type="submit" class="btn btn-primary">
          작성
        </button>
      </span>
    </form>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
// import StarRanking from '@/components/StarRanking'
import axios from 'axios'
export default {
  name: "MovieReviewCreateForm",
  components:{
    // StarRanking,
    StarRating,
  },
  data() {
    return {
      // title: "",
      content: "",
      rank : 0,
      movie_id : this.$route.params.movie_id,
    };
  },
  methods: {
    createReview() {
      // const title = this.title
      const content = this.content
      const rank = this.rank * 2
      // let form = new FormData()
      // form.append('content', content)
      // form.append('rank', rank)
      axios({
        method: 'post',
        url: this.$store.state.URL + `/movies/${this.movie_id}/review/create/`,
        data: { content, rank },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({name: 'movieDetail', params: {movie_id: this.movie_id}})
      })
      .then(() => {
          axios({
            method: 'get',
            url: this.$store.state.URL + `/movies/${this.movie_id}/review/`
          })
          .then((res) => {
            this.content = null
            return res.data
          })
          .then((data) => {
            this.$emit('movie-review-list', data)
          })

          .catch((err) => {
          console.log(err)
          })
        })
      .catch((err) => {
        if (err.response.data.detail === "Invalid token.") {
          alert('로그인 후에 작성해주세요~')
        }
      })
    },
    starRanking(rank) {
      this.rank = rank

      
    }
  },
};
</script>



<style>
.modal {
  background-color: #000000;
}
</style>