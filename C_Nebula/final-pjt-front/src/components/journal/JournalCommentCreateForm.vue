<template>
  <div>
    <form @submit.prevent="createComment">
      <div class="mb-3">
        <label for="content" class="form-label">댓글 작성</label>
        <textarea
          class="form-control"
          id="content"
          rows="3"
          placeholder="리뷰 내용을 입력하세요"
          v-model="content"
        ></textarea>
      </div>
      <div class="d-flex justify-content-end">
        <button type="submit" class="btn btn-secondary">
          작성
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "JournalCommentCreateForm",
  components:{
  },
  data() {
    return {
      content: "",
      commentList: null,
    };
  },
  props : {
    id: Number
  },
  methods: {
    createComment() {
      const content = this.content
      axios({
        method: 'post',
        url: this.$store.state.URL + `/journal/${this.id}/comments/create/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.content = null
        this.$emit('get-comment-list')
      })
      .catch((err) => {
        console.log(err)
      })
    },
      
    
  }
}
</script>

<style>

</style>