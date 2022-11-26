<template>
  <div @click="moviesDetail" class="col-3">
    <div class="a">
      <div class="item card text-center" style="width: 13rem;">
        <img :src="poster" class="card-img-top" alt="">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props:{
    movie : Object,
  },
  data() {
    return{
      poster : "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path,
      index : this.movie.id

    }
  },
  methods: {
    moviesDetail() {
      this.$store.dispatch('getDetail', this.index)
      this.$router.push({name: 'movieDetail', params: {movie_id: this.index}})
    }
  }
}
</script>

<style>
.a {
  display: flex;
  padding: 5px;
}

.item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
}

.a:focus-within .item,
.container:hover .item {
  transform: translateX(-5%);
}

.item:focus ~ .item,
.item:hover ~ .item {
  transform: translateX(5%);
}

.a .item:focus,
.container .item:hover {
  transform: scale(1.1);
  z-index: 1;
}

.item img {
  display: block;
  max-width: 100%;
}
.card-img-top {
  height: 30rem;
  object-fit: cover;
}
</style>