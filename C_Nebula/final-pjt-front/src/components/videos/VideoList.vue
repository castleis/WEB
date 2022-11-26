<template>
  <div class="container">
    <div class="row">

      <VideoListItem
      v-for="video in video_list"
      :key="video.id.videoId"
      :video="video"
      @open-modal="openModal"
      />
      <VideoModal @close="closeModal" v-if="modal" :nowPlayingUrl="nowPlayingUrl">
        <!-- default 슬롯 콘텐츠 -->
        <!-- /default -->
        <!-- footer 슬롯 콘텐츠 -->
        <template slot="footer">
        </template>
        <!-- /footer -->
      </VideoModal>
    </div>
      
  </div>
</template>

<script>
import VideoModal from '@/components/videos/VideoModal'
import VideoListItem from "@/components/videos/VideoListItem"
export default {
  name: 'VideoList',
  props:{
    video_list: Array
  },
  components: {
    VideoListItem,
    VideoModal
  },
  data() {
    return {
      modal : false,
      nowPlayingUrl : null
    }
  },
  methods:{
    openModal(data) {
        this.modal = data.modal
        this.nowPlayingUrl = data.url
      },
      closeModal() {
        this.modal = false
      },
}
}
</script>

<style>

</style>