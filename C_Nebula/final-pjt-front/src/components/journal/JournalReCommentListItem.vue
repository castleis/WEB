<template>
  <div>
    <div style="border: 2px;" v-if="!to_update" class="ms-5 shadow p-3 mb-5 mt-3 bg-body rounded">
      <p class="d-flex justify-content-start" style="font-size:13px;"><router-link :to="{ name: 'profile', params: { 'user_id' : `${user_id}`} }">{{ nickname }}</router-link>님의 대댓글 :</p>
      <p>{{ content }}</p>
      <p>{{ created_at }}</p>
      <span class="d-flex justify-content-end" v-if="is_me">
        <button @click="updateToggle" class="btn btn-dark">수정</button>
      </span>
    </div>
    <!-- 대댓글 수정폼 -->
    <div v-if="to_update" class="ms-5 shadow p-3 mb-5 bg-body rounded">
      <JournalCommentUpdateForm
      :id="comment_id" 
      :content="content"
      @get-comment-list="updateCommentList"
      @update-toggle="updateToggle"
      />
    </div>
  </div>
</template>

<script>


import JournalCommentUpdateForm from '@/components/journal/JournalCommentUpdateForm'
export default {
  name: 'JournalReCommentListItem',
  props: {
    comment: Object,
  },
  components: {
    JournalCommentUpdateForm
  },
  data() {
    return {
      to_update : false
    }
  },
  
  computed: {
    comment_id() {
      return this.comment.id
    },
    user_id() {
      return this.comment.user
    },
    created_at() {
      return this.comment.created_at.substring(0, 10)
    },
    content() {
      return this.comment.content
    },
    nickname() {
      return this.comment.nickname
    },
    is_me() {
      if (this.user_id === this.$store.state.user_id) {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    updateCommentList() {
      this.$emit('update-comment-list')
    },
    updateToggle() {
      this.to_update = !this.to_update
    }
  }

}
</script>

<style>

</style>