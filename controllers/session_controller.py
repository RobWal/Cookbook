from flask import Blueprint, request, session, redirect, render_template
from models.user import get_user_by_email
import bcrypt
