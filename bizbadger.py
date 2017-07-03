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


def gross_margin_calculations(revenue, variable_costs, sales_costs=0, no_products=1, fixed_costs=0):
	cogs = variable_costs + sales_costs
	gross_profit = revenue - cogs
	gross_margin = gross_profit/float(revenue)	
	gross_profit_per_product = gross_profit/float(no_products)
	break_even = fixed_costs/gross_profit_per_product
	# returns the gross profit, the gross margin and the number of ;products needed to be sold to reach break even
	return gross_profit, gross_margin, break_even


def net_profit (revenue, variable_costs, sales_costs=0, no_products=1, fixed_costs=0, other_expenses=0):
	#subtracts all costs and for margin divides it bu floating revenue; returns float
	# other_expenses might mean interest, amortization, depreciation, taxez
	return (revenue-variable_costs-sales_costs-fixed_costs-other_expenses), (revenue-variable_costs-sales_costs-fixed_costs-other_expenses)/float(revenue)



#functions that calculate prices before and after vat
def price_before_vat(price_after_vat, vat):
	return price_after_vat/float(1+vat)

def price_after_vat(price_before_vat, vat):
	# vat will be decimal
	return price_before_vat*float(1+vat)

def vat(price_before_vat, price_after_vat):
	return (price_after_vat-price_before_vat)/float(price_before_vat)



# returns - investement, equity, assets

def ROI(gain_investment, cost_investment):
	return (gain_investment-cost_investment)/float(cost_investment)


def ROA(net_income, total_assets):
	return (net_income)/float(total_assets)
	#net_income = net_profit()


def ROE(net_income, shareholder_equity):
	return (net_income)/float(shareholder_equity)
	#net_income = net_profit()


def conversionRate(transactions, total_interactions):
	# total_interactions is very generic - can mean visits, interactions with a specific page; it should be defined for each need
	# will return a float
	if total_interactions!=0:
		return transactions/float(total_interactions)
	else:
		return 0


def repeatRate(customers_with_second_purchase, total_customers_purchase):
	# it is applied only on an X period of time
	if (total_customers_purchase!=0):
		return customers_with_second_purchase/float(total_customers_purchase)
	else:
		return 0


def renewalRate(clients_renew, clients_end):
	#clients_renew = total clients who renew after a period of time
	#clients_end = total clients whose previous licenses came to an end

	if clients_end!=0:
		return clients_renew/float(clients_end)
	else:
		return 0


def referralConversion(convertedReferrals, totalReferralInvitations):
	if totalReferralInvitations!=0:
		return convertedReferrals/float(totalReferralInvitations)
	else:
		return 0






















