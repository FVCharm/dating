from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

from app.forms.base import BaseForm


class VerifyForm(BaseForm):
    phone = IntegerField('手机号', validators=[
        DataRequired(message='不允许为空'),
        NumberRange(min=10000000000, max=99999999999)])
