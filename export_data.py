import pandas as pd
from datetime import datetime

class ExportData:
    def __init__(self, data, type):
        self.data = data
        self.type = type

    def export(self):
        now = datetime.now()
        current_time_formatted = now.strftime("%d-%m-%Y_%H-%M-%S")
    
        df1 = pd.DataFrame(self.data)
        # Export data with a unique filename
        with pd.ExcelWriter(self.type + '_' + current_time_formatted + '.xlsx') as excel_writer:
            df1.to_excel(excel_writer, sheet_name='Sheet1', index=False)