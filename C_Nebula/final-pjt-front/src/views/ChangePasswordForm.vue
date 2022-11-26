<template>
  <div class="m-5">
    <div class="mb-3 row">
      <label for="old_password" class="col-sm-2 col-form-label">이전 비밀번호</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="old_password" v-model="old_password">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="new_password1" class="col-sm-2 col-form-label">비밀번호</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="new_password1" v-model="new_password1">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="new_password2" class="col-sm-2 col-form-label">비밀번호 확인</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="new_password2" v-model="new_password2">
      </div>
    </div>
    <div class="d-flex justify-content-end">
      <button type="button" class="btn btn-primary" @click="changePassword">비밀번호 변경</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChangePasswordForm',
  data() {
    return {
      new_password1: null,
      new_password2: null,
      old_password: null

    }
  },
  methods: {
    changePassword() {
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      const old_password = this.old_password


      const payload = {
        new_password1: new_password1,
        new_password2: new_password2,
        old_password: old_password

      }
      this.$store.dispatch('changePassword', payload)
    }
  }
}
</script>

<style>

</style>