import sys
sys.path.append(r"C:\Users\immun\Desktop\school\year 3 semeseter1\ece444\ECE444-F2022-Lab6\project") 
import app


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"