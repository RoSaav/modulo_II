import os
import sys
import pandas as pd
import pytest
import shutil
from datetime import datetime
sys.path.append( os.path.abspath(os.path.dirname(__file__)+'/../..') )
from src import todos

@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    todos.PATH_TO_DATA = my_tmpdir
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="function")
def new_row():
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "cocinar",
        "summary": "Cocinar algo rico",
        "status": "todo",
        "owner": "Andre",
    }


@pytest.fixture(scope="function")
def df_full(new_row):
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )


n1 = {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "Programar",
        "summary": "Tarea python",
        "status": "todo",
        "owner": "Rodrigo",
    }

n2 = {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "cocinar",
        "summary": "Cocinar algo rico",
        "status": "todo",
        "owner": "Andre",
    }

def obtener_datos_test_add_task():
    return [(False, n2), 
            (True, n1)]

@pytest.mark.parametrize('Bool, nr', obtener_datos_test_add_task())
def test_add_to_list(Bool, nr, tmp_dir, df_full):

    todos.create_list("todos")
    todos.add_to_list("todos", nr)
    df1 = todos.load_list("todos")
    assert (df_full.append(df1).drop_duplicates().shape[0]>1)==Bool
