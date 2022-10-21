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


def obtener_datos_test_dataframe():
    return [(False, pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])), 
            (True, pd.DataFrame(columns=["crtd", "tsk", "smmr", "stts", "ownr"])),
            (True, pd.DataFrame(columns=["crt", "ts", "smm", "stt", "own"])),
            (True, pd.DataFrame(columns=["c", "t", "s", "s", "o"])),
            (True, pd.DataFrame(columns=["crtd", "tsk"])),
            (True, pd.DataFrame(columns=["crtd", "tsk", "smmr", "stts"]))]

@pytest.mark.parametrize('Bool, dataframe', obtener_datos_test_dataframe())
def test_create_list(tmp_dir, Bool, dataframe):
    todos.create_list("todos")
    df1 = todos.load_list("todos")
    assert (pd.concat([df1, dataframe], axis=1).columns.unique().shape[0]>5)==Bool