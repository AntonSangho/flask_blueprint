from flask import Blueprint

library = Blueprint("B", __name__, url_prefix="/B")

@library.route("/")
def home():
    return "B 도서관"

@library.route("/userlist") #현재 사용자를 확인하는 페이지
def userlist():
    return "uerlist"

@library.route("/userinfo") #사용자를 확인하는 페이지
def userinfo():
    return "todaylist"

@library.route("/aftermodify") #사용자를 수정 후 페이지
def aftermodify():
    return "aftermodify"

@library.route("/modify") #사용자를 수정하는 페이지
def modify():
    return "modify"
