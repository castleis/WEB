<template>
  <!-- 로그인 안되었을때 -->
  <div class="mx-3">
    <div v-if="!isLogin" class="container">
      <div class="row justify-content-center">
        <button type="button" class="btn btn-outline-light btn-sm col-6">
          <router-link :to="{ name: 'signUp' }" class="nav-link"
            >SignUp</router-link
          >
        </button>
        <div class="col-4 mx-1">
          <button type="button" v-b-modal.modal-1 class="btn btn-outline-light btn-sm"
            >LogIn</button
          >
          <b-modal b-modal id="modal-1" title="로그인" hide-footer>
            <div class="mb-3 row">
              <label for="username" class="col-sm-3 col-form-label"
                >ID</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  v-model="loginUsername"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="password" class="col-sm-3 col-form-label"
                >비밀번호</label
              >
              <div class="col-sm-8">
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  v-model="password"
                />
              </div>
            </div>
             <div class="d-flex justify-content-end me-3">
               <button type="button" class="btn btn-primary" @click="logIn">
                 로그인
               </button>
             </div>
          </b-modal>
        </div>
      </div>
    </div>
    <!-- 로그인 되었을때 -->
    <div v-if="isLogin">
      <div class="container text-end">
        <div class="row">
          <div class="col d-flex-center">
            <router-link 
            :to="{ name: 'profile', params:{ user_id : `${this.$store.state.user_id}` } }" 
            class="nav-link">
            <h5>{{ nickName }}</h5>
          </router-link>
        </div>
        </div>
        <div class="row">
          <div class="col">
            <button type="button" class="btn btn-outline-light btn-sm" @click="logOut">
              LogOut
            </button>
          </div>
          <div class="col">
            <button type="button" class="btn btn-outline-light btn-sm" @click="changePassword">
              changePassword
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginNav",
  data() {
    return {
    loginUsername: null,
    password: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    nickName() {
      return this.$store.state.nickName;
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch("logOut");
    },
    logIn() {
      const username = this.loginUsername
      const password = this.password
      
      const payload = { username, password }
      this.$store.dispatch('logIn', payload)
    },
    changePassword() {
      this.$router.push({name: "ChangePassword"})
    }
  },
};
</script>

<style>
.mx-3{
  color: white;
}
</style>