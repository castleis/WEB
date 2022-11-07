<template>
  <div id="app">
    <h1>METUBE</h1>
    <SearchBar @search-video="searchVideo"/>
    <VideoList :videoList="videoList" @on-click-video="onClickVideo"/>
    <VideoPlay :selectedVideo="selectedVideo"/>
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
  data() {
    return {
      videoList: [],
      selectedVideo: null,
    }
  },
  methods: {
    searchVideo(videoList) {
      this.videoList = videoList
    },
    onClickVideo(video) {
      this.selectedVideo = video
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
