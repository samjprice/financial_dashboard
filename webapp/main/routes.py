from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user
from webapp.example_values import *


main = Blueprint("main", __name__)


@main.route("/layout")
def layout():
    return render_template("base/layout.html")


@main.route("/")
def splash_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("main/splash.html")


@main.route("/dashboard")
@login_required
def dashboard():
    cards = [card_net_worth, card_nest_egg, card_total_assets, card_liabilities, card_fi_number]
    return render_template("main/dashboard.html", title="Dashboard", cards=cards, card_fi_percentage=card_fi_percentage)


@main.route("/portfolio")
@login_required
def portfolio():
    cards = [card_net_worth, card_nest_egg, card_liabilities, card_open_credit, card_available_credit, card_cash_credit]
    return render_template("main/portfolio.html", title="Portfolio", cards = cards)


@main.route("/expenses")
@login_required
def expenses_page():
    table
    total
    return render_template("main/expenses.html", title="Expenses", table = table, total = total)


@main.route("/site_info")
def site_info():
    return render_template("main/site_info.html", title="Site Info")


@main.route("/financial_independence")
@login_required
def fi_page():
    milestones = [milestone_first_100, milestone_coast_fi, milestone_half_fi, milestone_lean_fi, milestone_fi]
    return render_template("main/financial_independence.html", title="Financial Independence", milestones = milestones)


@main.route("/documents")
@login_required
def documents_page():
    return render_template("main/documents.html", title="Documents")
