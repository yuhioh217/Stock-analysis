"use strict";

var Router = require('koa-router');
var router = module.exports = new Router();
var homepagectrl = require('../src/controllers/homePageController');

router.get('/home/tradingShort/:date', homepagectrl.table1) //http://localhost:3000/apis/home/table1/dateTime(format:20171229)/
	  .get('/home/market/:date',homepagectrl.market_date)
	  .get('/home/market',homepagectrl.market_all)
	  .get('/home/industry/:category',homepagectrl.industry);