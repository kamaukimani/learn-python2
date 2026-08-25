from __init__ import CURSOR, CONN
class Department:
    all={}
    def __init__(self,name,location,id=None):
        self.id=id
        self.name=name
        self.location=location
    def __repr__(self):
        return f"<Department {self.id}:{self.name},{self.location}>"
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS departments1(
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT)  
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS departments1"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql="""
        INSERT INTO departments1(name,location)
        VALUES(?,?)
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
        UPDATE departments1
        SET name=?,location=?
        WHERE id=?
        """
        CURSOR.execute(sql,(self.name,self.location,self.id))
        CONN.commit()
    def delete(self):
        sql="DELETE FROM departments1 WHERE id=?"
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
        sql="SELECT * FROM departments1"
        rows=CURSOR.execute(sql).fetchall()
        return[cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql="""SELECT * 
        FROM departments1
        WHERE id=?
        """
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls,name):
        sql="""
        SELECT * 
        FROM departments1
        WHERE name is ?
        """
        row=CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None

# Department.create_table()
# payroll=Department.create("Payroll","Building A, 5th Floor")
# hr=Department.create("Human Resources","Building B, East Wing")
# developer=Department("Developer","Nairobi,KENYA")
# developer.save()
#Department.drop_table()

row=CURSOR.execute("SELECT * FROM departments1").fetchone()
department=Department.instance_from_db(row)
print(department)
Department.get_all()
print(Department.all)
print(Department.find_by_id(2))
print(Department.find_by_name("Developer"))
print(developer)