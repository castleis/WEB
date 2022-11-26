<template>
  <div>
    
    <JournalCommentListItem 
      v-for="comment in commentList"
      :key="comment.id"
      :comment="comment"
      :journal_id="journal_id"
      @like-comment-update="likeCommentUpdate"
      @get-comment-list="getCommentList"

    />
  </div>
</template>

<script>
import JournalCommentListItem from '@/components/journal/JournalCommentListItem'
export default {
  name: 'JournalCommentList',
  props: {
    commentList: Array,
    journal_id: Number
  },
  components: {
    JournalCommentListItem
  },
  methods: {
    likeCommentUpdate() {
      this.$emit('like-comment-update')
    },
    getCommentList() {
      this.$emit('get-comment-list')
    },


  }
}
</script>

<style>

</style>