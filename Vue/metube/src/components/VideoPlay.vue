<template>
  <div>
    <iframe :src="videoUrl" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
    name: 'VideoPlay',
    props: {
      selectedVideo: Object
    },
    computed: {
      videoUrl() {
        const videoId = this.selectedVideo.id.videoId
        return `https://https://www.youtube.com/embed/${videoId}`
      }
    }
}
</script>

<style>

</style>