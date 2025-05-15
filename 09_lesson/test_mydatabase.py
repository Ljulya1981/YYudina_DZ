from QATable import QATable

db = QATable("postgresql://postgres:TypeSuper551@localhost:5432/QA")


def test_insert_subject():
    db_result = db.get_subjects()
    title = 'Ethics'
    db.insert_subject(title)
    new_result = db.get_subjects()
    assert len(new_result) - len(db_result) == 1
    db.delete('Ethics')


def test_update_subject():
    db_result = db.get_subjects()
    title = 'Ethics'
    db.insert_subject(title)
    new_id = len(db_result)+1
    db.update_subject(title, new_id)
    assert new_id == len(db_result)+1
    db.delete('Ethics')


def test_delete_subject():
    db_result = db.get_subjects()
    title = 'Ethics'
    db.insert_subject(title)
    new_result = db.get_subjects()
    assert len(new_result) - len(db_result) == 1
    db.delete('Ethics')
    super_result = db.get_subjects()
    assert len(super_result) == len(db_result)
