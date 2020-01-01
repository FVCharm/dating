from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange
from wtforms import ValidationError

from app.models.user import User
from app.forms.base import BaseForm


class MainInfoForm(BaseForm):
    name = StringField()
    ethnic_group = StringField()
    birthday = StringField()
    native_place = StringField()


class PersonalForm(BaseForm):
    username = StringField()
    working_place = StringField()
    degree = IntegerField()
    height = IntegerField()
    gender = IntegerField()
    salary = IntegerField()
    occupation = IntegerField()


class ContactForm(BaseForm):
    qq = StringField()
    weixin = StringField()


class LivelyForm(BaseForm):
    marital_status = StringField()
    children = StringField()
    house = StringField()
    car = StringField()
    drink = StringField()
    smoke = StringField()
    health = StringField()
    religion = StringField()


class HobbyForm(BaseForm):
    topic = StringField()
    sport = StringField()
    ball = StringField()
    leisure = StringField()
    dietary = StringField()
