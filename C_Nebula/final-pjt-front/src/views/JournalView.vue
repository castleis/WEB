<template>
  <div>
    <div class="container">
      <div class="row g-0">
        <h1 class="col text-left">Journal</h1>
        <div class="d-flex justify-content-between">
          <span>
            <select class="form-select" aria-label="오름차순" v-model="order">
              <option :value="0">최신순</option>
              <option :value="1">오래된순</option>
              <option :value="2">인기순</option>
            </select>
          </span>
          <button @click="journalCreate" class="col-2 btn btn-outline-success">저널 작성</button>
        </div>
      </div>
    </div>
    <hr>
    <br>
    <JournalList :journalList="journalList"/>
    <hr>
  </div>
</template>

<script>
import JournalList from '@/components/journal/JournalList'
import axios from 'axios'

export default {
  name: 'JournalView',
  components: {
    JournalList
  },
  data () {
      return {
        journalList : null,
        order: 0
      }
    },
  methods: {
    journalCreate () {
      this.$router.push({name:'journalCreateView'})
  },
  getJournalList () {
    axios({
      method: 'get',
      url: this.$store.state.URL + `/journal/`,
      params:{
        order: this.order
      },
      headers: {
        Authorization : `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.journalList = res.data
      console.log('journalList : ', this.journalList)

    })
    .catch((err) => console.log(err))
  }
  },
  watch: {
    order: function(value, oldvalue) {
      value, oldvalue
      this.getJournalList()
    } 
  },
  created () {
    this.getJournalList()
  }
}
</script>

<style>

</style>