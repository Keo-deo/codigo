from app import app


@app.route("/")
def paginainicial():
    return """
  pages:

  1-murilo

  2-escola

"""
@app.route("/murilo")
def paginamurilo():
    return "Dados do murilo"
@app.route("/escola")
def paginaescola():
    return "supergeeks"