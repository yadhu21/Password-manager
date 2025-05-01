import sqlite3


class DbOperations:
    
    
    
    def connect_to_db(self):
        conn=sqlite3.connect("password_record.db")
        return  conn
    


    
    
    def create_table(self,table_name="password_info"):
        conn=self.connect_to_db()
        query=f'''
        CREATE TABLE IF NOT EXISTS {table_name}(
            ID INTEGER PRIMARY KEY NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            website TEXT NOT NULL,
            username VARCHAR(200),
            password VARCHAR(50),
            question VARCHAR(200),
            answer VARCHAR(50),
            user VARCHAR(50)
            
        );
        '''
        with conn as conn:
            cursor=conn.cursor()
            cursor.execute(query)
    
    
    
    def create_record(self,data,table_name="password_info"):
        website=data["website"]
        username=data["username"]
        password=data["password"]
        question=data["question"]
        answer=data["answer"]
        user=data["user"]
        conn=self.connect_to_db()
        query=f'''
        INSERT INTO {table_name}("website","username","password","question","answer","user") VALUES
            ( ?, ?, ?, ?, ?, ?)
        ;
        '''
        with conn as conn:
            cursor=conn.cursor()
            cursor.execute(query,(website,username,password,question,answer,user))



    def show_records(self,data_from_main,table_name="password_info"):
        
        conn=self.connect_to_db()
        query=f'''
        SELECT * FROM {table_name} WHERE  user= ?
        
        ;
        '''
        with conn as conn:
            cursor=conn.cursor()
            list_records=cursor.execute(query,(data_from_main,))
            return list_records
        
    def update_record(self,data,table_name="password_info"):
        ID=data["ID"]
        website=data["website"]
        username=data["username"]
        password=data["password"]
        question=data["question"]
        answer=data["answer"]
        conn=self.connect_to_db()
        query=f'''
        UPDATE {table_name} SET website= ?,username= ?,
        password= ? ,question= ?,answer= ? WHERE ID= ?
        
        ;
        '''
        with conn as conn:
            cursor=conn.cursor()
            cursor.execute(query,(website,username,password,question,answer,ID))

    def delete_record(self,ID,table_name="password_info"):
        
        conn=self.connect_to_db()
        query=f'''
        DELETE FROM {table_name} WHERE ID= ?
        
        ;
        '''
        with conn as conn:
            cursor=conn.cursor()
            cursor.execute(query,(ID,))



        
            
