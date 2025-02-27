from .handler import Grade
from loader import logger
import json


class GradeHandler:
    
    def get_all_grades(self, data):
        grades = []
        for grade in data:
            gr = self.get_grade(grade)
            if gr != None:
                grades.append(gr)
        return grades

    def get_grade(self, grade):
        try:
            user_id = grade['lti_user_id']
            is_correct = grade['is_correct']
            attempt_type = grade['attempt_type']
            created_at = grade['created_at']
            passback_params = json.loads(grade['passback_params'].replace("'", '"'))
            oauth_consumer_key = passback_params['oauth_consumer_key']
            lis_result_sourcedid = passback_params['lis_result_sourcedid']
            lis_outcome_service_url = passback_params['lis_outcome_service_url']
        except KeyError as err:
            logger.error("Загружены неполные данные", exc_info=True)
            return None
        return Grade(user_id, 
                     oauth_consumer_key,
                     lis_result_sourcedid,
                     lis_outcome_service_url,
                     is_correct,
                     attempt_type,
                     created_at)