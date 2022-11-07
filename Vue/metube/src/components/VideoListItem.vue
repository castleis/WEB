<template>
  <div id="listItem" @click="onClickVideo">
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
        video: Object,
    },
    computed: {
        videoTitle() {
            // console.log(this.video)
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
    methods: {
        onClickVideo() {
            this.$emit('on-click-video', this.video)
        }
    }
}
</script>

<style>
.listItem{
    border: 2px solid orange;
}
</style>