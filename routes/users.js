"use strict";

var Router = require('koa-router');
var router = module.exports = new Router();

router.get('/', function (ctx, next) {
  ctx.body = 'this a users response!';
});
