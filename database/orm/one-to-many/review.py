from __init__ import CURSOR,CONN
from employee import Employee
class Review:
    all={}
    def __init__(self,year,summary,employee_id,id=None):
        self.id=id
        self.year=year
        self.summary=summary
        self.employee_id=employee_id
    def __repr__(self):
        return (
            f"<Review {self.id}:{self.year},{self.summary}, "+
            f"Employee ID:{self.employee_id}>"
        )
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,year):
        if type(year) is int and year >= 2000:
            self._year=year
        else:
            raise ValueError("Year must be an integer and greater than or equal to 2000")
    @property
    def summary(self):
        return self._summary
    @summary.setter
    def summary(self,summary):
        if isinstance(summary,str) and len(summary):
            self._summary=summary
        else:
            raise ValueError("Summary must be a non-empty string")
    @property
    def employee_id(self):
        return self._employee_id
    @employee_id.setter
    def employee_id(self,employee_id):
        if type(employee_id) is int and Employee.find_by_id(employee_id):
            self._employee_id=employee_id
        else:
            raise ValueError("employee_id must reference a employee in the database")
    @classmethod 
    def create_table(cls):
        sql="""
        CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY,
        year INTEGER,
        summary TEXT,
        employee_id INTEGER,
        FOREIGN KEY(employee_id) REFERENCES employees(id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS reviews;"
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql="""
        INSERT INTO reviews(year,summary,employee_id)
        VALUES(?,?,?);
        """
        CURSOR.execute(sql,(self.year,self.summary,self.employee_id))
        CONN.commit()
        self.id=CURSOR.lastrowid
        type(self).all[self.id]=self
    @classmethod
    def create(cls,year,summary,employee_id):
        review=cls(year,summary,employee_id)
        review.save()
        return review
    def update(self):
        sql="""
        UPDATE reviews
        SET year=?,summary=?,employee_id=?
        WHERE id=?;
        """
        CURSOR.execute(sql,(self.year,self.summary,self.employee_id,self.id))
        CONN.commit()
    def delete(self):
        sql="DELETE FROM reviews WHERE id=?;"
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id=None
    @classmethod
    def instance_from_db(cls,row):
        review=cls.all.get(row[0])
        if review:
            review.year=row[1]
            review.summary=row[2]
            review.employee_id=row[3]
        else:
            review=cls(row[1],row[2],row[3])
            review.id=row[0]
            cls.all[review.id]=review
        return review
    @classmethod
    def get_all(cls):
        sql="SELECT * FROM reviews;"
        rows=CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls,id):
        sql="SELECT * FROM reviews WHERE id=?;"
        row=CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_year(cls,year):
        sql="SELECT * FROM reviews WHERE year=?;"
        row=CURSOR.execute(sql,(year,)).fetchone()
        return cls.instance_from_db(row) if row else None
Review.drop_table()
Review.create_table()
review1=Review.create(2023,"Excellent Python skills",1)
review2=Review(2020,"Greate coder",2)
review2.save()
review3=Review.create(2000,"Awesome code",1)
review4=Review(2021,"Usually double checks their work",3)
review4.save()
review5=Review.create(2002,"Takes long lunches",3)
# review6=Review.create(1999,"Old enough to retire",4)
# review6=Review.create(2004,30,4)
# review6=Review.create(2004,"Always ready to learn",7)
review6=Review.create(2004,"Always ready to learn",4)
review6.year=2023
review6.update()
#review6.delete()
print(Review.find_by_id(6))
print(Review.all)
print(".............................................................")
print(Review.find_by_year(2020))