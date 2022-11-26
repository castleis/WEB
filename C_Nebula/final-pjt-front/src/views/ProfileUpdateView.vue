<template>
  <div>
    <div v-if="!to_delete" class="m-5">
      <div class="mb-3 row">
        <label for="nickName" class="col-sm-2 col-form-label">닉네임</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="nickName" :value="nickName">
        </div>
      </div>
      <div class="d-flex justify-content-end">
        <div class="align-content-center">
          <input type="checkbox" id="checkbox" :value="adult">
          <label for="checkbox">성인입니까?</label>
          <div>
            <button type="button" class="btn btn-primary me-2" @click="updateProfile">정보수정</button>
            <button type="button" class="btn btn-danger" @click="areYouSure">회원탈퇴</button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div v-if="to_delete" class="m-5">
        <h1>정말 탈퇴하시겠습니까?</h1>
        <div class="container">
          <div class="row d-flex justify-content-center" >
            <button type="button" class="btn btn-danger col-1 m-5" @click="deleteForReal">예</button>
            <button type="button" class="btn btn-primary col-4" @click="areYouSure">아니오</button>
          </div>
        </div>


      </div>
    </div>
  </div>


</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileUpdate',
  data() {
    return {
      nickName: this.$store.state.nickName,
      adult: this.$store.state.adult,
      to_delete: false
      // email: null
    }
  },
  methods: {
    updateProfile() {
      const nickNameTag = document.querySelector('#nickName')
      const adultTag = document.querySelector('#checkbox')
      const nickname = nickNameTag.value
      const adult = adultTag.value

      const payload = {
        nickname,
        adult
      }
      this.$store.dispatch('updateProfile', payload)
    },
    deleteUser() {
      this.areYouSure()
    },
    areYouSure() {
      this.to_delete = !this.to_delete
    },
    deleteForReal() {
      axios({
        method: 'delete',
        url: this.$store.state.URL + `/profile/delete_user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$store.dispatch('logOut')
        alert('지금까지 이용해주셔서 감사했습니다!')
        this.$router.push({name: 'index'})
      })
    }
  }
}
</script>

<style>

</style>