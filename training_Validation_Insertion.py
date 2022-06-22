from DataTransform_Training.DataTransformation import dataTransform
from Training_Raw_data_validation.rawValidation import Raw_Data_validation
from application_logging import logger


class train_validation():
    def __init__(self, path):
        self.raw_data = Raw_Data_validation(path)
        self.dataTransform = dataTransform()
        self.file_object = open('Training_Logs/Training_Main_Log.txt', 'a+')
        self.log_writter = logger.App_Logger()

    def train_validation(self):
        try:
            self.log_writter.log(self.file_object, "Start of Validation on files for Training")
            # extracting values from prediction schema
            LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, noofcolumns = self.raw_data.valuesFromSchema()
            # getting the regex defined to validate filename
            regex = self.raw_data.manualRegexCreation()
            # validate filename in the file
            self.raw_data.validateFileNameRaw(regex, LengthOfDateStampInFile, LengthOfTimeStampInFile)
            # validate column length in the file
            self.raw_data.validateColumnLength(noofcolumns)
            # validate if any column has all values missing
            self.raw_data.validateMissingValuesInWholeColumns()
            self.log_writter.log(self.file_object, "Raw data validation Complete!!")

            self.log_writter.log(self.file_object, "Starting Data Transformation!!")
            # replace blanks in the csv file with "Null" values to insert into table
            self.dataTransform.replaceMissingWithNull()

            self.log_writter.log(self.file_object, "Data Transformation Complete!!")
        except Exception as e:
            raise e
