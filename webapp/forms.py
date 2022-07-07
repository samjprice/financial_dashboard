from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from webapp.models import Accounts, User


class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            InputRequired(),
            Length(max=20),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            InputRequired(),
            Length(max=20),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField(
        "Date of birth"
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo("password"),
        ],
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already registered")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            InputRequired(),
            Length(max=20),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            InputRequired(),
            Length(max=20),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(),
            Length(max=100),
        ],
    )
    dob = DateField(
        "Date of birth"
    )
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is already registered")



class AddAccountForm(FlaskForm):
    account_name = StringField(
        "Account Name",
        validators=[
            InputRequired(),
        ],
    )
    account_type = SelectField(
        "Account Type",
        choices=[
            'Cash',
            'Credit Card',
            'Crypto',
            'Liability',
            'Liquid Asset',
            'Non-Liquid Asset',
            'Material Asset',
            'Pension',
            'Savings Account',
            'Time-Locked Asset',
            ],
        validators=[
            InputRequired(),
        ],
    )
    currency = StringField(
        "Currency Code",
        validators=[InputRequired(),
        Length(min=3, max=3)
        ]
    )
    date_opened = DateField(
        "Date Opened",
        validators=[
            InputRequired(),
        ],
    )
    credit_limit = FloatField("Credit Limit")
    benefit = StringField(
        "Account Benefit",
    )
    benefit_expiry = DateField("Benefit Expiry")
    pin = StringField("PIN")
    notes = StringField(
        "Notes",
    )
    submit = SubmitField("Add")


    def validate_account_name(self, account_name):
        account = Accounts.query.filter_by(account_name=account_name.data).first()
        if account:
            raise ValidationError("That account name is already registered")