import sys
import os
import traceback

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))        
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)                  
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger(__file__)

class DocumentPortalException (Exception):
    """Custom Exception for Document Portal Application"""
    def __init__(self, error_message:str, error_details:sys):
        _, _, exec_tb = error_details.exc_info()
        self.file_name = exec_tb.tb_frame.f_code.co_filename
        self.line_number = exec_tb.tb_lineno
        self.error_message = str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))

        
    def __str__(self):
        return f"""Error in [{self.file_name}] at line [{self.line_number}] 
        Message: {self.error_message} 
        Traceback:
        {self.traceback_str}
        """

            
if __name__ == "__main__":
    try:
        # Simulate an error
        a= 1 / 0
        print(a)
    except Exception as e:
        app_exec = DocumentPortalException(e, sys)
        logger.error(app_exec)
        raise app_exec
