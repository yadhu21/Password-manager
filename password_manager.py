from tkinter import Tk,Label,Button,Entry,Frame,END,INSERT,Event,messagebox,Toplevel,Pack
from  tkinter import ttk
from db_operations import DbOperations
import random,pyperclip

import sys

class root_window:
    
    def __init__(self,root,db):
        self.db=db
        self.root=root
        self.root.title("Password Manager")
        self.root.config(bg="plum")
        self.root.geometry("1375x700+40+40")
        head_title=Label(self.root,text="Password Manager",width=40,bg="yellow",font=("Caslon Italic",20),padx=10,pady=10,justify="center").grid(columnspan=4,padx=110,pady=10)
        self.crud_frame=Frame(self.root,highlightbackground="black",highlightthickness=2,padx=20,pady=30)
        self.crud_frame1=Frame(self.root,highlightbackground="black",highlightthickness=2,padx=5,pady=5,height=20)
        
        self.crud_frame.grid()
        
        
        self.create_entry_labels()
        
        self.create_entry_boxes()
        self.create_buttons()
        self.search_entry=Entry(self.crud_frame,width=19,font=("Ariel",14),bg="lightgrey")
        self.search_entry.grid(row=self.row_no,column=self.col_no)
        self.col_no+=1
        Button(self.crud_frame,command=self.search,text="Search",width=20,bg="yellow",font=("Ariel",13)).grid(row=self.row_no,column=self.col_no,padx=5,pady=2)
        Button(self.crud_frame,command=self.clear,text="Clear",width=20,bg="violet",font=("Ariel",13)).grid(row=self.row_no,column=self.col_no+1,padx=5,pady=2)
        self.create_records_tree()
        self.crud_frame1.grid()
        Button(self.crud_frame1,command=self.logout,text="Logout",width=20,bg="pink",font=("Ariel",13),).grid(row=10,column=0,padx=5,pady=2)
        Button(self.crud_frame1,command=self.generator,text="Generator",width=20,bg="orange",font=("Ariel",13)).grid(row=10,column=1,padx=5,pady=2)


    def create_entry_labels(self):
        self.col_no=self.row_no=0
        Labels_info=("ID","Website","Username","Password","Question","Answer")
        for labels_info in Labels_info:
            Label(self.crud_frame,text=labels_info,bg="light sea green",fg="black",font=("Ariel",12),padx=5,pady=2).grid(row=self.row_no,column=self.col_no,padx=5,pady=2)
            self.col_no+=1
        

        
    def create_buttons(self):
        self.row_no+=1 
        self.col_no=0
        buttons_info=(("Save","green",self.save_record),("Update","blue",self.update_record),("Delete","red",self.delete_record),("Copy Password","cyan",self.copy_password),("Show All record","purple",self.show_record))
        for buttons_info in buttons_info:
            if buttons_info[0]=="Show All record":
                self.row_no+=1
                self.col_no=0
            Button(self.crud_frame,text=buttons_info[0],bg=buttons_info[1],command=buttons_info[2],fg="black",font=("Ariel",12),padx=5,pady=2,width=20).grid(row=self.row_no,column=self.col_no,padx=5,pady=2)
            self.col_no+=1
    
        
    def create_entry_boxes(self):
        self.row_no+=1 
        self.entry_boxes=[]
        self.col_no=0
        for i in range(6):
            show=""
            if(i==3):
                show="*"
            entry_box=Entry(self.crud_frame,width=19,background="lightgrey",font=("Ariel",14),show=show)
            entry_box.grid(row=self.row_no,column=self.col_no,padx=5,pady=2)
            self.col_no+=1
            self.entry_boxes.append(entry_box)







    def generator(self):
        
        window=Toplevel(root)
        
        window.config(background="plum")
        
        
        window.geometry("250x200+600+200")
        window.title("Random password generator")
        
        
        Label(window,text="Random Password Generator",bg="light sea green",fg="black",font=("Ariel",12),padx=5,pady=2).grid(padx=3,pady=2)
        frame=Frame(window,highlightbackground="black",highlightthickness=2,padx=20,pady=30)
        frame.grid()
        
        
        button1=Button(frame,command=self.process,text="Generate",width=20,bg="pink",font=("Ariel",13),).grid(row=10,column=30,padx=5,pady=2)
        if button1==True:
            
            window.after(900,window.destroy)
            

        

      
    def process(self):
        length = 10
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special = ['@', '#', '$', '%', '&', '*']
        all = lower + upper + num + special
        ran = random.sample(all,length)
        password = "".join(ran)
        messagebox.showinfo('Result', 'Your password {} \n\nPassword Copied to Clipboard'.format(password))
        messagebox.showinfo("Copied","Your Password is copied into password block")
        x=0
        for entry in (self.entry_boxes):
            
            if(x==3):
                entry.insert(0,password)
            x+=1
        pyperclip.copy(password)

        
        
        
        


    def logout(self):
        root.destroy()
    
    def search(self):
        x=0
        website=self.search_entry.get()
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        record_list=self.db.show_records(data_from_main)
        for record in record_list:
            if(website==record[3]):
                self.records_tree.insert("",END,values=(record[0],record[3],record[4],record[5]))
                self.showmessage("Found","Enrty found")
                x=1
        if(x==0):
            self.showmessage("Error","Enrty not found")

        

        

    

    def save_record(self):
        website=self.entry_boxes[1].get()
        username=self.entry_boxes[2].get()
        password=self.entry_boxes[3].get()
        question=self.entry_boxes[4].get()
        answer=self.entry_boxes[5].get()
        user=data_from_main

        
        
        

        if(len(password)>7):
            data={"website":website,"username":username,"password":password,"question":question,"answer":answer,"user":user}
            self.db.create_record(data)
            self.clear()
        else:
            self.showmessage("Error","Short Password")
        
        self.show_record()

    def update_record(self):
        ID=self.entry_boxes[0].get()
        website=self.entry_boxes[1].get()
        username=self.entry_boxes[2].get()
        password=self.entry_boxes[3].get()
        question=self.entry_boxes[4].get()
        answer=self.entry_boxes[5].get()
        data={"ID":ID,"website":website,"username":username,"password":password,"question":question,"answer":answer}
        self.db.update_record(data)
        self.show_record()
        self.clear()


    def clear(self):
        for entry in (self.entry_boxes):
            entry.delete(0,END)
        
        


        





    def create_records_tree(self):
        columns=("ID","Website","Username","Password","Question","Answer")
        self.records_tree=ttk.Treeview(self.root,columns=columns,show="headings")
        self.records_tree.heading("ID",text="ID")
        self.records_tree.heading("Website",text="Website")
        self.records_tree.heading("Username",text="Username")
        self.records_tree.heading("Password",text="Password")
        self.records_tree.heading("Question",text="Question")
        self.records_tree.heading("Answer",text="Answer")
        self.records_tree["displaycolumns"]=("Website","Username")
        
        def item_selected(event):
            for selected_item in self.records_tree.selection():
                item=self.records_tree.item(selected_item)
                record= item["values"]
                for entry_box, item in zip(self.entry_boxes,record):
                    entry_box.delete(0, END)
                    entry_box.insert(0, item)
        self.records_tree.bind("<<TreeviewSelect>>",item_selected)
        self.records_tree.grid()

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry_boxes[3].get())
        message="Password copied"
        title="Copy"
        if self.entry_boxes[3].get()=="":
            message="Box is empty"
            title="Error"
        self.showmessage(title,message)
        self.clear()


    
    def showmessage(self,title_box:str=None,message:str=None):
        TIME_TO_WAIT=900
        root=Toplevel(self.root)
        background="green"
        
        root.geometry("200x30+600+200")
        root.title(title_box)
        Label(root,text=message,background=background,font=("Ariel",15),fg="white").pack(padx=4,pady=2)
        
        try:
            root.after(TIME_TO_WAIT,root.destroy)
        except Exception as e:
            print("Error occured ",e)

    def delete_record(self): 
        ID=self.entry_boxes[0].get()
        self.db.delete_record(ID)
        self.show_record()
        self.clear()
        

    
    
    
    def show_record(self):
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        record_list=self.db.show_records(data_from_main)
        for record in record_list:
            self.records_tree.insert("",END,values=(record[0],record[3],record[4],record[5],record[6],record[7]))







    

if __name__=="__main__":
    db_class=DbOperations()
    db_class.create_table()
    if len(sys.argv) > 1:
        data_from_main = sys.argv[1]
        
        
    
    
    


    root=Tk()
    root_class=root_window(root,db_class)
    root.mainloop()
