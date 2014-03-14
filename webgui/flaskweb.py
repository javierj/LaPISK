__author__ = 'Javier'


from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from presenter.ReportPresenter import ReportPresenter
from LaBSKApi.reports import PreGeneratedReports

##def create_app():
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

## Properties

stats_module = None

def set_stats_module(stats_modl):
    global stats_module
    stats_module = stats_modl


def _get_stats_module():
    if not hasattr(g, 'stats_module'):
        g.stats_module = stats_module
    return g.stats_module

def register_access(route):
    stats_mod = _get_stats_module()
    ip = request.remote_addr
    if 'X-Client-Ip' in request.headers:
        ip = request.headers['X-Client-Ip']
    stats_mod.register_access_now(str(route), ip)
    # Tambien vale: request.environ['REMOTE_ADDR'] o request.remote_addr


## Navigation

@app.route("/")
def main():
    register_access(request.path)
    return render_template('main.html')


@app.route("/faqs")
def faqs():
    register_access(request.path)
    return render_template('faqs.html')


@app.route("/stats")
def stats():
    stats_mod =  _get_stats_module()
    return render_template('stats.html', stats_list=stats_mod.all_visits())


@app.route("/reports")
def reports():
    register_access(request.path)
    #register_access("/reports")
    return render_template('reports.html')


@app.route("/reports/asylum-games")
def static_asylum_games():
    register_access(request.path)
    return render_template('static_asylum_games.html')


@app.route("/reports/devir")
def static_devir_games():
    register_access(request.path)
    return render_template('static_devir.html')



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