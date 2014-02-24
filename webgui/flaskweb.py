__author__ = 'Javier'


from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from presenter.ReportPresenter import ReportPresenter, PreGeneratedReports
from LaBSKApi.MongoDB import MongoDB
import helppers

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# FIX: This will fail
reportPresenter = ReportPresenter()
#reportPresenter.database = MongoDB()

@app.route("/")
def main():
    return render_template('main.html', reports_url = url_for("reports"))

@app.route("/reports")
def reports():
    return render_template('reports.html')

@app.route("/reports/asylum-games")
def static_asylum_games():
    return render_template('static_asylum_games.html')



# Dynamic behaviour
@app.route("/reports/dynamic-asylum-games")
def reports_asylum_games():
    """
    text = reportPresenter.generatePreReport_AsylumGames()
    helpper = helppers.GenerateHTMLFromText()
    if text is not None:
        html = helpper.html_from(text, 1)
    else:
        html = "Warning, report result was None. "
    return render_template('report.html', text = html)
    """

    # first obtaining the report
    report = reportPresenter.getReportFor_AsylumGames()
    # Passing the Json to the template
    # This is a hack and shuld be changed
    return render_template('_static_report.html', report = report.json(), \
                                               keywords=  PreGeneratedReports.report_asylum_games['keywords'])


if __name__ == "__main__":
    app.run()