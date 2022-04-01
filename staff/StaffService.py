from database.database import Database
from staff.constants import ItemType
from staff.staff import Staff


# class for staff table access
class StaffService:

    def __init__(self, db: Database):
        self.db: Database = db

    # inserting multiple staff instances into database table
    def insert_list(self, insert_list: list[Staff]):
        insert_data: list = list(map(lambda staff: [staff.id, staff.parent_id, staff.name, staff.type], insert_list))
        query: str = "INSERT INTO staff (id, parent_id, name, type) values (%s, %s, %s, %s)"
        with self.db.get_connection() as conn:
            conn.execute_many(query=query, insert_list=insert_data)

    # getting staff in same city by person id by getting top parents for all items and selecting items with type = 3
    # (person) and same top-level parent with given person
    def get_city_staff_by_person_id(self, id_: int) -> list[str]:
        query: str = f"""WITH RECURSIVE res AS
         (
             SELECT id, parent_id, name, id as top, type
             FROM staff
             where parent_id IS NULL
             UNION ALL
             SELECT s.Id, s.parent_id, s.name, r.top, s.type
             FROM staff s
                      INNER JOIN res r ON s.parent_id = r.id
         )
         select name from res where type = {ItemType.person.value} 
         and res.top = (select top from res where id = {id_});"""
        with self.db.get_connection() as conn:
            conn.query(query)
            data: list[tuple] = conn.fetchall()
            return list(map(lambda x: x[0], data))
