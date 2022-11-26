<template>
  <!-- <div class="container flex-direction-column" :style="`background-image:url(${backdrop_path})`"> -->
    <!-- <div class="card" > -->
      <!-- <div class="card-body"> -->
      <div class="container">
        <div class="row g-0">
          <div class="col-8">
            <div class="row g-0 d-flex justify-content-between">
              <div class="col-8">
                <!-- <h1>DetailView</h1> -->
                <div>
                  <h1 style="font-size: 2rem;">{{ movie_detail.title }}</h1>
                  <p>({{ movie_detail.original_title }})</p>
                  <!-- <p v-if="!(movie_detail.title===movie_detail.original_title)">({{ movie_detail.original_title }})</p> -->
                </div>
              </div>
              <div class="col-3 mt-3" style="font-size: 2rem;">
                <span @click="likeMovie">
                  <i class="bi bi-heart" v-if="!is_like"></i>
                  <i class="bi bi-heart-fill" v-if="is_like"></i>
                </span>
                <span>  {{movie_detail.like_users.length}}</span>
              </div>
            </div>
            <hr class="col-12">
            <p>개봉일 : {{ movie_detail.release_date }}</p>
            <!-- <p>관람객 수 : {{ movie_detail.popularity}}</p> -->
            <p>상영 시간 : {{ movie_detail.runtime}}</p>
            <p>장르 : {{ movie_detail.genre_names[0].name }}</p>
            <hr class="col-12">
            <VideoList :video_list="video_list"/>
          </div>
          <div class="col-4">
            <img :src="`https://image.tmdb.org/t/p/w500/${movie_detail.poster_path}`" alt="" class="img-fluid m-3 poster">
          </div>
        </div>
        <p class="overview">{{movie_detail.overview}}</p>
        <hr>
        
        <!-- </div> -->
        <MovieReviewCreateForm @movie-review-list="getReviewList"/>
        <BestMovieReviewList 
        :movie_id="Number(movie_id)" 
        :best_movie_review_list="best_movie_review_list"
        @delete-review="deleteReview"
        @update-review="updateReview"
        @like-review="likeReview"/>
        <MovieReviewList 
        :movie_id="Number(movie_id)" 
        :movie_review_list="movie_review_list"
        @delete-review="deleteReview"
        @update-review="updateReview"
        @like-review="likeReview"/>
      </div>
        <!-- </div> -->
  <!-- </div> -->
</template>

<script>
import "bootstrap-icons/font/bootstrap-icons.css"
import axios from 'axios'

import MovieReviewList from '@/components/MovieReviewList'
import BestMovieReviewList from '@/components/BestMovieReviewList'
import MovieReviewCreateForm from '@/components/movies/MovieReviewCreateForm'
import VideoList from '@/components/videos/VideoList'

export default {
  name: 'MovieDetailView',
  components: {
    MovieReviewList,
    MovieReviewCreateForm,
    VideoList,
    BestMovieReviewList,
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id,
      movie_detail: null,
      movie_review_list: null,
      backdrop_path: null,
      video_list: null,
      best_movie_review_list: null
    }
      
    },
    computed: {
      is_like() {
      if (this.movie_detail.like_users.includes(this.$store.state.user_id)) {
        return true
      } else {
        return false
      }
    }
  },
  
  
  methods: {
    // TODO: 나중에 부트스트랩 적용 전에, res.data를 항목 별로 분리해서 저장하기
    getDetail() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/movies/${this.movie_id}/`
      })
      .then((res) => {
        this.movie_detail = res.data
        this.backdrop_path = `https://image.tmdb.org/t/p/original/${res.data.backdrop_path}`

        // 영상 가져오기
        axios({
          method: 'get',
          url: 'https://www.googleapis.com/youtube/v3/search',
          params: {
            key: "AIzaSyA5wZLzqNgXy5Nx6NGndHWlpD06NWVSeSE",
            part: 'snippet',
            q: `${this.movie_detail.title}`,
            maxResult: 3,
            type: 'video',
            videoDuration: 'short'
        },
        })
        .then((res) => {
          this.video_list = res.data.items.slice(0, 3)
        })
        .catch((err) => console.log(err))

      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviewList() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/movies/${this.movie_id}/review/`
      })
      .then((res) => {
        this.movie_review_list = res.data
        axios({
        method: 'get',
        url: this.$store.state.URL + `/movies/${this.movie_id}/bestreview/`
        })
        .then((res) => {
        this.best_movie_review_list = res.data
        })

        .catch((err) => {
          console.log(err)

      })
      })

      .catch((err) => {
        console.log(err)

      })
    },

    // movieReviewList(data) {
    //   this.movie_review_list = data
    // },
    deleteReview(id) {
      axios({
        method: 'delete',
        url: this.$store.state.URL + `/movies/review/${id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.getReviewList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 리뷰 업데이트
    updateReview(context) {
      axios({
        method: 'put',
        url: this.$store.state.URL + `/movies/review/${Number(context.id)}/`,
        data: {
          // id: context.id,
          content: context.content,
          rank: context.rank,
          movie: this.movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.getReviewList()
      })
      
      .catch((err) => {
        console.log(err)
      })
    },
    likeReview(id) {
      axios({
        method: 'post',
        url: this.$store.state.URL + `/movies/review/${id}/review_likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {

          this.getReviewList()
        })
        .catch((err) => console.log(err))

    },
    likeMovie() {
      axios({
        method: 'post',
        url: this.$store.state.URL + `/movies/${this.movie_id}/movie_likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.getDetail()
        })
        .catch((err) => console.log(err))
    }
  },
  created() {
      this.getDetail()
      this.getReviewList()
    },

}
</script>

<style>
.container {
  background-size: cover;
  padding: 20px;
}
.background-image{
  opacity: 70%;
}
.overview{
  padding: 10px;
}

.poster{
  width: 100%;
  height: 100%;
}
</style>