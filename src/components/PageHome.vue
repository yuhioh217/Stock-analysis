<template>
  <div>
      <one-day></one-day>
      <five-day></five-day>
  </div>

</template>

<script>

import OneDay from './OneDay.vue'
import FiveDay from './FiveDay.vue'

export default {
  name:'page-home',
  data () {
    return {
    }
  },
  components : {
    OneDay,
    FiveDay
  },
  methods: {

  }
}
</script>
