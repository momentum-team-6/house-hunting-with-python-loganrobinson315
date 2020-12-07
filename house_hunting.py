# Write your code here
total_cost = float(input('Enter dream home Value'))
annual_salary = float(input('Enter your salary'))
portion_saved_input = float(input('Enter your % portion saved'))




def calculate_months(total_cost, annual_salary, portion_saved_input):
    months = 0
    current_savings = 0
    down_payment = total_cost*0.25
    portion_saved = (annual_salary/12*portion_saved_input) + ((annual_salary/12*portion_saved_input)*0.04)
    if current_savings>down_payment:
        print('You have enough money!')
        return
    while current_savings<down_payment:
        months += 1
        current_savings += portion_saved
    print(months)
    

calculate_months(total_cost, annual_salary, portion_saved_input)


