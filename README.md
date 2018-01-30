2018_0131_TASK_sprint1

=================

Change Log
-

* all_stock_collection.py => all stock info getting from API and save in Mongodb (db,collecion) => (industry,stock)
* category_stock_collection.py => category, child items and its stocks (a machine only do it once) 
* history_stock_collection => from 2015/1 to 2018/1 each stock history data fetch (now center market finish)
* update_date_field => change year from format 20180131 to 1070131 ROC date format.

## Python Tool Project Structure
```
.
├── all_stock_collection.py
├── category_stock_collection.py
├── history_stock_collection.py
├── update_date_field.py
├── lib
│   ├── ConfigLoader   #config loading task
│   ├── DataAnalyze    #data analyze process
│   ├── FetchPageData  #Fetch Data from API or webpag
│   ├── MongoDatabase  #MongoDB contorller
│   ├── StockLoader    #Stock info get and save/update to mongoDB
│   └── StockIdLoader  #Stock Array collect
│   
└── config
```

License
-
Licensed under the MIT License

Authors
-
Copyright(c) 2017 KE Jiang<<yuihoh217@gmail.com>>
