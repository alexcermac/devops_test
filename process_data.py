from export_data import ExportData
from datetime import date
from datetime import datetime

class ProcessData:
    def __init__(self, data):
        self.data = data

    def list_suspended_licenses(self):
        suspended_licenses = []
        for item in self.data:
            if item['suspendat'] == True:
                suspended_licenses.append(item)

        ExportData(suspended_licenses, 'suspended').export()

    def extract_valid_licenses(self):
        today = date.today()
        
        valid_licenses = []
        for item in self.data:
            expiration_date = datetime.strptime(item['dataDeExpirare'], '%d/%m/%Y').date()
            if expiration_date > today:
                valid_licenses.append(item)
        print(valid_licenses)

        ExportData(valid_licenses, 'valid').export()