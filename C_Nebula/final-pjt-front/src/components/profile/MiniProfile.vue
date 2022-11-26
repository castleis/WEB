<template>
    <div class="card col-3" >
        <div class="card-body" @click="goToProfile">
            <!-- <p>유저 pk :{{user}}</p> -->
            <h3>{{nickname}}</h3>
            <p>경험치 :{{ranking}}</p>
            <p>성인 여부:{{String(adult)}}</p>
        </div>
    </div>
</template>

<script>
export default {
    
    name: 'MiniProfile',
    props: {
        profile: Object
    },
    data() {
        return {
            user: this.profile.user,
            nickname: this.profile.nickname,
            ranking: this.profile.ranking,
            adult: this.profile.adult
        }
    },
   
    methods:{
        goToProfile() {
            console.log(this.user)
            this.$router.push({ name: 'profile', params: { 'user_id': `${this.user}` } })
        }
            
        }
}

</script>

<style>
.card {
    margin: 10px;
}
</style>