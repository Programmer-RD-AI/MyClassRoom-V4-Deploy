from server import *
from server.db.notices import *


@app.route("/Teacher")
@app.route("/Teacher/")
def teacher():
    """
    Teacher Home Page
    """
    try:
        conditions = [
            "Auth" in session,
            "User Name" in session,
            "Password or Email" in session,
            "Role" in session,
            "Returned Data" in session,
            session["Role"] == "Teacher",
        ]
        if all(conditions):
            return render_template("/teacher/home.html")
        return abort(404)
    except:
        return abort(505)


@app.route("/Teacher/Log/Out")
@app.route("/Teacher/Log/Out/")
def teacher_log_out():
    """
    Teacher Log Out
    """
    try:
        pop = ["Auth", "User Name", "Password", "Role", "Returned Data"]
        for poper in pop:
            session.pop(poper, None)
        return redirect("/")
    except:
        return abort(505)
