class regression:
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
        
    def linear_regression(self):

            sumX=self.x.sum()
            sumY=self.y.sum()
            sumXY=(self.x*self.y).sum()
            sumX2=(self.x**2).sum()
            n=len(self.x)
            
            b0=(((sumX2)*sumY ) - (sumX*sumXY)) / ((n*sumX2) - (sumX**2))
            b1=(((n*sumXY) - (sumX*sumY)) / ((n*sumX2) - (sumX**2)))
            
            return b0,b1
        
        
        
     
        
    
   