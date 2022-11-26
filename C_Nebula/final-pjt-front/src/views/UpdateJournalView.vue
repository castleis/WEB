<template>
  <div>
    <h1>UpdateJournalView</h1>
    <form @submit.prevent="updateJournal">
      <StarRanking @star-ranking="starRanking"/>
      <div class="mb-3">
        <label for="title" class="form-label">title</label>
        <input
          id="title"
          :value="journal_detail.title"/>
        <label for="content" class="form-label">content</label>
        <textarea
          class="form-control"
          id="content"
          rows="3"
          placeholder="리뷰 내용을 입력하세요"
          :value="journal_detail.content"
        ></textarea>
      </div>
      <input type="checkbox" id="checkbox" v-model="secretUpdate">
      <label for="checkbox">비밀글</label>
      <button type="submit" class="btn btn-secondary">
        수정
      </button>
    </form>
  </div>
</template>

<script>
import StarRanking from '@/components/StarRanking'
import axios from 'axios'
export default {
  name: 'UpdateJournalView',
  components: {
    StarRanking
  },
  data() {
    return {
      secretUpdate : this.secret,
      rank: 0
    }
  },
  getters: {
    // TODO: 여기도 부트스트랩 할때 다 나눠서 받기
    journal_detail() {
      return this.$store.state.journal_detail
    },
    secret() {
      return this.$store.state.secret
    }
  },
  methods: {
    updateJournal() {
      const titleTag = document.querySelector('#title')
      const contentTag = document.querySelector('#content')
      const title = titleTag.value
      const content = contentTag.value
      axios({
        method: 'put',
        url: this.$store.state.URL + `/journal/${this.journal_detail.id}/detail/`,
        data: {
          title: title,
          content: content,
          private: this.secret,
          rank: this.rank
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
      })
      .catch((err) => console.log(err))
    },
    starRanking(rank) {
      this.rank = rank
    },
  }
}
</script>

<style>

</style>