from waitress import serve
from accont import app
serve(app,host='0.0.0.0',port=80)