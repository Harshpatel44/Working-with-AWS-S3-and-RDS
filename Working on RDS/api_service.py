import mysql.connector
import generatePassword


class RdsApi:

    def connectRDS(self,host,database,user,password):
        return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)

    def addData(self,user_id,password):
        encrypted_password=generatePassword.encryptPassword(password) #encrypt password
        object = self.connectRDS("database-1.ceofxztsta8i.us-east-1.rds.amazonaws.com", "sampleDB", "admin",
                                 "amazonrds")
        cur = object.cursor()
        query = 'INSERT INTO users (userID,Password) VALUES ({0},"{1}")'.format(str(user_id),encrypted_password)
        cur.execute(query)
        object.commit()
        cur.close()
        object.close()

    def fetchData(self,userID):
        object = self.connectRDS("database-1.ceofxztsta8i.us-east-1.rds.amazonaws.com", "sampleDB", "admin",
                                 "amazonrds")
        cur=object.cursor()
        query = "SELECT Password FROM users WHERE userID="+str(userID)
        cur.execute(query)
        print(generatePassword.decryptPassword(cur.fetchone()[0]))     #get decrypted password
        object.commit()
        cur.close()
        object.close()


api = RdsApi()
api.addData(1,"harsh")
api.fetchData(1)














