const fs      = require("fs");
const S       = require("string");
const cheerio = require("cheerio");
const iconv   = require("iconv-lite");
const async   = require("async");
const request = require("request");
const mongo   = require("./mongo_test.js");
const dateTime= require("date-time");


const get_webpage = (url) => { //Get HTML information
	return new Promise((resolve, reject)=>{
		request({url:url,encoding:null}, function (err, body) {
	  	  if(err)reject(err)
	  	  resolve(body.body);
		});
	});
}


const sortArr = (arry1, arry2, arry3, id=0, val=0, dif=0) => {

}

const sellAndBuyPercent = async() => {
	var stockHTML = "http://jdata.yuanta.com.tw/z/zc/zcx/zcxD5.djjs?A=";
	var buyInfoHTML = "http://jdata.yuanta.com.tw/z/zc/zcl/zcl_";//"6116.djhtm"


	var centerData = fs.readFileSync("./stock_info/center.txt",'utf8');
	var cabinetData = fs.readFileSync("./stock_info/cabinet.txt",'utf8');

	var centerArr = S(centerData).splitLeft('\r\n');
	var cabinetArr= S(cabinetData).splitLeft('\r\n');
	console.log(centerArr);
	var centerRankOne = [];
	var centerRankTwo = [];
	var body = "";
	var buyBody = "";
	var arrNum  = 0;

	async.eachSeries(centerArr, async(stockID, callback)=>{
		arrNum = arrNum + 1;
		console.log("=====" + stockID + "=====");
		body = await get_webpage(stockHTML + stockID);
		var bodyBig5 = iconv.decode(body,"big5");
		var a = cheerio.load('<html><head></head><body>' + S(bodyBig5).substr(18,S(bodyBig5).length-25).s + '</body></html>');

		var percentData = a('td');
		var one   = parseFloat(S(a(percentData[29]).text()).splitLeft('%')[0]);
		var two   = parseFloat(S(a(percentData[42]).text()).splitLeft('%')[0]);
		var three = parseFloat(S(a(percentData[55]).text()).splitLeft('%')[0]);
		var four  = parseFloat(S(a(percentData[68]).text()).splitLeft('%')[0]);
		var five  = parseFloat(S(a(percentData[81]).text()).splitLeft('%')[0]);


		var trading_shortToday = parseFloat(S(a(percentData[28]).text()).replaceAll(',','').s);
		var trading_shortYester= parseFloat(S(a(percentData[41]).text()).replaceAll(',','').s);
		var trading_shortDiff  = trading_shortToday - trading_shortYester;
		var dif = (one*100-two*100)/100;

		//get buy info
		buyBody = await get_webpage(buyInfoHTML + stockID +'.djhtm');
		var buybodyBig5 = iconv.decode(buyBody,"big5");
		var b = cheerio.load(buybodyBig5);
		var buyData = b('.t01 td');

		console.log(S(b(buyData[21]).text()).replaceAll(',','').s);
		console.log(S(b(buyData[22]).text()).replaceAll(',','').s);
		console.log(S(b(buyData[23]).text()).replaceAll(',','').s);

		var foreign_Investors = parseFloat(S(b(buyData[21]).text()).replaceAll(',','').s);
		var investment_Trust  = parseFloat(S(b(buyData[22]).text()).replaceAll(',','').s);
		var dealer            = parseFloat(S(b(buyData[23]).text()).replaceAll(',','').s);

		var obj = {
			"id" :stockID,
			"one":one,
			"two":two,
			"dif":dif,
			"foreignInvestors" : foreign_Investors,
			"investmentTrust"  : investment_Trust,
			"dealer"           : dealer
		} 
		if(one >= 20.0000 && one <= 40.0000 && trading_shortToday > 3000 && trading_shortDiff > 300){
			centerRankOne.push(obj);
			centerRankOne.sort(function(obj1, obj2){
				return obj2.one - obj1.one;
			});
			if(centerRankOne.length > 30){
				centerRankOne.pop();
			}
		}
		console.log(centerRankOne);


		if((one-two) > 2 && trading_shortToday > 3000 && trading_shortDiff > 300){
			centerRankTwo.push(obj);
			centerRankTwo.sort(function(obj1, obj2){
				return obj2.dif - obj1.dif;
			});
			if(centerRankTwo.length > 30){
				centerRankTwo.pop();
			}
		}
		console.log(centerRankTwo);

		if(arrNum == centerArr.length){
			var url = 'mongodb://localhost:27017/stock';
			var mongodb = new mongo(url);
			var date = S(S(dateTime()).splitLeft(" ")[0]).replaceAll("-","").s;
			await mongodb.insert({
				TimeStamp     : date,
				rankByPercent : centerRankOne,
				rankByDiff    : centerRankTwo
			},"tradingShort");
		}

	});
	/*var url = 'mongodb://localhost:27017/tradingshort';
	var mongodb = new mongo(url);
	await mongodb.remove("table1");*/
	//var table1_data = await mongodb.get({TimeStamp:"20171106"}, "table1");
	//console.log(table1_data[0].rankByDiff);
}

sellAndBuyPercent();
