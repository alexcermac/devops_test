import pandas as pd
from datetime import datetime

class ExportData:
    def __init__(self, data, type):
        self.data = data
        self.type = type

    def export(self):
        now = datetime.now()
        current_time_formatted = now.strftime("%d-%m-%Y_%H-%M-%S")

        if(self.type == 'by_category'):
            data_frame = pd.DataFrame(list(self.data.items()), columns=['Category', 'Count'])
            with pd.ExcelWriter(self.type + '_' + current_time_formatted + '.xlsx') as excel_writer:
                data_frame.to_excel(excel_writer, sheet_name='Sheet1', index=False)
        else:
            data_frame = pd.DataFrame(self.data)
            # Export data with a unique filename
            with pd.ExcelWriter(self.type + '_' + current_time_formatted + '.xlsx') as excel_writer:
                data_frame.to_excel(excel_writer, sheet_name='Sheet1', index=False)