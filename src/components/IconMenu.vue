<template>
  <mu-appbar title="">
    <mu-text-field icon="search" class="appbar-search-field"  slot="left" hintText="stock"/>
  </mu-appbar>
</template>

<script>
  export default{
    name: 'icon-menu',
    data() {
      return {
      
      }
    },
    methods: {

    }
  }
</script>


<style lang="less">
  .appbar-search-field{
    color: #FFF;
    margin-bottom: 0;
    &.focus-state {
      color: #FFF;
    }
    .mu-text-field-hint {
      color: fade(#FFF, 54%);
    }
    .mu-text-field-input {
      color: #FFF;
    }
    .mu-text-field-focus-line {
      background-color: #FFF;
    }
  }
</style>