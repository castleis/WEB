<template>
  <div>
    <JournalReCommentListItem 
      v-for="comment in recommentList"
      :key="comment.id"
      :comment="comment"
      @update-comment-list="updateCommentList"
    />
  </div>
</template>

<script>
import JournalReCommentListItem from '@/components/journal/JournalReCommentListItem'
export default {
  name: 'JournalCommentList',
  props: {
    recommentList: Array
  },
  components: {
    JournalReCommentListItem
  },
  methods: {
    updateCommentList() {
      this.$emit('update-comment-list')

    }
  }
}
</script>

<style>

</style>