<template>
  <div class="content">
    <div class="navbar">
      <template>
        <mu-appbar title="Title">
          <mu-icon-button icon="close" slot="left"/>
          <mu-flat-button color="white" label="flat Button" slot="right"/>
        </mu-appbar>
      </template>

      <mu-tabs :value="activeTab" @change="handleTabChange">
        <mu-tab value="home" icon="home" title="HOME"/>
        <mu-tab value="favorite" icon="favorite" title="FAVORITES"/>
        <mu-tab value="search" icon="person_pin" title="SEARCH"/>
      </mu-tabs>
    </div>
    <div class="home-main">
      <div v-if="activeTab === 'home'" >
        <page-home></page-home>
      </div>
      <div v-if="activeTab === 'favorite'">

      </div>
      <div v-if="activeTab === 'search'">

      </div>
    </div>
  </div>

</template>

<script>
import PageHome from './PageHome.vue'

export default {
  data () {
    return {
      theme: 'light',
      activeTab: 'home'
    }
  },
  created : function(){

  },

  components : {
    PageHome
  },
  methods: {
    handleTabChange (val) {
      this.activeTab = val;
    }
  }
}

</script>

<style>
.content {
  width: 100%;
  height: 100%;
}

.navbar {
  position: fixed;
  width: 100%;
  height: 100px;
  background: #0077cc;
  top: 0;
}

.home-main {
  height: 140%;
  padding: 20px;
  margin-top: 150px;
}

</style>
