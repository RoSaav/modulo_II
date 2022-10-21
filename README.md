## modulo_II

Package to build a todo list

Initially appeared on
[gist](https://github.com/RoSaav/modulo_II).

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Python 3.9.x

### Installing - Microsoft Windows

A step by step series of examples that tell you how to get a development
environment running

Run the next lines in a powershell

-pip install virtualenv

-virtualenv todos_env

-todos_env\Scripts\activate

-pip install -r requirements.txt
 
## Running the tests

If you want to run test pre installation you can run all the test in project or unit/integration with the next lines

-tox -v

-pytest todos\tests\integration\test_integration.py -v

-pytest todos\tests\unit\test_create.py -v 

-pytest todos\tests\unit\test_add_task.py

### Sample Tests

-todos\tests\test_list.py .........            [ 47%]

-todos\tests\integration\test_integration.py ..[ 57%]

-todos\tests\unit\test_add_task.py ..          [ 68%]

-todos\tests\unit\test_create.py ......        [100%]

-========================================== 19 passed, 5 warnings in 0.98s -=========================================== 
-______________________________________________________ summary -______________________________________________________

-  py39: commands succeeded

-  congratulations :)

## Deployment

Install the package todos
-pip install dist\todos-0.1.0.tar.gz

To use it follow the next lines ane find out an example

>>> from todos.src import todos

>>> todos.list_lists()

my_first_todo_list.csv

>>> todos.show_list('my_first_todo_list') 

|    | created             | task    | summary      | status   | owner   |

|---:|:--------------------|:--------|:-------------|:---------|:--------|

|  0 | 2022-10-17 22-51-32 | pruebas | update value | todo     | yo      |

If you want know which methods there are check the documentation of each in todos.py

## Authors

Homework for MODULO_II

TECNOLOGICO DE MONTERREY

Miguel Rodrigo Saavedra Perez

https://github.com/RoSaav/modulo_II


## License

This project is licensed under the [MIT](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details
