<template>
  <div>
    <div v-if="!to_update">
      <!-- <h1>MovieReviewListItem</h1> -->
      <!-- <h3>{{ starRank }}</h3> -->
      <div class="shadow p-3 mb-5 bg-body rounded">
        <div class="container">
          <div class="row">
            <p class="d-flex justify-content-start" style="font-size:13px;"><router-link :to="{ name: 'profile', params: { 'user_id' : `${user_id}`} }">{{ nickname }}</router-link>님의 리뷰 :</p>
          </div>
          <div class="row d-flex justify-content-between">
            <div class="d-flex justify-content-start mx-5 fs-3 col-4">
              {{ starRank }}
            </div>
            <div class="col-2 mt-3">
              <div @click="likeReview">
                <i class="bi bi-heart" v-if="!is_like"></i>
                <i class="bi bi-heart-fill" v-if="is_like"></i>
                <span class="mx-2">{{like_user_count}}</span>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p class="text-start mx-5 mt-2">{{ content }}</p>
            </div>
          </div>
          <div>
            <div class="col">
              <span v-if="is_me" class="d-flex justify-content-end"><button type="button" class="btn btn-dark" @click="updateToggle">수정</button></span>
    
              
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 여기는 수정 폼 -->
      <form v-if="to_update" @submit.prevent class="mb-3">
        <label for="updateContent" class="form-label d-flex justify-content-start">수정 내용 입력</label>
        <star-rating v-model="updateRank" :increment=0.5 :animate="true" :glow="5"  active-color="#f001" id="starRank" class="mb-2"></star-rating>
        <div class="mb-3">
          <textarea
          class="form-control"
          id="updateContent"
          rows="3"
          :value="content"
          ></textarea>
        </div>
        <div class="d-flex justify-content-end">
          <span><button @click="deleteReview" class="btn btn-danger mx-1">삭제</button></span>
          <span><button @click="updateToggle" class="btn btn-secondary mx-1">수정 취소</button></span>
          <span><button @click="updateReview" type="button" class="btn btn-primary mx-1">수정</button></span>
        </div>
      </form>
  </div>
</template>

<script>
import "bootstrap-icons/font/bootstrap-icons.css"
import StarRating from 'vue-star-rating'
export default {
  name: "MovieReviewListItem",
  components: {
    StarRating,
  },
  
  props: {
    movie_review: Object,
  },
  computed: {
    id() {
      return this.movie_review.id;
    },
    nickname() {
      return this.movie_review.nickname;
      
    },
    content() {
      return this.movie_review.content;
    },
    rank() {
      return this.movie_review.rank;
    },
    like_user() {
      return this.movie_review.like_user
    },
    like_user_count() {
      return this.movie_review.like_user.length
    },
    user_id() {
      return this.movie_review.user
    },
    is_like() {
      if (this.movie_review.like_user.includes(this.$store.state.user_id)) {
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
    is_me() {
      if (this.user_id === this.$store.state.user_id) {
        return true
      } else {
        return false
      }
    }
  },
  data() {
    return {
      updateRank : 0,
      to_update: false,
    };
  },
  methods: {
    deleteReview() {
      this.$emit("delete-review", this.id);
    },
    updateReview() {
      this.updateToggle()
      const contentTag = document.querySelector('#updateContent')

      const content = contentTag.value
      const rank = this.updateRank * 2
      const context = {
        id: this.id,
        content: content,
        rank: rank
        // TODO: Rank도 default가 기존값이었으면 좋을텐데...
        
      };
      this.$emit("update-review", context);
      console.log('MovieReviewListItem')
    },
    updateToggle() {
      this.to_update = !this.to_update;
    },
    starRanking(rank) {
      this.updateRank = rank;
    },
    likeReview() {
      this.$emit("like-review", this.id);
    }
  },

};
</script>

<style>
</style>