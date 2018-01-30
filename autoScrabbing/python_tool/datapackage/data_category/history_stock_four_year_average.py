from lib.DataAnalyze.DateChecking import DateChecking

if __name__ == '__main__':
	a = DateChecking()
	# find result index -> array name -> could search many object, so ues index to select-> search field bt field name 
	a.lock_stock('1101')
	if a.include_data_by_date('1070104'):
		print a.fetch_data('end')


	