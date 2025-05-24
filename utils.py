from flask import session, redirect, url_for, flash

def isLoggedIn(func):
    def decorator():
        if 'user_id' not in session:
            flash("Please Login To Access These Routes", "error")
            return redirect(url_for("Taskly.auth.login"))
        return func
    return decorator