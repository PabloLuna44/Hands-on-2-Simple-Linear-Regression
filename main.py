import pandas as pd
import model.regression as regression



dataset = pd.read_csv('datasets/benettonCase.csv')

x=dataset.iloc[:,0].values
y=dataset.iloc[:,1].values


regression= regression.regression(x,y)
b0,b1=regression.linear_regression()
print("B0:",round(b0))
print("B1:",round(b1))


print(f"Ecuación de Regresión: ŷ = {round(b0)} + {round(b1)}x")


advertising_values = [25, 28, 44, 54, 60] 

for x in advertising_values:
    y_pred = b0 + b1 * x  
    print(f"Advertising: {x}, Predicted Sales: {round(y_pred, 2)}")



