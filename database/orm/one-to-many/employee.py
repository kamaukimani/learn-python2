from __init__ import CURSOR,CONN
from department import Department
from faker import Faker
class Employee:
    all={}
    def __init__(self,name,job_title,department_id,id=None):
        self.id=id
        self.name=name
        self.job_title=job_title
        self.department_id=department_id
    def __repr__(self):
        return (
            f"<Employee{self.id}:{self.name},{self.job_title}, " +
            f"Department ID:{self.department_id}>"
        )
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
    def job_title(self):
        return self._job_title
    @job_title.setter
    def job_title(self,job_title):
        if isinstance(job_title,str) and len(job_title):
            self._job_title=job_title
        else:
            raise ValueError("Job title must be a non-empty string")
    @property
    def department_id(self):
        return self._department_id
    @department_id.setter
    def department_id(self,department_id):
        if type(department_id) is int and Department.find_by_id(department_id):
            self._department_id=department_id
        else:
            raise ValueError("department_id must reference a department in the database")
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        job_title TEXT,
        department_id INTEGER,
        FOREIGN KEY(department_id) REFERENCES departments(id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS employees;"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql="""
        INSERT INTO employees(name,job_title,department_id)
        VALUES(?,?,?);
        """
        CURSOR.execute(sql,(self.name,self.job_title,self.department_id))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    def update(self):
        sql="""
        UPDATE employees
        SET name=?,job_title=?,department_id=?
        WHERE id=?;
        """
        CURSOR.execute(sql,(self.name,self.job_title,self.department_id,self.id))
        CONN.commit()
    def delete(self):
        sql="DELETE FROM employees WHERE id=?;"
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None
    @classmethod
    def create(cls,name,job_title,department_id):
        employee=cls(name,job_title,department_id)
        employee.save()
        return employee
    @classmethod
    def instance_from_db(cls,row):
        employee=cls.all.get(row[0])
        if employee:
            employee.name=row[1]
            employee.job_title=row[2]
            employee.department_id=row[3]
        else:
            employee=cls(row[1],row[2],row[3])
            employee.id=row[0]
            cls.all[employee.id]=employee
        return employee
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM employees;"
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row)for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM employees WHERE id=?;"
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls,name):
        sql="SELECT * FROM employees WHERE name is?;"
        row=CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
Employee.drop_table()
Employee.create_table()
faker=Faker()
employee1=Employee.create(faker.name(),"Manager",1)
#employee1.delete()
employee2=Employee(faker.name(),"Web Developer",2)
employee2.save()
#employee2.delete()
employee3=Employee.create(faker.name(),"Teacher",1)
#employee3.delete()
employee4=Employee(faker.name(),"Secretary",3)
employee4.save()
employee4.job_title="Sec"
employee4.update()
print(f"update:{employee4}")
employee5=Employee.create("James","Security",3)
employee5.delete()
print(Employee.find_by_id(1))
print(Employee.find_by_name("James"))
print(Employee.get_all())
print(Employee.all)
employee5=Employee.create(99,"Artist",3)
employee5=Employee.create("Savage",99,3)
employee5=Employee.create("Savage","Artist",100)
CURSOR.close()
CONN.close()