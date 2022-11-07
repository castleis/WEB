<template>
  <div id="list">
    <VideoListItem 
      v-for="video in videoList"
      :key="video.id.videoId"
      :video="video"
      @on-click-video="onClickVideo"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
    name: 'VideoList',
    components: {
      VideoListItem
    },
    props: {
      videoList: Array
    },
    methods: {
      onClickVideo() {
        this.$emit('on-click-video', this.video)
      }
    }
}
</script>

<style>

</style>