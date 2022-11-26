<template>
  <div>
    <JournalListItem v-for="journal in journalList" :key="journal.id" :journal="journal"/>
  </div>
</template>

<script>
import JournalListItem from '@/components/journal/JournalListItem'
export default {
  name: 'JournalList',
  components: {
    JournalListItem
  },

  props: {
    journalList: Array,
  },

}
</script>

<style>

</style>