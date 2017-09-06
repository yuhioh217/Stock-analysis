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

	table5 : async () => {

		var date = S(S(dateTime()).splitLeft(" ")[0]).replaceAll("-","").s; // get today data
		var url = 'mongodb://localhost:27017/foreignInvestment';
		var mongodb = new mongo(url);
		var table5_data = await mongodb.get({TimeStamp:date}, "Table5");

		if(table5_data.length == 0){
			var last_date = console.log(date_check(date)); // if today's data don't catch, use tomorrow's data. 
			table5_data = await mongodb.get({TimeStamp:last_date},"Table5");
		}

		var table5_sort = table5_data.sort(sortByProperty('Rank'));
		return table5_sort;
	}
}

