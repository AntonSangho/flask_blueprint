from flask import Flask
from . import A 
from . import B 
from . import C  
from . import D 
from . import E 


app = Flask(__name__)

app.register_blueprint(A.library)
app.register_blueprint(B.library)
app.register_blueprint(C.library)
app.register_blueprint(D.library)
app.register_blueprint(E.library)

