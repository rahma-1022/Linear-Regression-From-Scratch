import ast
import sys
import matplotlib.pyplot as plt 
x=ast.literal_eval(input ("Enter the values of x as a list "))
y=ast.literal_eval(input ("Enter the values of y as a list "))
if len(x)==len(y):
    pass
else:
    sys.exit("The number of X values is not equal to the number of Y values.\nTry again, making sure that the number of X and Y values is equal.")
n=len(x) 
sum_x = 0
for i in range (n):
    sum_x = sum_x + x[i]
print (f"The sum of x = {sum_x}")
sum_y = 0
for i in range (n):
    sum_y = sum_y + y[i]
print (f"The sum of y = {sum_y}")
sum_xy = 0
for i in range (n):
    sum_xy = sum_xy + x[i]*y[i]
print (f"The sum of x*y = {sum_xy}")
sum_x_square = 0
for i in range(n):
    sum_x_square = sum_x_square +x[i]*x[i]
print (f"The sum of x^2 = {sum_x_square}")    
square_of_sum_x = sum_x**2
print (f"The square of the sum of x ((sum of x)^2) = {square_of_sum_x}")
a1 =round((n*sum_xy-sum_x*sum_y)/(n*sum_x_square-square_of_sum_x) , 2)
print (f"a1 = {a1}")
a0 = round((sum_y-a1*sum_x)/n , 2)
print(f"a0 = {a0}")
print("-"*50)
print (f"The Equation of this linear regression is\n   Y = ({a0})+({a1})*X")
print("-"*50)

y_pred = [a0 + a1 * i for i in x]
plt.scatter(x, y, color='blue', label='Actual Data') 
plt.plot(x, y_pred, color='red', label='Regression Line') 
plt.title('Linear Regression From Scratch')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.show()