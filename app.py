from flask import Flask, render_template, Markup, request, redirect, url_for
from markdown import markdown
import json
import datetime

app = Flask(__name__)


@app.route("/suuri/")
def main():
    f = open("database.json","r")
    database = json.load(f)
    f.close()
    database.reverse()
    if len(database) > 5:
        database = database[:6]
    return render_template("index.html",datas=database)

@app.route("/suuri/newText")
def NewText():
    return render_template("upload.html")

@app.route("/suuri/upload/", methods=["POST"])
def upload():
    title = request.form["title"]
    date = str(datetime.datetime.now())
    username = request.form["username"]
    affiliation = request.form["affiliation"]
    text = request.form["text"]
    tags = request.form.getlist("tag")
    print(tags)
    date = datetime.datetime.now()
    data = {
        "title":title,
        "username":username,
        "affiliation":affiliation,
        "text":text,
        "tags":tags,
        "datetime":f"{date.year}/{date.month}/{date.day}"
        }
    print(data)
    f = open("database.json","r")
    database = json.load(f)
    f.close()
    f = open("database.json","w")
    database.append(data)
    text = json.dump(database,f,ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()
    return redirect(url_for("main"))

@app.route("/suuri/data/<path>/<path2>/")
def ronbun(path,path2):
    f = open("database.json","r")
    database = json.load(f)
    for i in database:
        if i["username"] == path and i["title"] == path2:
            return render_template("template.html",content=i,text=Markup(markdown(i["text"])))
    return "<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>"

@app.route("/suuri/tags/<string:tag>")
def serch_tag(tag):
    with open("database.json") as f:
        database = json.load(f)
    apply_datas = list()
    for data in database:
        if tag in data["tags"]:
            apply_datas.append(data)
    apply_datas.reverse()
    return render_template("index.html",datas=apply_datas)

@app.route("/test")
def test():
    return render_template("test.html")    

if __name__ == "__main__":
    app.run(debug=True)