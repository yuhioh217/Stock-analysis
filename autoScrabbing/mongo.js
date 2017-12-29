var MongoClient = require("mongodb").MongoClient;


module.exports = mongo = function(url){
	this.url = url;
}

mongo.prototype.connect = function(){
	var self = this;
	return new Promise((resolve,reject)=>{
		MongoClient.connect(self.url, function(err, db) {
			if(err)reject(err);
			resolve(db);
		});
	})
}

mongo.prototype.insert_date = function(data, collection){
	return new Promise((resolve,reject)=>{
		collection.insert(data, (err,result)=>{
			if (err) {
				reject(err)
			}
			resolve(result);
		})
	})
}


mongo.prototype.insert = async function(data, collection){
	var self = this;
	var db = await self.connect();
	var collect = db.collection(collection);
	var insert  = await self.insert_date(data, collect);
	db.close();
}


mongo.prototype.find_data = function(collection){
	return new Promise((resolve, reject) => {
		collection.find({}).toArray(function(err, result) {
		    if(err)reject(err);
		    resolve(result);
		});
	});

}

mongo.prototype.find = async function(collection){
	var self = this;
	var db = await self.connect();
	var collect = db.collection(collection);
	var result = await self.find_data(collect);
	db.close();
	console.log(result);

}

mongo.prototype.remove_data = function(collection){
	return new Promise((resolve, reject) => {
		collection.remove({},function(err, result) {
		    if(err)reject(err);
		    resolve(result);
		});
	});
}

mongo.prototype.remove = async function(collection){
	var self = this;
	var db = await self.connect();
	var collect = db.collection(collection);
	var delete_data = await self.remove_data(collect);
	var result = await self.find_data(collect);
	db.close();
	console.log(result);
}