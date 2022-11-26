<template>
  <div>
    <form @submit.prevent="createComment">
      <div class="mb-3">
        <textarea
          class="form-control"
          id="content"
          rows="3"
          placeholder="대댓글 내용을 입력하세요"
          v-model="content"
        ></textarea>
      </div>
      <span class="d-flex justify-content-end">
        <button type="button" @click="toggleRecomment" class="btn btn-secondary mx-3"> 댓글 작성 취소</button>
        <button type="submit" class="btn btn-secondary">
          작성
        </button>
      </span>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "JournalReCommentCreateForm",
  components:{
  },
  data() {
    return {
      content: "",
      commentList: null,
    };
  },
  props : {
    comment_id: Number,
    journal_id: Number
  },
  methods: {
    createComment() {
      const content = this.content

      axios({
        method: 'post',
        url: this.$store.state.URL + `/journal/${this.journal_id}/${this.comment_id}/recomments/create/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.content = null
        this.$emit('get-re-comment-list')
        this.toggleRecomment()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    toggleRecomment() {
      this.$emit('toggle-recomment')
    }
      
    
  }
}
</script>

<style>

</style>