import requests

base_url = "https://yougile.com/api-v2"
token = 'OhqzNHFZvL3DnKlUQAGiXHHNdvQYLB9iMKN9JJTVtFeCX8gZI6txIJB-jwMeVBbO'


def create_projects(title):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }
    project = {"title": title}
    resp = requests.post(base_url + '/projects', headers=headers, json=project)
    return resp.json()


def get_projects_by_id(project_id):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }
    resp = requests.get(base_url + '/projects/'+project_id, headers=headers)
    return resp.json()


def edit_projects_by_id(project_id, new_title):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }
    project = {"title": new_title}
    resp = requests.put(base_url + '/projects/' + project_id, headers=headers, json=project)
    return resp.json()


def test_create_project_positive():
    title = "My project"
    result = create_projects(title)
    project_id = result["id"]
    retrieved_response = get_projects_by_id(project_id)
    assert retrieved_response["title"] == "My project"


def test_create_project_negative():
    title = ""
    result = create_projects(title)
    error_message = result["message"]
    assert error_message == ['title should not be empty']


def test_get_projects_by_id_positive():
    title = "SuperCar"
    result = create_projects(title)
    project_id = result["id"]
    retrieved_response = get_projects_by_id(project_id)
    assert retrieved_response["title"] == "SuperCar"


def test_get_projects_by_id_negative():
    project_id = "77777"
    retrieved_response = get_projects_by_id(project_id)
    error_message = retrieved_response["message"]
    assert error_message == 'Проект не найден'


def test_edit_projects_positive():
    title = "Rancho"
    result = create_projects(title)
    project_id = result["id"]
    new_title = "It is not Rancho"
    edited = edit_projects_by_id(project_id, new_title)
    project_new_id = edited["id"]
    project_new_name = get_projects_by_id(project_new_id)
    assert project_new_name["title"] == "It is not Rancho"


def test_edit_projects_negative():
    title = "It is not Rancho"
    result = create_projects(title)
    project_id = result["id"]
    new_title = ""
    edited = edit_projects_by_id(project_id, new_title)
    error_message = edited["message"]
    assert error_message == ['title should not be empty']
