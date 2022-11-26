<template>
  <div>
    <button type="button" class="btn btn-dark" @click="deleteComment">삭제</button>
  </div>
</template>

<script>
import axios from'axios'
export default {
  name: 'JorunalCommentDeleteButton',
  props: {
    comment_id: Number
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url: this.$store.state.URL + `/journal/${this.comment_id}/comments/detail/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('update-comment-list')

      })
      .catch((err) => console.log(err))
    }

  }
}
</script>

<style>

</style>