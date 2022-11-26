<template>
  <div>
    <div @click="follow">
      <button class="btn btn-primary btn-sm"  v-if="!is_followed">팔로우</button>
      <button class="btn btn-danger btn-sm"  v-if="is_followed">언팔로우</button>
    </div>
  </div>
</template>

<script>
// 해당 유저의 팔로워 중에 내가 있는지 혹은 내 팔로잉 중에 해당 유저가 있는지 어떤걸로 판단?
import axios from 'axios'
export default {
  name: "FollowButton",
  props: {
    user_id: Number,
    is_followed: Boolean
  },
  methods: {
    follow() {

      axios({
        method: 'post',
        url: this.$store.state.URL + `/profile/${this.user_id}/follow/`,
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('update-follow')

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