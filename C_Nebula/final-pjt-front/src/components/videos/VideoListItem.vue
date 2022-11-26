<template>
  <div class="col-4 m-0">
    <img :src="video.snippet.thumbnails.default.url" alt="thumnail" @click="openModal" >
    <!-- <div>
      <iframe width="640" height="360" :src="nowPlayingUrl" ></iframe>
    </div> -->
    
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
 
  computed: {
    nowPlayingUrl () {
      return 'https://www.youtube.com/embed/' + this.video.id.videoId
  },
  submitData() {
    return {
      modal: true,
      url: this.nowPlayingUrl
    }
  }
},

  methods: {
    openModal () {
      this.$emit('open-modal', this.submitData )
      console.log(this.submitData)
    }
  }
}


</script>

<style>

</style>