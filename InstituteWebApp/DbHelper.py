import matplotlib.pyplot as plt

class DataBaseHelper:

    def get_db(self):
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        db = client.RestaurentDb
        return db

#add_student adding data name address phoneno
    def add_student(self,db,name,address,phoneno):
        db.student.insert({"name": name,"phoneno":phoneno,"address":address})
        return "student iformation inserted in db"

    # add_student adding data name address phoneno
    def add_menu(self, db, name, price, description):
        db.menuDetails.insert({"name": name, "price": price, "description": description})
        return " if menu data inserted in db"
    def getStudentDetails(self, db):
        results = db.student.find()
        print("results", results)
        studentlist = []
        studentDict={}
        for result in results:
            studentlist.append(result)

        print("studentlist", studentlist)
        studentDict={'studentlist': studentlist}
        return studentDict

    def getMenuDetails(self, db):
        import numpy as np



        results = db.menuDetails.find()
        print("results", results)
        menulist = []
        studentDict = {}

        for result in results:
            menulist.append(result)

        print("menulist", menulist)
        studentDict = {'menuDetails': menulist}
        # N = 50
        # x = np.random.rand(N)
        # y = np.random.rand(N)
        # plt.scatter(x, y)
        # plt.show()
        return studentDict

    def getFacultyDetails(self, db):
        results = db.faculty.find()
        print("results", results)
        facultylist = []
        facultyDict={}
        for result in results:
            facultylist.append(result)

        print("facultylist", facultylist)
        facultyDict={'facultylist': facultylist}
        return facultyDict

