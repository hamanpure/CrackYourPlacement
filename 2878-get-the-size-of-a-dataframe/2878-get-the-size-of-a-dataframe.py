import pandas as pd

def getDataframeSize(d: pd.DataFrame) -> List[int]:
    r=c=0
    for i,j in d.items():
        c+=1
        r=len(j)
    return [r,c]
    
    