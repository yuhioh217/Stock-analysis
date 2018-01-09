const mongo     = require("./mongo.js");
const dateTime  = require("date-time");
const S         = require("string");

var sortByProperty = (property) => {  // sort the data by Rank.
	return function (x, y) {
		return ((parseInt(x[property]) === parseInt(y[property])) ? 0 : ((parseInt(x[property]) > parseInt(y[property])) ? 1 : -1));
	};
};

var date_check = (date) => {
	var year = parseInt(S(date).substr(0,4));
	var month = parseInt(S(date).substr(4,2));
	var day = parseInt(S(date).substr(6,2));

	var last_year = 0;
	var last_month= 0;
	var last_day  = 0;
	
	switch(month%12){
		case 0: // 12
			if(day == 1){
				last_day = 30; //11月最後一天
				last_month = 11;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 12;
				last_year = year;
			}
			break;
		case 1: // 1
			if(day == 1){
				last_day = 31; //12月最後一天
				last_month = 12;
				last_year = year-1;
			}else{
				last_day = day-1;
				last_month = 1;
				last_year = year;
			}
			break;		
		case 2: // 2
			if(day == 1){
				last_day = 31; //1月最後一天
				last_month = 1;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 2;
				last_year = year;
			}
			break;
		case 3: // 3
			var tDay = (year/4==0)?29:28  // 2月是否閏月
			if(day == 1){
				last_day = tDay; //2月最後一天
				last_month = 2;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 3;
				last_year = year;
			}
			break;
		case 4: // 4
			if(day == 1){
				last_day = 31; //3月最後一天
				last_month = 3;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 4;
				last_year = year;
			}
			break;
		case 5:
			if(day == 1){
				last_day = 30; //4月最後一天
				last_month = 4;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 5;
				last_year = year;
			}
			break;
		case 6:
			if(day == 1){
				last_day = 31; //5月最後一天
				last_month = 5;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 6;
				last_year = year;
			}
			break;
		case 7:
			if(day == 1){
				last_day = 30; //6月最後一天
				last_month = 6;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 7;
				last_year = year;
			}
			break;
		case 8:
			if(day == 1){
				last_day = 31; //7月最後一天
				last_month = 7;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 8;
				last_year = year;
			}
			break;
		case 9:
			if(day == 1){
				last_day = 31; //8月最後一天
				last_month = 8;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 9;
				last_year = year;
			}
			break;
		case 10:
			if(day == 1){
				last_day = 30; //9月最後一天
				last_month = 9;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 10;
				last_year = year;
			}
			break;
		case 11:
			if(day == 1){
				last_day = 31; //10月最後一天
				last_month = 10;
				last_year = year;
			}else{
				last_day = day-1;
				last_month = 11;
				last_year = year;
			}
			break;
	}
	var tempYear = last_year.toString();
	var tempMonth= (Math.floor(last_month/10)==0)?("0" + last_month.toString()):(last_month.toString());
	var tempDay  = (Math.floor(last_day/10)==0)?("0" + last_day.toString()):(last_day.toString());

	return tempYear+tempMonth+tempDay;
}

module.exports = {

	home_table1 : async(date_param) => {

		var date = S(S(date_param).splitLeft(" ")[0]).replaceAll("-","").s; // get today data
		var url = 'mongodb://localhost:27017/stock';
		var mongodb = new mongo(url);
		var table1_data = await mongodb.get({TimeStamp:date}, "tradingShort");
		while(table1_data.length == 0){
			date = date_check(date);
			table1_data = await mongodb.get({TimeStamp:date},"tradingShort");
		}

		return table1_data;
	},

	market_all : async() => {
		var url = 'mongodb://localhost:27017/stock';
		var mongodb = new mongo(url);
		var market_data = await mongodb.get({}, "market");
		return market_data;
	},

	market : async(date_param) => {
		var param = '';
		var tempParam = '';
		if(S(date_param).length == 8){
			tempParam = (S(S(date_param).substr(0,4)).toInt() - 1911).toString() + S(date_param).substr(4,2) + S(date_param).substr(6,2);
		}else{
			tempParam = date_param;
		}
		console.log(tempParam);
		if(S(tempParam).length%2==0){
			param = ' ' + S(tempParam).substr(0,2) + '/' + S(tempParam).substr(2,2) + '/' + S(tempParam).substr(4,2);
		}else{
			param = S(tempParam).substr(0,3) + '/' + S(tempParam).substr(3,2) + '/' + S(tempParam).substr(5,2);
		}
		
		console.log(param);
		var url = 'mongodb://localhost:27017/stock';
		var mongodb = new mongo(url);
		var market_data = await mongodb.get({date:param}, "market");
		return market_data;
	},

	industry_cement : async() => {
		var date = S(S(dateTime()).splitLeft(" ")[0]).replaceAll("-","").s;
		console.log('dateTime : ' + date);

		var url = 'mongodb://localhost:27017/industry';
		var mongodb = new mongo(url);
		var cement_data = await mongodb.get({date:date}, "cement");
		while(cement_data.length == 0){
			date = date_check(date);
			cement_data = await mongodb.get({date:date}, "cement");
		}
		console.log(cement_data);
		return cement_data;
	}
}

