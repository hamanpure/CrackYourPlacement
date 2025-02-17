import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    d = pd.DataFrame(student_data)
    d.rename(columns={0: 'student_id', 1: 'age'}, inplace=True)
    return d