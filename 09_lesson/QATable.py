from sqlalchemy import create_engine
from sqlalchemy.sql import text


class QATable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subjects(self):
        return self.db.execute("select * from subject").fetchall()

    def insert_subject(self, title):
        self.db.execute(text(
            "insert into subject(\"subject_title\") values (:new_title)"
        ), new_title=title)

    def update_subject(self, title, new_id):
        self.db.execute(text(
            "update subject set subject_id= :new_subject_id where subject_title= :title"
        ), title=title, new_subject_id=new_id)

    def delete(self, title):
        self.db.execute(text(
            "delete from subject where subject_title= :title"
        ), title=title)
