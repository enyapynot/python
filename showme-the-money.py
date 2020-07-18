payrate = eval (input ("whatchoo git an hour?"))
hours_worked = eval (input ("how many hours you sweated yo ass for?"))

if hours_worked <= 40:
    final_pay = hours_worked * payrate
else:
    final_pay = hours_worked * payrate
    overtime = (hours_worked - 40) * 0.5 * payrate
    final_pay = final_pay + overtime

print ("Here's your green ", final_pay)
