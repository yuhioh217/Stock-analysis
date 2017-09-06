"use strict";

var Router = require('koa-router');
var router = module.exports = new Router();

router.get('/', async function (ctx, next) {
  await ctx.render('index.html');
})
