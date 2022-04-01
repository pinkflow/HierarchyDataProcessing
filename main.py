import json
import sys

from database.database import Database
from staff.StaffService import StaffService
from staff.staff import Staff


# creating table and adding test data to database
def _add_test_data():
    database = Database()
    with open('json.txt', 'r', encoding='utf-8') as json_file:
        json_data: list[dict] = json.load(json_file)
        staff_list = list(map(lambda data: Staff(data['id'], data['ParentId'], data["Name"], data["Type"]), json_data))
    with database.get_connection() as conn:
        conn.query("DROP TABLE IF EXISTS staff")
        conn.query("""CREATE TABLE staff
            (
            id serial constraint staff_pk primary key,
            parent_id integer,
            name varchar(255),
            type integer
            );""")
    staff_service: StaffService = StaffService(database)
    staff_service.insert_list(staff_list)


def main() -> str:
    _add_test_data()
    database: Database = Database()
    staff_service: StaffService = StaffService(database)
    person_id: int = int(sys.argv[1])
    staff = staff_service.get_city_staff_by_person_id(person_id)
    return ", ".join(staff)


if __name__ == '__main__':
    sys.exit(main())
