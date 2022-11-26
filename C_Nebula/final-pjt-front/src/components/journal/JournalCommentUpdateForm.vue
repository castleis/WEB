<template>
  <div>
    <form @submit.prevent="updateComment">
      <div class="mb-3">
        <textarea
        class="form-control"
        id="updateContent"
        rows="3"
        :value="content"
        ></textarea>
      </div>
      <div class="d-flex justify-content-end">
        <JournalCommentDeleteButton :comment_id="id" @update-comment-list="getCommentList"/>
        <button @click="updateToggle" class="btn btn-dark mx-3">수정 취소</button>
        <button type="submit" class="btn btn-dark">
          수정
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import JournalCommentDeleteButton from '@/components/journal/JournalCommentDeleteButton'
export default {
  name: "JournalCommentUpdateForm",
  components:{
    JournalCommentDeleteButton
  },

  props : {
    id: Number,
    content: String
  },
  methods: {
    updateComment() {
      const contentTag = document.querySelector('#updateContent')
      const content = contentTag.value
      axios({
        method: 'put',
        url: this.$store.state.URL + `/journal/${this.id}/comments/detail/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        contentTag.value = ''
        this.$emit('get-comment-list')
        this.$emit('update-toggle')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateToggle() {
      this.$emit('update-toggle')
    },
    getCommentList() {
      this.$emit('get-comment-list')
    }
      
    
  }
}
</script>

<style>

</style>