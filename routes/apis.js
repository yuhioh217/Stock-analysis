"use strict";

var Router = require('koa-router');
var router = module.exports = new Router();
var homepagectrl = require('../src/controllers/homePageController');

router.get('/tab/home/:id', homepagectrl.tabhome)

	  .get('/tab/favorite', homepagectrl.tabfavorite)

	  .get('/tab/about', homepagectrl.tababout)

	  .get('/home/table1/:id', homepagectrl.table1);