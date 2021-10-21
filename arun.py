import  pymysql
def abc():

    try:
        con = pymysql.connect(host="localhost", user="root", password="Root", database="login")
        cur = con.cursor()
        cur.execute("Select * from Details where Id= %s",b)
        myresult=cur.fetchall()
        T_Name=myresult[0][1]
        To=myresult[0][2]
        from_d = myresult[0][3]
        print(T_Name)




        con.commit()
        con.close()
        #messagebox.showerror("Success", f"Reservation successful", parent=root)


    except Exception as es:
        pass
        #messagebox.showerror("Errors, f"Error due to:(str(es))", parent=root)
abc()

