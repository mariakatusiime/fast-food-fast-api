from webapp.views.api import myapp
from webapp.controllers.tables import Mytables

if __name__ == '__main__':
    Mytables().create_tables()  
    myapp.run(debug=True )