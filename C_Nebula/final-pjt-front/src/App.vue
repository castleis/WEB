<template>
  <div id="app">
    <nav class="navbar sticky-top navbar-dark bg-dark justify-content-between align-content-center" style="height:120px;  font-family: 'hyunygothic';">
      <router-link :to="{ name: 'index' }" class="nav-link ms-3"><img :src="require('@/assets/background/galaxycat1.gif')" style="height:70px; width:auto" alt=""><span class="fs-3 pt-1" style="color: yellow; text-shadow:2px 2px 2px #000;">C_Nebula</span></router-link>
      <!-- 흐르는 전광판 -->
      <div>
        



      </div>
      <div class="navbar d-flex justify-content-between">
        <!-- <h1>C_Nebula</h1> -->
        <router-link :to="{ name: 'recommendation' }" class="nav-link mx-2">
          <h3>recommendation</h3>
        </router-link>
        <router-link :to="{ name: 'journalView' }" class="nav-link mx-2">
          <h3>journal</h3>
        </router-link>
        <loginNav />
      </div>
    </nav>
    <router-view />
  </div>
</template>
<script>
import LoginNav from "@/components/LoginNav";
export default {
  name: "App",
  components: {
    LoginNav,
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: black;
  /* font-family: 'jua'; */
  font-family: 'y_computer';
  /* font-family: 'hyunygothic'; */

}
nav{
  color: white
}
/* .somebox{
  height: 100%;
  background-color: #150522;
} */
img{
  height: 7rem;
  width: 12rem;
  margin-right: 10px;
}

/* body {
    background: linear-gradient(-45deg, #5a4ba7, #16083d, #ffffff, #000000);
    background-size: 100% 100%;
    animation: gradient 10s ease infinite;
    height: 100vh;
} */

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
};

@font-face {
  font-family: 'jua';
  src:url('../public/fonts/BMJUA_ttf.ttf')
}
@font-face {
  font-family: 'y_computer';
  src:url('../public/fonts/Ycomputer.ttf')
}
@font-face {
  font-family: 'hyunygothic';
  src:url('../public/fonts/EF_hyunygothic.ttf')
}
@font-face {
  font-family: 'serif_led_board-7';
  src:url('../public/fonts/serif_led_board-7.ttf')
}
@font-face {
  font-family: 'DungGeunMo';
  src:url('../public/fonts/DungGeunMo.ttf')
}




/* nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
