# Hands-on-2-Simple-Linear-Regression

This project demonstrates a simple linear regression model using Python. The model predicts sales based on advertising expenditure.

## Files

- `main.py`: The main script that loads the dataset, performs linear regression, and prints the results.
- `model/regression.py`: Contains the `regression` class that implements the linear regression algorithm.

```bash
    Hands-on-2-Simple-Linear-Regression/
    │
    ├── datasets/
    │   └── benettonCase.csv      
    │
    ├── model/
    │   └── regression.py         
    │
    ├── main.py                   
    └── README.md                 
```


The script will output the calculated values of the regression coefficients ( B_0 ) and ( B_1 ), the regression equation, and the predicted sales for a given set of advertising values

Example 

```bash
    B0: 168
    B1: 23
    Regression Equation: ŷ = 168 + 23x
    Advertising: 25, Predicted Sales: 753
    Advertising: 28, Predicted Sales: 824
    Advertising: 44, Predicted Sales: 1198
    Advertising: 54, Predicted Sales: 1433
    Advertising: 60, Predicted Sales: 1573
```



