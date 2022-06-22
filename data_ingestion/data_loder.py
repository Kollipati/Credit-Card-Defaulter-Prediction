import pandas as pd


class Data_Getter:
    """
        This class shall  be used for obtaining the data from the source for training.

        Written By: swapnil sonawane
        Version: 1.0
        Revisions: None

        """

    def __init__(self, file_object, logger_object):
        self.training_file = "Training_Raw_files_validated/Good_Raw/creditCardFraud_28011961_120210.csv"
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):
        """
                Method Name: get_data
                Description: This method reads the data from source.
                Output: A pandas DataFrame.
                On Failure: Raise Exception

                 Written By: swapnil sonawane
                Version: 1.0
                Revisions: None

                """
        self.logger_object.log(self.file_object, "Entered the get_data method of the Data_Getter class")
        try:
            self.data = pd.read_csv(self.training_file)  # reading the data file
            self.logger_object.log(self.file_object,
                                   "Data Load Successfully!. Exited the get_data method of Data_Getter class")
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   "Exception occured in get_data method of Data_Getter class. Exception message:: " + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   "Data Load Unsuccessful!. Exited the get_data method of Data_Getter class")
