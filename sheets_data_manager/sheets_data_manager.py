import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetsDataManager:
    def __init__(self):
        
        scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive.file',
                    'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('settings/dataflow-452213-c66212541e1a.json', scope)
        gc = gspread.authorize(credentials)
        self.sheet = gc.open('dataflow tracker').sheet1
        
    def update_runs_count(self, amount):
        self.sheet.update_cell(2, 2, amount)
        
    def update_submit_count(self, amount):
        self.sheet.update_cell(3, 2, amount) 
    
    def update_seccess_submit_count(self, amount):
        self.sheet.update_cell(4, 2, amount) 
    
    def update_percent_seccess_decisions(self, percent):
        self.sheet.update_cell(5, 2, percent) 
    
    def update_unique_users(self, amount):
        self.sheet.update_cell(6, 2, amount) 
    
    def update_most_popular_task(self, url):
        self.sheet.update_cell(7, 2, url) 
    
    def update_max_decisions(self, amount):
        self.sheet.update_cell(8, 2, amount) 
