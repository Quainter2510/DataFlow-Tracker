from grade_handler import GradeHandler
from database import DataBase
from api_parser import ApiParser
from loader import logger, config
from sheets_data_manager import SheetsDataManager
import schedule
import datetime 
import time


grade_handler = GradeHandler()
database = DataBase()
sheet_manager = SheetsDataManager()

def load_grade():
    parse_result = ApiParser.parse(datetime.datetime.now())
    grade_list = grade_handler.get_all_grades(parse_result)
    logger.info("Загрузка данных в базу данных")
    for grade in grade_list:
        database.insert_data(grade)
    logger.info(f"Загрузка данных в базу данных завершена. Добавлено {len(grade_list)} записей")



def fill_table():
    logger.info("Загрузка данных в google sheets")
    sheet_manager.update_runs_count(database.get_runs_count_by_last_day())
    sheet_manager.update_commit_count(database.get_commit_count_by_last_day())
    sheet_manager.update_seccess_commit_count(database.get_success_commit_count_by_last_day())
    sheet_manager.update_percent_seccess_decisions(database.get_percentage_correct_decisions_by_last_day())
    sheet_manager.update_unique_users(database.get_unique_users_by_last_day())
    task, decisions = database.get_most_popular_task_by_last_day()
    sheet_manager.update_most_popular_task(task)
    sheet_manager.update_max_decisions(decisions)
    
    
    
if __name__ == "__main__":
    schedule.every().day.at("23:59").do(fill_table) 
    schedule.every(config.api.interval).minutes.do(load_grade) 
    
    while True:
        schedule.run_pending()
        time.sleep(1)  # Чтобы не нагружать процессор
    