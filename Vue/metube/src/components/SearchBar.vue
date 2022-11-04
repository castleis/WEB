<template>
  <div>
    <input type="text" @keyup.enter="searchVideo">
  </div>
</template>

<script>
import axios from 'axios'

const YOUTUBE_API_KEY = 'AIzaSyC61IAFX42wzEIwJagTJi5F_d7OQSOfEIQ'
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
    name: 'SearchBar',
    methods: {
      async searchVideo(event) {
        const keyword = event.target.value
        const config = {
          params: {
            zxpart: 'snippet',
            type: 'video',
            q: keyword,
            key: YOUTUBE_API_KEY,
          },
        }
        // console.log(config)
        const response = await axios.get(YOUTUBE_API_URL, config)
        const videoList = response.data.items
        console.log(videoList)
        this.$emit('search-video', videoList)
      }
    }
}
</script>

<style>

</style>