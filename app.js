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

const app = new Koa();
const router = new Router();
const S = require("string");
const analyze_info = require("./lib/analyze_info.js");


router.use('/', index.routes(), index.allowedMethods());
router.use('/users', users.routes(), users.allowedMethods());

app.use(convert(logger()))
   .use(convert(bodyParser()))
   .use(convert(koaStatic(path.join(__dirname, 'node_modules'), { hidden: true })))
   .use(convert(views(path.join(__dirname, 'views'), { ext: 'html', cache: true })))
   .use(convert(koaStatic(path.join(__dirname, 'public'), { hidden: true })))
   .use(router.routes())
   .use(router.allowedMethods())

var http = require("http");
var server = http.createServer(app.callback());
var io = require('socket.io')(server);

io.on('connection', async function (socket) {

	var analyze = await analyze_info.table5()
	var values = [];
	var labels = [];
	var today_buy = [];
	for(var i = 0; i < analyze.length/2; i++){
		values.push(S(analyze[i].Buy_count).replaceAll(",","").s);
		labels.push(S(analyze[i].No).replaceAll(",","").s);
		today_buy.push(S(analyze[i].today_buy).replaceAll(",","").s);
	}
	//console.log(values);
    socket.emit('fiveDay', { value : values, label : labels, today_buy:today_buy}); // 五天歪資買量最高*/
});

server.listen(3000, () => console.log('Listening on port 3000.'));


export default app;
