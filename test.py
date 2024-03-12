from main import mlops

mlopsObj = mlops(10)
def test_getTotalStudents():
    assert mlopsObj.getTotalStudents() == 10

def test_addStudents():
    mlopsObj.addStudents()
    assert mlopsObj.getTotalStudents() == 11

def test_removeStudents():
    mlopsObj.removeStudents()
    assert mlopsObj.getTotalStudents() == 10

def test_getClassName():
    assert mlopsObj.getClassName() == "MLOPS CS-B"