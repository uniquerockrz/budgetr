import os
import warnings
import logging

class Ledger:

    """Contains all functions for managing the ledger.
    
    You can use this to init a ledger if it doesn't exists.
    """
    
    def __init__(self, data_folder_path: str) -> None:
        """The init function to call when you start using a ledger

        Args:
            data_folder_path (str): The folder where all the data for the ledger is stored
        """

        self.data_folder_path = data_folder_path
        logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)
        logging.debug('Init Transactions')
        if (os.path.exists(self.data_folder_path) and os.path.isdir(self.data_folder_path)):
            logging.debug('Data folder found')
            pass
        else:
            logging.warning('Data folder path is not a valid path')
            warnings.warn('Data folder path is not a valid path!')
        pass

    def say_hello():
        print('Hello, World!')