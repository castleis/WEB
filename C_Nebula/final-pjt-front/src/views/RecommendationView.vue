<template>
  <div class="recommendations">
    <div class="container">
      <RecommendHot :weeklyRecommendList="weeklyRecommendList" class="row"/>
    </div>
    <div class="container">
      <RecommendFollowing :followRecommendList="followRecommendList" class="row"/>
    </div>
    <div class="container">
      <RecommendGenre :genreRecommendList="genreRecommendList" class="row"/>
    </div>
    <div class="container">
      <RecommendVote :voteRecommendList="voteRecommendList" class="row"/>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import RecommendFollowing from '@/components/recommendation/RecommendFollowing'
import RecommendGenre from '@/components/recommendation/RecommendGenre'
import RecommendVote from '@/components/recommendation/RecommendVote'
import RecommendHot from '@/components/recommendation/RecommendHot'

export default {
  name: 'RecommendationView',
  components: {
    RecommendFollowing,
    RecommendGenre,
    RecommendVote,
    RecommendHot
  },
  data() {
    return {
      voteRecommendList : null,
      genreRecommendList: null,
      followRecommendList: null,
      weeklyRecommendList: null,
      
    }
  },
  methods:{
    getAllRecommend() {
      axios({
        method: 'get',
        url: this.$store.state.URL + '/movies/recommend/my_genres/',
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {

        this.genreRecommendList = res.data

      })
      .catch((err) => console.log(err))
      axios({
        method: 'get',
        url: this.$store.state.URL + '/movies/recommend/my_followings/',
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {

        this.followRecommendList = res.data
      })
      .catch((err) => console.log(err))
      axios({
        method: 'get',
        url: this.$store.state.URL + '/movies/recommend/vote_average/',
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.voteRecommendList = res.data
      })
      .catch((err) => console.log(err))
      axios({
        method: 'get',
        url: this.$store.state.URL + '/movies/recommend/weekly_hot/',
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.weeklyRecommendList = res.data
      })
      .catch((err) => console.log(err))

    }
  },
  created() {
    this.getAllRecommend()
  }
}
</script>

<style>
.recommendations{
  margin-top: 5%;
}
</style>