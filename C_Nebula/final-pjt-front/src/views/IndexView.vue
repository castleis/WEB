<template>
  <div>
    <img class="index" :src="backgroundImg" alt="">
    <div class="animated-title" style="background-color: black; height:20px">
      <div class="track " >
      <div class="content" style="color: yellow; padding-top: 30px; font-family: 'DungGeunMo';">
        <!-- 여기에 흐를 문자 넣기 -->
        <!-- <span class="mx-4">
          우주고양이!!
        </span> -->
        <span class="mx-4">
          1위 : {{powerUser1.nickname}} {{powerUser1.ranking}}점
        </span >
        <span class="mx-4">
          2위 : {{powerUser2.nickname}} {{powerUser2.ranking}}점
        </span>
        <span class="mx-4">
          3위 : {{powerUser3.nickname}} {{powerUser3.ranking}}점
        </span>
        <span class="mx-4">
          1위 : {{powerUser1.nickname}} {{powerUser1.ranking}}점
        </span >
        <span class="mx-4">
          2위 : {{powerUser2.nickname}} {{powerUser2.ranking}}점
        </span>
        <span class="mx-4">
          3위 : {{powerUser3.nickname}} {{powerUser3.ranking}}점
        </span>
        <!-- <span class="mx-4">
          우주고양이!!
        </span> -->
        <span class="mx-4">
          1위 : {{powerUser1.nickname}} {{powerUser1.ranking}}점
        </span >
        <span class="mx-4">
          2위 : {{powerUser2.nickname}} {{powerUser2.ranking}}점
        </span>
        <span class="mx-4">
          3위 : {{powerUser3.nickname}} {{powerUser3.ranking}}점
        </span>
        <!-- <span><router-link :to="{ name: 'profile', params: { 'user_id' : `${powerUser1.user}`} }">{{powerUser1.nickname}}</router-link></span>&nbsp;
        <span><router-link :to="{ name: 'profile', params: { 'user_id' : `${powerUser2.user}`} }">{{powerUser2.nickname}}</router-link></span>&nbsp;
        <span><router-link :to="{ name: 'profile', params: { 'user_id' : `${powerUser3.user}`} }">{{powerUser3.nickname}}</router-link></span>&nbsp; -->
      </div>
    </div>
  </div>
    <div class="SM">
      <h1 style="font-size: 5rem; text-shadow:2px 2px 2px #000; font-family: 'hyunygothic'; color: yellow;" class="d-flex justify-content-center mb-3">C_Nebula</h1>
      <SearchMovies/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchMovies from '@/components/SearchMovies'
import _ from 'lodash'
export default {
  name: 'IndexView',
  components: {
    SearchMovies,
  },
  data() {
    return {
      powerUser1: {},
      powerUser2: {},
      powerUser3: {},
    }
  },
  computed: {
    backgroundImg() {
      const num = _.sample(_.range(2,12))
      const img = require(`@/assets/background/galaxycat${num}.jpg`)
      return img
    }
  },
  methods: {
    getUserRanking() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/profile/user_ranking/`
      })
      .then((res) => {
        this.powerUser1 = res.data[0]
        this.powerUser2 = res.data[1]
        this.powerUser3 = res.data[2]
      })
      .catch((err) => console.log(err))
    }
  },
  created() {
      this.getUserRanking()
    }
  
  // methods: {
  //   getAll() {
  //     this.$store.dispatch('getAll')
  //   }
  // },
  // created() {
  //   this.getAll()
  // }
}
</script>

<style>
.index{
  width: 120%;
  height: auto;
  content: "";
  overflow: hidden;
  background-position: center;
  background-repeat : no-repeat;
  opacity: 40%;
  top: -5%;
  left: -10%;
  z-index: -1;
  position: absolute;
  background: linear-gradient(
    to bottom,
    rgba(225, 225, 225, 0) 70%,
    rgba(225, 225, 225, 0.5) 80%
    rgba(225, 225, 225, 0.75) 90%
    rgba(225, 225, 225) 100%
    );
  background-size: cover;
}
.SM {
  margin: 5%;
}
/* 움직이는 텍스트 */
.animated-title {font-size:30px; font-family:'Raleway',Sans-serif; font-weight:300; position: relative; width: 100%;max-width:100%; height: auto; padding:20px 0; overflow-x: hidden; overflow-y: hidden;}
.animated-title .track {position: absolute; white-space: nowrap;will-change: transform;animation: marquee 60s linear infinite; }
@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
@media (hover: hover) and (min-width: 700px){
.animated-title .content {-webkit-transform: translateY(calc(100% - 8rem)); transform: translateY(calc(100% - 8rem));}
    }
</style>