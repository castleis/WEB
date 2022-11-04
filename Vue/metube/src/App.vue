<template>
  <div id="app">
    <h1>METUBE</h1>
    <SearchBar @search-video="searchVideo"/>
    <VideoList :videolist="videolist"/>
    <VideoPlay/>
  </div>
</template>

<script>
import VideoList from './components/VideoList.vue'
import SearchBar from './components/SearchBar.vue'
import VideoPlay from './components/VideoPlay.vue'

export default {
  name: 'App',
  components: {
    VideoList,
    SearchBar,
    VideoPlay
  },
  data: function () {
    return {
      videolist: [],
    }
  },
  methods: {
    searchVideo: function (videoList) {
      this.videolist = videoList
      // console.log(videoList)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
