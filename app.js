import Koa from 'koa';
import path from 'path';
import views from 'koa-views';
import logger from 'koa-logger';
import convert from 'koa-convert';
import koaStatic from 'koa-static';
import bodyParser from 'koa-bodyparser';
import Router from 'koa-router';
import index from './routes/index';
import users from './routes/users';
import apis  from './routes/apis';

const app = new Koa();
const router = new Router();



router.use('/', index.routes(), index.allowedMethods());
router.use('/users', users.routes(), users.allowedMethods());
router.use('/apis', apis.routes(), apis.allowedMethods());


app.use(convert(logger()))
   .use(convert(bodyParser()))
   .use(convert(koaStatic(path.join(__dirname, 'node_modules'), { hidden: true })))
   .use(convert(views(path.join(__dirname, 'views'), { ext: 'html', cache: true })))
   .use(convert(koaStatic(path.join(__dirname, 'public'), { hidden: true })))
   .use(router.routes())
   .use(router.allowedMethods());

var http = require("http");
var server = http.createServer(app.callback());
var io = require('socket.io')(server);

server.listen(3000, () => console.log('Listening on port 3000.'));


export default app;
