<template>
  <div>
    <mu-list :value="value" @change="handleChange">
      <mu-list-item  :open="open" :value="1" title="最近一天外資" inset toggleNested>
        <mu-avatar src="/assets/externals/images/red.jpg" slot="leftAvatar"/>
          <template v-for="(item,index) in data.label">
            <mu-list-item @click="openMenu(index)" v-bind:title="item" slot="nested" v-bind:value="indexChange(index)" inset>
              <template v-if="isRedGreen(data.today_buy[index])==0">
                <mu-avatar src="/assets/externals/images/red.jpg" slot="leftAvatar"/>
              </template>
              <template v-else-if="isRedGreen(data.today_buy[index])==1">
                <mu-avatar src="/assets/externals/images/green.jpg" slot="leftAvatar"/>
              </template>
              <template v-else>
                <mu-avatar src="/assets/externals/images/warning.jpg" slot="leftAvatar"/>
              </template>

              <template>
                <mu-tbody>
                  <mu-tr>
                    <mu-td>今日買超張數 : {{data.value[index]}}</mu-td>
                  </mu-tr>
                </mu-tbody>
              </template>
              
            </mu-list-item>
          </template>
      </mu-list-item>
    </mu-list>
    <mu-dialog :open="dialog" @close="closeMenu" scrollable>
      <mu-sub-header class="redlist" inset>外      資      買      超</mu-sub-header>
        <mu-menu>
          <template v-for="(item,index) in forBuy">
            <mu-list-item v-bind:title="item" v-bind:describeText="forBuyCount[index]">
              <!--<mu-icon value="info" slot="right"/>-->
            </mu-list-item>
          </template>
        </mu-menu>
      <mu-sub-header class="greenlist" inset>外      資      賣      超</mu-sub-header>
        <mu-menu>
          <template v-for="(item,index) in forSell">
            <mu-list-item :title="item" v-bind:describeText="forSellCount[index]">
              <!--<mu-icon value="info" slot="right"/>-->
            </mu-list-item>
          </template>
        </mu-menu>
    </mu-dialog>
  </div>
</template>


<script>
//var socket = io.connect('http://10.1.1.10:3000');

export default {
  name:'one-day',
  data () {
    const menus = []
    for (let i = 0; i < 30; i++) {
      menus.push(i + 1)
    }

    return {
      open: false,
      value: 1,
      data:{ 
             value : [1200,2000,3000], label : ['test A','test B','test C'],today_buy: ['123','123','123'], 
             forBuy: [['A'],['B']], forBuyCount: [['A'],['B']] ,forSell:[['1000'],['1000']], forSellCount: [['1000'],['1000']]
           },
      dialog: false,
      menus,
      forBuy: [],
      forBuyCount: [],
      forSell:[],
      forSellCount: []
    }
  },
  created : function(){
    this.getData();
  },

  mounted : function (){

  },

  updated : function(){

  },
  methods: {

    getData(){
      const dateTime  = require("date-time");
      
      axios.get('http://10.1.1.10:3000/apis/tab/home/'+ dateTime() +'/')
      .then(response => {
        this.data = response.data.data;
      })
    },

    handleChange (val) {
      this.value = val;
    },

    indexChange (index){
      return index + 2;
    },

    isRedGreen (value){
      if(value==""){
        return 2;
      }

      if(parseInt(value) > 0)
        return 0;
      else
        return 1;
    },
    openMenu (index) {

      for(var i =0; i< (this.data.forBuy[index]).length ;i++){
        (this.forBuy).push(this.data.forBuy[index][i]);
      }

      for(var i =0; i< (this.data.forSell[index]).length ;i++){
        (this.forSell).push(this.data.forSell[index][i]);
      }

      for(var i =0; i< (this.data.forBuyCount[index]).length ;i++){
        (this.forBuyCount).push(this.data.forBuyCount[index][i]);
      }

      for(var i =0; i< (this.data.forSellCount[index]).length ;i++){
        (this.forSellCount).push(this.data.forSellCount[index][i]);
      }
      console.log(this.forBuy);
      this.dialog = true;
    },
    closeMenu () {

      this.forBuy = [];
      this.forSell= [];
      this.dialog = false;
    }
  }
}
</script>

<style>
  .redlist {
    background: #FF0000;
    font-weight: 900;
  }

  .greenlist {
    background: #76EE00;
    font-weight: 900;
  }
  .mu-dialog{
    width:85%;
  }
  .mu-dialog-body {
    padding: 0 0 0 0;
  }

</style>