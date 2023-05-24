import pandas as pd

##tentInfoDF = pd.DataFrame(columns=['time', 'temperature', 'humidity'])
tentInfoDF = pd.read_csv('C:\\Users\\leona\\Desktop\\Raspberry Projects\\IndoorFarmManagement\\tentInfoDF.csv')


new_row = {'time': 5, 'temperature': 6, 'humidity':7}
##tentInfoDF.loc[len(tentInfoDF)] = new_row 
tentInfoDF = tentInfoDF.drop(index=1)


tentInfoDF.to_csv('C:\\Users\\leona\\Desktop\\Raspberry Projects\\IndoorFarmManagement\\tentInfoDF.csv', index=False)

print(tentInfoDF.head(5))
        
