<template>
  <div>
    <img :src="thumbUrl" alt="">
    <h3>{{ videoTitle | unescape }}</h3>
    <p>{{ videoDesc }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'VideoListItem',
    props: { 
        video: Object
    },
    computed: {
        videoTitle() {
            console.log(this.video)
            return this.video.snippet.title
        },
        videoDesc() {
            return this.video.snippet.description
        },
        thumbUrl() {
            return this.video.snippet.thumbnails.medium.url
        },
    },
    filters: {
        unescape(rawText) {
            return _.unescape(rawText)
        }
    },
}
</script>

<style>

</style>