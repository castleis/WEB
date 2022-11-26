<template>
  <div>
    <div class="mb-3 row">
      <label for="username" class="col-sm-2 col-form-label">ID</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="password1" class="col-sm-2 col-form-label">비밀번호</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="password1" v-model="password1">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="password2" class="col-sm-2 col-form-label">비밀번호 확인</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="password2" v-model="password2">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="nickName" class="col-sm-2 col-form-label">닉네임</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="nickName" v-model="nickName">
      </div>
    </div>
    <div class="d-flex justify-content-end">
      <div class="align-content-center">
        <label for="checkbox" class="mx-2">성인입니까?</label>
        <input type="checkbox" id="checkbox"  v-model="adult">
        <span>
          <button type="button" class="btn btn-primary ms-3" @click="signUp">가입</button>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpForm',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      nickName: null,
      adult: false
      // email: null
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nickName = this.nickName
      const adult = this.adult

      const payload = {
        forSignUp : {
          username: username,
          password1: password1,
          password2: password2,
        },
        forProfile:{
          nickname: nickName,
          adult: adult
        }


      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

</style>