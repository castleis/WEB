<template>
  <div class="d-flex justify-content-end">
    <span>
      <button @click="profileUpdate" class="btn btn-primary btn-sm" v-if="is_me">개인정보수정</button>
      <FollowButton
      v-if="!is_me"
      :user_id="Number(user_id)" 
      @update-follow="updateFollow"
      :is_followed="is_followed"
      />
    </span>
  </div>
</template>

<script>
import FollowButton from '@/components/profile/FollowButton'
export default {
  name: "ProfileBanner",
  components: {
    FollowButton,
  },
  props: {
    user_id: Number,
    is_followed: Boolean
  },
  computed: {
    is_me() {
      return this.user_id === this.$store.state.user_id
    }
  },
  methods: {
    updateFollow() {
      this.$emit('update-follow')
    },
    profileUpdate() {
      this.$router.push({name: 'profileUpdateView'})
    }
  }

}
</script>

<style>

</style>