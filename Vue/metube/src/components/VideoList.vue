<template>
  <div v-if="videolist.length">
    <VideoListItem 
      v-for="video in videolist"
      :video="video"
      :key="video.id.videoId"
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
      videolist: Array
    }
}
</script>

<style>

</style>