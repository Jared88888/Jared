def total_cost(cost):
    tax = cost * 0.09 #calculate the 9 percent
    cost_with_tax = cost + tax #calculate with tax included
    return cost_with_tax #return

def discount(cost):
    if total_cost(cost) >= 50 and total_cost(cost) < 100:
        discounted_cost = total_cost(cost) - (0.05 * total_cost(cost)) #minus 5 percent
    elif total_cost(cost) > 100:
        discounted_cost =  total_cost(cost) - (0.10 * total_cost(cost)) #minus 10 percent
    else:
        discounted_cost = total_cost(cost) #even if no discount have to return
    return discounted_cost

def reward_points(discounted_cost):
    reward_points = discounted_cost // 1 * 3  #floor divide to get whole number get rid of the cents
    return reward_points

def voucher(discounted_cost, first_name):
    if discounted_cost > 25 and discounted_cost <= 50:
        voucher_code = first_name[:3] + "05PERCENT"
    elif discounted_cost > 50:
        voucher_code = first_name[:3] + "10PERCENT"
    return voucher_code

fname = input("Enter your first name: ")
cost1 = int(input("Enter cost: "))
print(f"""
Receipt
Total cost: {total_cost(cost1)}   
Discounted cost: {discount(cost1)} 
Reward points: {reward_points(discount(cost1))}
""")

