import logging
import os
import sys

from datetime import datetime


class log(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        # formate string in day-month-year and hrs-min-sec manner
        dt_string = datetime.now()
        dt_string = dt_string.strftime("%d/%m/%Y--%H:%M:%S")

        # Start time
        start = datetime.now()

        # Function name
        func_name = self.func.__name__

        # End time
        end = datetime.now()

        # Getting current working directory
        cwd = os.getcwd()

        # assign folder name to the object
        folder = 'Log'
        self.newpath = os.path.join(cwd, folder)

        # try and except block if the directory exists
        try:

            # make directory if it doesn't exists
            os.makedirs(self.newpath, exist_ok=True)

            # result of called function
            result = self.func(self, *args, **kwargs)

            # Message to be passed in log file
            self.message = """

                        Function: {} {}
                        Result : {}
                        Execution Time : {}
                        Memory : {} bytes
                        Date : {}
            """.format(
                func_name,
                args,
                result,
                end - start,
                sys.getsizeof(self.func),
                dt_string)

            # call method to write logs in file
            self.write_file()

            # return result
            return result

        except Exception as e:

            # call method to write in file
            self.message = "Exception occurred"
            self.write_file()
            raise e

    def write_file(self):

        # create the logging object
        logger = logging.getLogger()

        # set logging level
        logger.setLevel(logging.DEBUG)

        # create console handler
        ch = logging.StreamHandler()

        # set console level
        ch.setLevel(level=logging.DEBUG)

        # create formatter and add it to ch object
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # set logging file handler
        fh = logging.FileHandler('{}/log.log'.format(self.newpath), mode='a')
        fh.setFormatter(formatter)

        # set fh level to debug
        fh.setLevel(logging.DEBUG)

        # add handler to logger
        logger.addHandler(fh)

        # debug to store the line in log file
        logger.debug("Function execution started of :  " + self.func.__name__)

        # debug to store message in log file
        logger.debug(self.message)
