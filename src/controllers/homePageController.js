const S = require("string");
const analyze_info = require("../../lib/analyze_info.js");

exports.tabhome = async(ctx, next) =>
{
	var analyze="";
	console.log('Use Restful API' + ctx.params.id);
	if(ctx.params.id==5){  //5 day
		analyze = await analyze_info.table5()
	}else if(ctx.params.id==1){ //1 day
		analyze = await analyze_info.table1()
	}		
	var values = [];
	var labels = [];
	var today_buy = [];
	var forBuy = [];
	var forSell= [];
	var forBuyCount = [];
	var forSellCount = [];
	for(var i = 0; i < analyze.length; i++){
		values.push(S(analyze[i].Buy_count).replaceAll(",","").s);
		labels.push(S(analyze[i].No).replaceAll(",","").s);
		today_buy.push(S(analyze[i].today_buy).replaceAll(",","").s);
		forBuy.push(analyze[i].forBuy);
		forSell.push(analyze[i].forSell);
		forBuyCount.push(analyze[i].forBuyCount);
		forSellCount.push(analyze[i].forSellCount);
	}

	ctx.response.type = 'application/json';
	ctx.response.body = {
		code: 200,
		message: '',
		data: {
			"value" : values,
			"label" : labels,
			"today_buy":today_buy,
			"forBuy":forBuy,
			"forBuyCount":forBuyCount,
			"forSell":forSell,
			"forSellCount":forSellCount
		}
	};
}

exports.tabfavorite = (req, res) =>
{

}

exports.tababout = (req, res) =>
{

}

exports.table1 = async(ctx, next) => {
	var analyze="";
	console.log('Use Restful API' + ctx.params.date);
	var date_param = ctx.params.date;
	analyze = await analyze_info.home_table1(date_param);

	var date = analyze[0].TimeStamp;
	var rankByPercent = analyze[0].rankByPercent;
	var rankByDiff = analyze[0].rankByDiff;

	ctx.response.type = 'application/json';
	ctx.response.body = {
		code: 200,
		message: '',
		data: {
			"date" : date,
			"rankByPercent" : rankByPercent,
			"rankByDiff" : rankByDiff			
		}
	};
}


