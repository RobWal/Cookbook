from flask import Blueprint, request, session, redirect, render_template
# from models.user import get_user_by_email
import bcrypt

session_controller = Blueprint(
    "session_controller", __name__, template_folder="../templates/session")
