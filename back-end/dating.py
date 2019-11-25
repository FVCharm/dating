from app import create_app
from app.models.user import User
from app.models.base import db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user': User}

