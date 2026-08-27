from __init__ import CURSOR,CONN
class Department:
    all={}
    def __init__(self,name,location,id=None):
        self.id=id
        self.name=name
        self.location=location
    def __repr__(self):
        return f"<Department {self.id}:{self.name},{self.location}>"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name):
            self._name=name
        else:
            raise ValueError("Name must be a non-empty string")
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self,location):
        if isinstance(location,str) and len(location):
            self._location=location
        else:
            raise ValueError("Location must be a non-empty string")
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS departments(
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT);
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS departments;"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql="""
        INSERT INTO departments(name,location)
        VALUES(?,?);
        """
        CURSOR.execute(sql,(self.name,self.location))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    @classmethod
    def create(cls,name,location):
        department=cls(name,location)
        department.save()
        return department
    def update(self):
        sql="""
        UPDATE departments
        SET name=?,location=?
        WHERE id=?;
        """
        CURSOR.execute(sql,(self.name,self.location,self.id))
        CONN.commit()
    def delete(self):
        sql="DELETE FROM departments WHERE id=?;"
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None
    @classmethod
    def instance_from_db(cls,row):
        department=cls.all.get(row[0])
        if department:
            department.name=row[1]
            department.location=row[2]
        else:
            department=cls(row[1],row[2])
            department.id=row[0]
            cls.all[department.id]=department
        return department
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM departments"
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM departments WHERE id=?;"
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod 
    def find_by_name(cls,name):
        sql="SELECT * FROM departments WHERE name=?;"
        row=CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    def employees(self):
        from employee import Employee
        sql="SELECT * FROM employees WHERE department_id=?"
        CURSOR.execute(sql,(self.id,),)
        rows=CURSOR.fetchall()
        return [Employee.instance_from_db(row) for row in rows]

if __name__ == "__main__":
    Department.drop_table()
    Department.create_table()
    payroll=Department.create("Payroll","Building A, 5th Floor")
    #payroll.delete()
    hr=Department("Human Resources","Building C, 2nd Floor")
    hr.save()
    #hr.delete()
    hr.name="HR"
    hr.update()
    developer=Department.create("Software Engineer","Nairobi-KENYA")
    print(f"payroll id:{payroll.id}")
    print(f"payroll:{payroll.employees()}")
    print(f"hr id:{hr.id}")
    print(f"hr:{hr.employees()}")
    print(Department.find_by_id(1))
    print(Department.find_by_name("HR"))
    print(f"Developer:{developer}")
    finance=Department("Finance","Building A, 7th Floor")
    finance.save()
    finance.delete()
    print(Department.find_by_name("Finance"))
    print(Department.get_all())

    it=Department.create(99,"Building C")
    it=Department.create("John",33)
    # CURSOR.close()
    # CONN.close()

