<template>
  <div>
    <div class="mb-3 row">
      <label for="username" class="col-sm-2 col-form-label">UserName</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
    </div>
    <div class="mb-3 row">
      <label for="password" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="password" v-model="password">
      </div>
    </div>
    <div>
      <button type="button" class="btn btn-primary" @click="logIn">로그인</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInForm',
  data() {
    return {
    username: null,
    password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      
      const payload = { username, password }
      this.$store.dispatch('logIn', payload)
    }
  
  }
}
</script>

<style>

</style>