<template>
  <div class="m-5">
    <h1>회원 가입</h1>
    <SignUpForm/>
  </div>
</template>

<script>
import SignUpForm from "@/components/accounts/SignUpForm"
export default {
  name: 'SignUpView',
  components: {
    SignUpForm
  }

}
</script>

<style>

</style>