var request = require("tinyreq");
var cheerio = require("cheerio");
var cheerioReq = require("cheerio-req");
var S = require("string");
var dateTime  = require("date-time");
var iconv = require("iconv-lite");
var mongo = require("./mongo.js");
var async = require("async")

const get_webpage = (url) => { //Get HTML information
	return new Promise((resolve, reject)=>{
		
		request({url:url,encoding:null}, function (err, body) {
	  	  if(err)reject(err);
	  	  resolve(body);
		});
	});
}

const get_field = async(body, table) => {
	var $ = cheerio.load(body);
	//console.log(body);
	var lists = $("#oMainTable tr");
	//console.log($(lists).text());
	//db url;
	var url = 'mongodb://localhost:27017/foreignInvestment';
	var mongodb = new mongo(url);
	var date = S(S(dateTime()).splitLeft(" ")[0]).replaceAll("-","").s;
	var arr = [];
	$(lists).each(async function(i, link){
		if(i > 1){

			var strArray = S($(link).text()).splitLeft("\n");

			for(var i = 0; i < strArray.length; i++){
				if(strArray[i] == "")
					strArray.splice(i,1);
			}
			arr.push(strArray);
		}
  	});
	console.log(arr.length);

	async.eachSeries(arr, async(strArray, callback)=>{
		//console.log(strArray);
		var rank = strArray[0];
		//console.log(rank);
		var no = strArray[1]; //
		
		var closing = (S(strArray[2]).replaceAll("&nbsp;","").s);
		//console.log(closing);
		var up_down = (S(strArray[3]).replaceAll("&nbsp;","").s);
		//console.log(up_down);
		var quote_change = (S(strArray[4]).replaceAll("&nbsp;","").s);
		//console.log(quote_change);
		var buy_count = (S(strArray[5]).replaceAll("&nbsp;","").s);
		//console.log(buy_count);
		//get each ranking stock info by the "no" (type:string)
		var stock_no = S(S(no).substr(1,6).s).replaceAll(' ','').s;
		//console.log(stock_no);
		//var testURL = 'http://jdata.yuanta.com.tw/z/ZC/ZCX/ZCX_6116.djhtm';

		var smallURL= 'http://jdata.yuanta.com.tw/z/zc/zcx/zcxD3.djjs?A=' + stock_no;
		//console.log("-----");
		var fiveBuy = await get_webpage(smallURL);
		//console.log(smallURL);
		var fiveBuySituation = iconv.decode(fiveBuy,"big5");
		var a = cheerio.load('<html><head></head><body>' + S(fiveBuySituation).substr(18,S(fiveBuySituation).length-25).s + '</body></html>');
		var fiveList = a('td');
		var today_date = [];
		today_date.push(a(fiveList[5]).text());
		today_date.push(a(fiveList[6]).text());
		today_date.push(a(fiveList[7]).text());
		today_date.push(a(fiveList[8]).text());

		var day_1 = [];
		day_1.push(a(fiveList[9]).text());
		day_1.push(a(fiveList[10]).text());
		day_1.push(a(fiveList[11]).text());
		day_1.push(a(fiveList[12]).text());

		var day_2 = [];
		day_2.push(a(fiveList[13]).text());
		day_2.push(a(fiveList[14]).text());
		day_2.push(a(fiveList[15]).text());
		day_2.push(a(fiveList[16]).text());

		var day_3 = [];
		day_3.push(a(fiveList[17]).text());
		day_3.push(a(fiveList[18]).text());
		day_3.push(a(fiveList[19]).text());
		day_3.push(a(fiveList[20]).text());

		var day_4 = [];
		day_4.push(a(fiveList[21]).text());
		day_4.push(a(fiveList[22]).text());
		day_4.push(a(fiveList[23]).text());
		day_4.push(a(fiveList[24]).text());

		//外資主力買賣
		var smallURL= 'http://jdata.yuanta.com.tw/z/zc/zcx/zcxD2.djjs?A=' + stock_no;
		//console.log("-----");
		var foreignBuy = await get_webpage(smallURL);
		var fiveBuyForeign = iconv.decode(foreignBuy,"big5");
		//console.log('<html><head></head><body>' + S(fiveBuyForeign).substr(18,S(fiveBuyForeign).length-25).s + '</body></html>');
		var b = cheerio.load('<html><head></head><body>' + S(fiveBuyForeign).substr(18,S(fiveBuyForeign).length-25).s + '</body></html>');
		var fiveForeign = b('td');
		//console.log(b(fiveForeign).text());
		/*console.log("==========");
		for(var i =0; i<fiveForeign.length;i++){
			console.log(i + " ---- " + b(fiveForeign[i]).text())
		}*/
		var forBuy = [];
		var forBuyCount = [];
		var forSell= [];
		var forSellCount= [];

		for(var l=11,r=15,lc=14,rc=18,i=0; i<=14;i++){
			forBuy.push(b(fiveForeign[l+i*8]).text());
			forBuyCount.push(b(fiveForeign[lc+i*8]).text());

			forSell.push(b(fiveForeign[r+i*8]).text());
			forSellCount.push(b(fiveForeign[rc+i*8]).text());
		}

		//console.log(forSellCount);

		/*console.log("URL : " + smallURL);
		console.log(today_date);
		console.log(day_1);
		console.log(day_2);
		console.log(day_3);
		console.log(day_4);*/
		
		await mongodb.insert({
			TimeStamp:date, 
			Rank: rank, No:no, 
			Close:closing, 
			Ups_downs:up_down, 
			Quote_change:quote_change, 
			Buy_count:buy_count, 
			today_date:today_date[0],
			today_have:today_date[1],
			today_rate:today_date[2],
			today_buy :today_date[3],
			day_1_date:day_1[0],
			day_1_have:day_1[1],
			day_1_rate:day_1[2],
			day_1_buy :day_1[3],
			day_2_date:day_2[0],
			day_2_have:day_2[1],
			day_2_rate:day_2[2],
			day_2_buy :day_2[3],
			day_3_date:day_3[0],
			day_3_have:day_3[1],
			day_3_rate:day_3[2],
			day_3_buy :day_3[3],
			day_4_date:day_4[0],
			day_4_have:day_4[1],
			day_4_rate:day_4[2],
			day_4_buy :day_4[3],
			forBuy    :forBuy,
			forBuyCount:forBuyCount,
			forSell   :forSell,
			forSellCount:forSellCount
		}, table);
	});
	console.log(date);
  	//await mongodb.remove(table);
  	//await mongodb.find(table);
}

const get_ranking = () => {

}

const test = async() => {

	var buy_1 = "http://jdata.yuanta.com.tw/z/zg/zg_D_0_1.djhtm"; //歪資買超一天排行
	var buy_2 = "http://jdata.yuanta.com.tw/z/zg/zg_D_0_2.djhtm"; //歪資買超兩天排行
	var buy_3 = "http://jdata.yuanta.com.tw/z/zg/zg_D_0_3.djhtm"; //歪資買超三天排行
	var buy_5 = "http://jdata.yuanta.com.tw/z/zg/zg_D_0_5.djhtm"; //歪資買超五天排行

	var body = await get_webpage(buy_1);
	var body_Big5 = iconv.decode(body,"big5");
	get_field(body_Big5, "Table1");

	body = await get_webpage(buy_2);
	body_Big5 = iconv.decode(body,"big5");
	get_field(body_Big5, "Table2")

	body = await get_webpage(buy_3);
	body_Big5 = iconv.decode(body,"big5");
	get_field(body_Big5, "Table3");

	body = await get_webpage(buy_5);
	body_Big5 = iconv.decode(body,"big5");
	get_field(body_Big5, "Table5");
}

test();
