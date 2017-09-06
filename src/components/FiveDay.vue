<template>
  <div>
    <mu-list :value="value" @change="handleChange">
      <mu-list-item  :open="open" :value="1" title="連續五天量" inset toggleNested>
        <mu-avatar src="/assets/externals/images/red.jpg" slot="leftAvatar"/>
          <template v-for="(item,index) in data.label">
            <mu-list-item v-bind:title="item" slot="nested" v-bind:value="indexChange(index)" v-bind:describeText=" 
            '5天外資買量 : ' + data.value[index] + '\n' +
             '今天外資購買狀況 : ' + data.today_buy[index]" inset>
              <template v-if="isRedGreen(data.today_buy[index])">
                <mu-avatar src="/assets/externals/images/red.jpg" slot="leftAvatar"/>
              </template>
              <template v-else>
                <mu-avatar src="/assets/externals/images/green.jpg" slot="leftAvatar"/>
              </template>
            </mu-list-item>
          </template>
      </mu-list-item>
    </mu-list>
  </div>

</template>


<script>
var socket = io.connect('http://10.1.1.10:3000');

export default {
  name:'five-day',
  data () {
    return {
      open: false,
      value: 1,
      data:{ value : [1200,2000,3000], label : ['test A','test B','test C'], today_buy: ['123','123','123']}
    }
  },
  created : function(){
    socket.on('fiveDay', function(data) {
      this.data = data;
      console.log(this.data.value);
    }.bind(this));
  },

  mounted : function (){
    socket.on('fiveDay', function(data) {
      this.items = data.label;
      console.log(this.items.length);
    }.bind(this));
  },
  methods: {
    handleChange (val) {
      this.value = val;
    },

    indexChange (index){
      return index + 2;
    },

    isRedGreen (value){
      if(parseInt(value) > 0)
        return true;
      else
        return false;
    }
  }
}
</script>