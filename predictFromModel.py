from application_logging import logger
from file_operations import file_methods


class prediction:
    def __init__(self, data):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        self.data = data
        self.columns = [ 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4',
                         'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                         'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6' ]

    def predictionFromModel(self):
        try:
            self.log_writer.log(self.file_object, "Start of Prediction")
            # data = pd.DataFrame(self.data, columns = self.columns)
            # print("1st data: \n", self.data)

            # calling the scaled object for standardization
            file_loder = file_methods.File_Operation(self.file_object, self.log_writer)
            scaled = file_loder.load_model("scaler")
            self.log_writer.log(self.file_object, "Scaled model loaded")

            X = scaled.transform(self.data)
            # X = pd.DataFrame(scaled_data, columns = self.columns)
            # print("scaled data: \n", X)

            # loading the cluster model
            file_loader = file_methods.File_Operation(self.file_object, self.log_writer)
            kmeans = file_loader.load_model('Kmeans')
            self.log_writer.log(self.file_object, "Clustering model loaded")

            cluster = kmeans.predict(X)
            # print("cluster is: ", str(cluster))
            model_name = file_loader.find_correct_model_file(cluster[ 0 ])
            # print("\nModel Name: ", model_name)
            model = file_loader.load_model(model_name)
            result = model.predict(X)
            # print("\n Resutl is: ", result)

            return result
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % e)
            raise e
        return "none"
