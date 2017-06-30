def churn_rate(nr_customers_start, nr_customers_end):
	# returns the ratio between exisitng customers at the end of the period and total number of customers at the beginning of the period
	if (nr_customers_start==0): return -1
	elif (nr_customers_end!=0):
		return nr_customers_end/float(nr_customers_start)
	else:
		return 0


def ARPU(total_revenue, nr_customers, period_months=12):
	# return ARPU per total period of time and ARPU per month
	if (nr_customers==0): return -1
	else:
		return (total_revenue/float(nr_customers), (total_revenue/float(period_months))/float(nr_customers))


def LTV(average_revenue_per_user, period_months=1, life_time_period_months=12):
	# returns ARPU per month x life time period OR average revenue per user x fraction between(life_time_period_months/period_months)
	return (average_revenue_per_user*(life_time_period_months/float(period_months)))


def CPA(array_channel_cost):
	# returns an array of CPAs per channel and the total CPA. The first parameter is an array of objects. The first element of the object contains the sum
	# invested in that channel and the second is the number of acquired customers from that channel	
	CPA=[]
	total_cpa=0
	for a in array_channel_cost:
		CPA.append(a[0]/float(a[1]))
		total_cpa +=(a[0]/float(a[1]))
	return CPA, total_cpa


def salesGrowth_2periods(value_period1, value_period2):
	#returns growth for a 2 period
	return (value_period2-value_period1)/float(value_period1)

def salesGrowth_nperiods(arr_values):
	# n = number of periods; by default =2; a is the array with the values
	i=0
	growth_array=[]
	while i<(len(arr_values)-1):
		growth_array.append(salesGrowth_2periods(arr_values[i],arr_values[i+1]))
		i+=1
	return growth_array



