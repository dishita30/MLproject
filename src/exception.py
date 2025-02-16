## EXCEPTION HANDLING
import sys
#provides various functions and variables that are used to manipulate different parts of the Python runtime environment

def error_message_detail(error,error_details:sys): #shows the error message and the details of the error in the sys
    def error_message_detail(error, error_details: sys):
        """
        Constructs a detailed error message including the file name, line number, and error message.
        Args:
            error (Exception): The exception instance that was raised.
            error_details (module): The sys module, used to extract detailed error information.
        Returns:
            str: A formatted string containing the file name, line number, and error message where the exception occurred.
        """
    _,_,exc_tb = error_details.exc_info() #gives info like on which file the error occured, the line number and the error message
    file_name= exc_tb.tb_frame.f_code.co_filename #gives the file name
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
  
class CustomException(Exception):
    def __init__(self,error_message, error_details:sys):
        super().__init__(error_message) #inherit the error message
        self.error_message = error_message_detail(error_message,error_details) #get the error message details
        #whenever this custom exception is raised, it will show the error message and the details of the error(inheriting the parent exception)
    
    def __str__(self):
        return self.error_message
