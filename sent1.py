import pandas as pd
import logging


class sentimentalana(object):
    def __init__ (self,filename,logger):
        self.filename=filename
        self.logger=logger
        
        
    def readfile(self):       
        """
        1. open a file 
        2. initialize a object to store the csv files
        3. read the file using pandas
        4. check whether the file is read using logger.info
        """
        df=pd.read_csv(self.filename,low_memory=False)
        self.logger.info('author={}, authority={}, host={},contents = {}'
                         .format(df['author'],df['authority'],df['host'],df['contents']))
        df['contents']=df['contents'].map(sentimentalana)
    
    def space(self,z):
        try:
            if re.match('\s+',z):
                return np.nan
            else:
                return z
            
            
if __name__ == '__main__' :
    logging.basicConfig(format = '%(asctime)s %(message)s',level ='INFO')
    logger = logging.getLogger('sentimentalana')
    obj = sentimentalana('merged_twitter_data_final.csv',logger)
    obj.readfile()
    obj.space()