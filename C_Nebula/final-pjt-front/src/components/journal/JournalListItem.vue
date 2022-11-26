<template>
  <div class="container">
    <div @click="journalDetail" class="row g-0">
      <div class="item">
        <h1 class="col">{{ title }}</h1>
        <p>{{ nickname }}님의 글</p>
        <p class="col">글 번호 : {{ id }}</p>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JournalListItem',
  props: {
    journal: Object,

  },
  computed: {
    id() {
      return this.journal.id
    },
    nickname() {
      return this.journal.nickname
    },
    title() {
      return this.journal.title
    },
    content() {
      return this.journal.content
    },
    secret() {
      return this.journal.private
    }
  },
  methods: {
    journalDetail() {

      this.$router.push({name: 'journalDetail', params:{journal_id : this.journal.id}})
    
    },

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
</style>