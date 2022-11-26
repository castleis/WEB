<template>
  <div >
    <!-- 여기는 댓글 구간 -->
    <div >
      <div v-if="!to_update && comment" class="shadow p-3 mb-5 bg-body rounded">
        <!-- {{ comment_id }} 여기 부터{{ comment_like_user }} 여기 까지 {{ user_id }}
        {{ created_at }}
        {{ content }} -->
        <p class="d-flex justify-content-start" style="font-size:13px;"><router-link :to="{ name: 'profile', params: { 'user_id' : `${user_id}`} }">{{ nickname }}</router-link>님의 댓글 :</p>
        <p>{{ content }}</p>
        <p>{{ created_at }}</p>
        <div @click="likeComment">
          <i class="bi bi-heart" v-if="!is_like_comment"></i>
          <i class="bi bi-heart-fill" v-if="is_like_comment"></i>
          <span>
            {{ comment_like_user.length }}
          </span>
        </div>
        <span v-if="is_me" class="d-flex justify-content-end">
          <button type="button" class="btn btn-dark " @click="updateToggle">수정</button>
        </span>
      </div>
      
    </div>
    <!-- 여기부터 댓글 수정 폼 -->
    <div v-if="to_update" class="shadow p-3 mb-5 bg-body rounded">
      <JournalCommentUpdateForm
      :id="comment_id" 
      :content="content"
      @get-comment-list="getCommentList"
      @update-toggle="updateToggle"
      />
    </div>
    <!-- 대댓글 리스트 자리 -->
    <JournalReCommentList
    :recommentList="recommentList"
    @update-comment-list="getReCommentList"
    />
    <!-- 대댓글 입력 폼 자리 -->
    <div class="d-flex justify-content-end">
      <button v-if="!to_recomment" class="btn btn-dark mx-3" @click="toggleRecomment">대댓글 작성</button>
    </div>
    <JournalReCommentCreateForm 
    :comment_id="comment_id" 
    :journal_id="journal_id"
    @get-re-comment-list="getReCommentList"
    @update-toggle="updateToggle"
    @toggle-recomment="toggleRecomment"
    v-if="to_recomment"
    class="ms-5"/>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import JournalReCommentList from '@/components/journal/JournalReCommentList'
import JournalReCommentCreateForm from '@/components/journal/JournalReCommentCreateForm/'
import JournalCommentUpdateForm from '@/components/journal/JournalCommentUpdateForm'
export default {
  name: 'JournalCommentListItem',
  components: {
    JournalReCommentCreateForm,
    JournalReCommentList,
    JournalCommentUpdateForm
  },
  props: {
    comment: Object,
    journal_id: Number
  },
  data() {
    return {
      to_recomment : false,
      recommentList : [],
      to_update : false
  }
},
  computed: {
    nickname() {
      return this.comment.nickname
    },
    comment_id() {
      return this.comment.id
    },
    comment_like_user() {
      return this.comment.comment_like_user
    },
    user_id() {
      return this.comment.user
    },
    created_at() {
      return this.comment.created_at.substring(0,10)
    },
    content() {
      return this.comment.content
    },
    is_like_comment() {
      if (this.comment.comment_like_user.includes(this.$store.state.user_id)) {
        return true
      } else {
        return false
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
  methods: {
    likeComment() {
      axios({
        method: 'post',
        url: this.$store.state.URL + `/journal/${this.comment_id}/comments_likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('like-comment-update')
      })
      .catch((err) => console.log(err))
    },
    getCommentList() {
      this.$emit('get-comment-list')
    },
    toggleRecomment() {
      this.to_recomment = !this.to_recomment 
    },
    getReCommentList() {
      axios({
        method: 'get',
        url: this.$store.state.URL + `/journal/${this.journal_id}/${this.comment_id}/recomments/`,
      })
      .then((res) => {
        this.recommentList = res.data
      })
      .catch((err) => console.log(err))
    },
    updateToggle() {
      this.to_update = !this.to_update
    }
  
  },
  created() {
      this.getReCommentList()

}
}
</script>

<style>

</style>