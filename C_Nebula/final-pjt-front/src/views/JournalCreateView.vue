<template>
  <div class="m-5 container">
    <div class="row">
      <div class="col-8">
        <h1>영화저널 작성</h1>
        <form @submit.prevent="createJournal">
          <div class="mb-3">
            <SearchBarSimple @check-this-movie="getMovieId" class="mb-2"/>
            <span>선택된 영화 : {{ showTitle }} </span>
            <input
            id="title"
            v-model="title"
            class="form-control mb-3"
            placeholder="저널 제목을 입력하세요"/>
            <textarea
            class="form-control"
            id="content"
            rows="3"
            placeholder="저널 내용을 입력하세요"
            v-model="content"
            ></textarea>
          </div>
          <div class="container p-0">
            <div class="row d-flex justify-content-between">
              <star-rating v-model="rank" :increment=0.5 :animate="true" :glow="5" active-color="#f001" class="col-4"></star-rating>
              <div class="col-3">
                <input type="checkbox" id="checkbox" v-model="secret">
                <label for="checkbox">비밀글</label>
                <button type="submit" class="btn btn-secondary d-flex justify-content-end">
                  작성
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
        <div class="item card col-3" style="width: 13rem;" v-if="poster">
          <img :src="poster" class="card-img-top" alt="">
        </div>
    </div>

    
    
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import SearchBarSimple from '@/components/SearchBarSimple'
import axios from 'axios'

export default {
  name: "JournalCreateView",
  components: {
    StarRating,
    SearchBarSimple
  },
  data() {
    return {
      title: null,
      content: null,
      rank: 0,
      secret: false,
      movie_id : null,
      showTitle : '영화를 선택하세요',
      poster: null
    }
  },
  methods: {
    starRanking(rank) {
      this.rank = rank
    },
    createJournal() {
      axios({
        method: 'post',
        url: this.$store.state.URL + `/journal/create/`,
        data: {
          title: this.title,
          content: this.content,
          rank: this.rank * 2,
          private: this.secret,
          // TODO: 검색기능 추가한 후에 여기 바꿔주기
          movie: this.movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({name: 'journalView'})
      })
      .catch((err) => {
        if (err.response.data.movie[0] === "This field may not be null.") {
          alert('영화를 선택해주세요!')
        }
      }
      )
    },
    getMovieId(context) {
      this.movie_id = context.index
      this.showTitle = context.title
      this.poster = context.poster
    }
  },

  
}
</script>

<style>

</style>