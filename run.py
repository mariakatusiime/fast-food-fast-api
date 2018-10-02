from views.api import myapp
from controllers.tables import Mytables

if __name__ == '__main__':
    Mytables().create_tables()  
    myapp.run(debug=True )