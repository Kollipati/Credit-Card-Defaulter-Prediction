# from cassandra.auth import PlainTextAuthProvider
# from cassandra.cluster import Cluster
#
# from application_logging.logger import App_Logger
#
# cloud_config = {'secure_connect_bundle': '/mnt/sda3/iNeuron/download/cassandra/secure-connect-creditcarddefault.zip'}
# auth_provider = PlainTextAuthProvider('xCkoBluHClSAExeGJBBINUrc',
#                                       '4t+B27o7hN9gf-Eabde0EmFTOGPcUMRYNbGdZ2sbYI3FyRW8QmbRQ0bJLAnw,,LGJc2vcyklHC5ECQ4nCYNQPMMOjUtHEd-IgxSIQfU6z7YgzXq2zMsalNy,z92WrNLz')
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
#
#
# class dBOperation:
#     """
#           This class shall be used for handling all the SQL operations.
#
#           Written By: swapnil sonawane
#           Version: 1.0
#           Revisions: None
#
#           """
#
#     def __init__(self):
#         self.path = "Traninig_Database/"
#         self.badFilePath = "Traning_Raw_files_validated/Bad_Raw"
#         self.goodFilePath = "Training_Raw_files_validated/Good_Raw"
#         self.logger = App_Logger()
#
#     def DataBaseConnection(self):
#         """
#                         Method Name: dataBaseConnection
#                         Description: This method creates the database with the given name and if Database already exists then opens the connection to the DB.
#                         Output: Connection to the DB
#                         On Failure: Raise ConnectionError
#
#                          Written By: swapnil sonawane
#                         Version: 1.0
#                         Revisions: None
#
#                         """
#         try:
#             session = cluster.connect()
#             file = open("Training_Logs/DataBaseConnectionLog.txt", "a+")
#             self.logger.log(file, "Connection established successfully!!")
#             file.close()
#         except ConnectionError as e:
#             file = open("Training_Logs/DataBaseConnectionLog.txt", "a+")
#             self.logger.log(file, "Error while establishing the connection :: %s" % e)
#             file.close()
#             raise e
#
#     def create_table(self):
#         """
#                Method Name: createTableDb
#                Description: This method creates a table in the given database which will be used to insert the Good data after raw data validation.
#                Output: None
#                On Failure: Raise Exception
#                Written By: swapnil sonawane
#                Version: 1.0
#                Revisions: None
#                """
#         file = open("Training_Logs/DataBaseTableLog.txt", "a+")
#         try:
#             session = cluster.connect()
#             for row in session.execute("SELECT keyspace_name, table_name FROM   system_schema.tables;"):
#                 if row[0] == "data":
#                     pass
#         except:
#             pass
