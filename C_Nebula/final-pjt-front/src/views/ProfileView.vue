<template>
  <div>
    <img class="back" :src="backgroundImg" alt="">
    <div class="profile">
      <h1>{{user_info.nickname}}님의 프로필</h1>
      <div>
        <!-- 회원정보 수정 -->
        <ProfileBanner :user_id="Number(user_id)" 
        @update-follow="updateFollow"
        :is_followed="is_followed"
        />
      </div>
      <hr>
      <p>Point : {{ user_info.ranking }}</p>
      <p>followers : {{follower_list.length}} / followings : {{following_list.length}}</p>
    </div>
    
    <!-- 팔로워 / 팔로잉 목록 -->
    <div class="container">
      <div class="row">
        <h3>팔로워</h3>
        <MiniProfile v-for="follower in follower_list" :key="follower.id" :profile="follower" class="shadow p-3 mb-5 bg-body rounded"/>
        <p v-if="follower_list.length === 0"> 팔로워가 없습니다...</p>
      </div>
      <div class="row">
        <h3>팔로잉</h3>
        <MiniProfile v-for="following in following_list" :key="following.id" :profile="following" class="shadow p-3 mb-5 bg-body rounded"/>
        <p v-if="following_list.length === 0"> 팔로잉이 없습니다...</p>
      </div>
      
      <div class="my_journal">
        <h2>작성한 저널</h2>
        <JournalList :journalList="journalList"/>
        <p v-if="!journalList">작성한 저널이 없습니다...</p>
      </div>
      <div>
        <h2>좋아요한 영화</h2>
        <MyMovie :my_movies="my_movies"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import JournalList from '@/components/journal/JournalList'
import ProfileBanner from '@/components/profile/ProfileBanner'
import MyMovie from '@/components/profile/MyMovie'
import MiniProfile from '@/components/profile/MiniProfile'

export default {
  name: 'ProfileView',
  components: {
    JournalList,
    ProfileBanner,
    MyMovie,
    MiniProfile
  },
  data() {
    return {
      journalList: null,
      user_id: this.$route.params.user_id,
      follower_list: [],
      following_list: [],
      user_info: null
    }
  },
  computed: {
    is_followed () {
      const follower_id_list = this.follower_list.map((elem) => elem.id)
      
      if (follower_id_list.includes(this.$store.state.user_id)) {
        return true
      } else {
        return false
      }
    },
    backgroundImg() {
      const img = require('@/assets/background/galaxycat5.jpg')
      return img
    },
    my_movies() {
      return this.$store.getters.moviesList
    }
  },
  methods: {
    updateFollow() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/profile/${this.user_id}/follower/list/`,
      })
      .then((res) => {
        this.follower_list = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateFollowing() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/profile/${this.user_id}/following/list/`,
    })
    .then((res) => {
      this.following_list = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  },
  updateJounal() {
    axios({
      method: 'get',
      url: this.$store.state.URL + `/journal/${this.user_id}/profile/`
    })
    .then((res) => {
      this.journalList = res.data
    })
    .then((err) => console.log(err))
  },
  getProfile() {
    axios({
      method: 'get',
      url: this.$store.state.URL + `/profile/${this.user_id}/`,
    })
    .then((res) => {
      this.user_info = res.data
    })
    .catch((err) => console.log(err))
  },
  getMyMovies() {
      this.$store.dispatch('getMyMovies', this.user_id)

    }

  },
  beforeRouteUpdate(to, from, next) {
        this.user_id = to.params.user_id
        this.updateFollow()
        this.updateFollowing()
        this.updateJounal()
        this.getProfile()
        this.getMyMovies()
        next()
    },
  created() {
    this.updateFollow()
    this.updateFollowing()
    this.updateJounal()
    this.getProfile()
    this.getMyMovies()

  },
}

</script>

<style>
.back{
  width: 120%;
  height: auto;
  content: "";
  overflow: hidden;
  background-position: center;
  background-repeat : no-repeat;
  opacity: 40%;
  top: -20rem;
  left: -15rem;
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
.profile{
  margin: 10%;
  text-align: left;
}
.my_journal{
  margin-top: 3%;
}
/* body {
  height: 100vh;
  width: 100vw;
  background-image: url('@/assets/background/galaxycat5.jpg');
  background-repeat : no-repeat;
  background-size : cover;
  background: linear-gradient(
    to left top,
    rgba(225, 225, 225, 0) 70%,
    rgba(225, 225, 225, 0.5) 80%
    rgba(225, 225, 225, 0.75) 90%
    rgba(225, 225, 225) 100%
  );
} */
/* body {
    background: linear-gradient(-45deg, #ffffff, #000000, #ffffff, #000000);
    background-size: 100% 100%;
    animation: gradient 10s ease infinite;
    height: 100vh;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
} */

</style>