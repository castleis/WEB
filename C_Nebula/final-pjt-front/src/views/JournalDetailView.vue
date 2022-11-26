<template>
  <div class="container">
    <div v-if="!to_update">
      <p>저널 id :{{ id }}</p>
      <h1>글 제목 : {{ title }}</h1>
      <div class="row">
        <div class="col-8">
          <span @click="goToProfile">작성자 닉네임 : {{ nickname }}   |  {{ created_at }}</span><br>
        </div>
        <!-- <span>{{ created_at }}</span> -->
        <!-- <p >수정일자 : {{ updated_at }}</p> -->
        <div class="col-4">
          <div @click="likeJournal">
            <i class="bi bi-heart" v-if="!is_like_journal"></i>
            <i class="bi bi-heart-fill" v-if="is_like_journal"></i>
            <span> {{like_user.length}}</span>
          </div>
        </div>
      </div>
      <hr>
      <h5>영화 제목 : {{ movie_title }}</h5>
      <p>별점 : {{starRank}}</p>

      <p>{{ content }}</p>
      <!-- <p>시크릿(불린값이라 안보임) : {{ secret }}</p> -->
      <!-- <p>이 글을 좋아하는 유저 : {{ like_user }}</p> -->
      <div class="d-flex justify-content-end">
        <button type="button" class="btn btn-dark" @click="toggleUpdate" v-if="is_me">수정</button>
      </div>
      
      <hr>
      <!-- 여기가 댓글작성폼 -->
      <JournalCommentCreateForm :id="id" @get-comment-list="getCommentList" />
      <!-- 여기가 댓글리스트 -->
      <JournalCommentList 
      :commentList="commentList"
      @like-comment-update="likeCommentUpdate" 
      :journal_id="id"
      @get-comment-list="getCommentList"
      class="mt-3"
      />
    </div>
    
    <!-- 여기부터는 수정폼 -->
    <div v-if="to_update" class="m-5 container">
      <div class="row">
        <div class="col-8">
          <h1>영화저널 수정</h1>
          <form @submit.prevent="updateJournal">
            <div class="mb-3">
              <SearchBarSimple @check-this-movie="getMovieId" class="mb-2"/>
              <span>선택된 영화 : {{ update_showTitle }}</span>
              <input
                id="updateTitle"
                class="form-control mb-3"
                :value="title"
                placeholder="저널 제목을 입력하세요"/>
                <textarea
                class="form-control"
                id="updateContent"
                rows="3"
                placeholder="리뷰 내용을 입력하세요"
                :value="content"
                ></textarea>
              </div>
              <div class="container p-0">
                <div class="row d-flex justify-content-between">
                  <star-rating v-model="updateRank" :increment=0.5 :animate="true" :glow="5"  active-color="#f001" id="starRank" class="col-3"></star-rating>
                  <div class="col-6">
                    <input type="checkbox" id="checkbox" v-model="secretUpdate" />
                    <label for="checkbox">비밀글</label>
                    <div class="container">
                      <div class="row d-flex justify-content-end">
                        <button type="button" class="btn btn-danger col-3 mx-1" @click="deleteJournal">삭제</button>
                        <button type="button" class="btn btn-secondary col-3 mx-1" @click="toggleUpdate">수정 취소</button>
                        <button type="submit" class="btn btn-primary col-3 mx-1">수정</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
          </form>
        </div>
        <div class="item card col-3" style="width: 13rem;" v-if="update_poster">
          <img :src="update_poster" class="card-img-top" alt="">
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import JournalCommentCreateForm from "@/components/journal/JournalCommentCreateForm";
import JournalCommentList from "@/components/journal/JournalCommentList";
import StarRating from 'vue-star-rating'
import SearchBarSimple from '@/components/SearchBarSimple'
import axios from "axios";
export default {
  name: "JournalDetailView",
  components: {
    JournalCommentCreateForm,
    JournalCommentList,
    StarRating,
    SearchBarSimple
  },
  computed: {

    is_me() {
      if (this.user_id === this.$store.state.user_id) {
        return true
      } else {
        return false
      }
    },
    
    is_like_journal() {
      if (this.like_user.includes(this.$store.state.user_id)) {
        return true
      } else {
        return false
      }
    },
    starRank() {
      if ((this.rank % 2) === 1) {
        return "★".repeat(parseInt(parseInt(this.rank / 2))) + "☆"
      } else {
        return "★".repeat(parseInt(this.rank / 2))
      } 
    },
  },
  data() {
    return {
      commentList: null,
      to_update: false,
      secretUpdate : false,
      updateRank: 0,
      id : null,
      title : null,
      content : null,
      secret : null,
      like_user : [],
      user_id : null,
      rank : null,
      updated_at : null,
      created_at : null,
      movie_id : null,
      nickname : null,
      movie_title : null,
      update_movie_id : null,
      update_showTitle : null,
      update_poster : null,
      update_title : null,
      update_content : null,

    };
  },
 
  methods: {
    toggleUpdate() {
      this.to_update =!this.to_update;
    },
    journalDetail() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/journal/${this.$route.params.journal_id}/detail/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
          this.id = res.data.id,
          this.title= res.data.title,
          this.content= res.data.content,
          this.created_at= res.data.created_at,
          this.like_user= res.data.like_user,
          this.movie_id= res.data.movie,
          this.secret= res.dataprivated,
          this.rank= res.data.rank,
          this.updated_at= res.data.updated_at,
          this.user_id= res.data.user,
          this.nickname= res.data.nickname,
          this.movie_title= res.data.movie_title
        }
      )
      .then(() => {
        this.getCommentList()
      })
      .catch((err) => console.log(err))
    },
    getCommentList() {
      axios({
        method: "get",
        url: this.$store.state.URL + `/journal/${this.id}/comments/`,
      })
        .then((res) => {
          this.commentList = res.data;
          
        })
        .catch((err) => console.log(err));
    },
    updateJournal() {
      const titleTag = document.querySelector('#updateTitle')
      const contentTag = document.querySelector('#updateContent')
      const title = titleTag.value
      const content = contentTag.value
      const rank = this.updateRank * 2
      axios({
        method: 'put',
        url: this.$store.state.URL + `/journal/${this.id}/detail/`,
        data: {
          title: title,
          content: content,
          private: this.secret,
          rank: rank,
          movie: this.update_movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.journalDetail()
        this.toggleUpdate()

      })
      .catch((err) => {
        if (err.response.data.movie[0] === "This field may not be null.") {
          alert('영화를 선택해주세요!')
        }
      })
    },
    
    deleteJournal() {
      axios({
        method: 'delete',
        url: this.$store.state.URL + `/journal/${this.id}/detail/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({name: 'journalView'})
        this.$store.commit('DELETE_JOURNAL_DETAIL')
      })
      .catch((err) => console.log(err))
    },

    // 저널 좋아요 -> 응답 받으면 다시 저널 디테일 요청
    likeJournal() {
      axios({
        method: 'post',
        url: this.$store.state.URL + `/journal/${this.id}/journal_likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.journalDetail()
      })
      .catch((err) => console.log(err))
    },

    // 저널 좋아요 이후 emit 두번 받아서 좋아요 상태 업데이트 해주기
    likeCommentUpdate() {
      this.getCommentList()
    },
    goToProfile() {
      this.$router.push({name: 'profile', params: {user_id: this.user_id}})
    },
    getMovieId(context) {
      this.update_movie_id = context.index
      this.update_showTitle = context.title
      this.update_poster = context.poster
    },
    changeTitle() {
      const titleTag = document.querySelector('#updateTitle')
      this.update_journal_title = titleTag.value
    },
    changeContent() {
      const contentTag = document.querySelector('#updateContent')
      this.update_journal_title = contentTag.value
    }
  },

  
  created() {
    this.journalDetail()
    
  },
};
</script>

<style>
.container {
  padding: 30px;
}
</style>