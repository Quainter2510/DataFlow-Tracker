from dataclasses import dataclass

@dataclass
class Grade:
    user_id: str
    oauth_consumer_key: str
    lis_result_sourcedid: str 
    lis_outcome_service_url: str 
    is_correct: str 
    attempt_type: str 
    created_at: str