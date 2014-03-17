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


@app.route("/contact")
def contact():
    register_access(request.path)
    return render_template('contact.html')


@app.route("/stats")
def stats():
    stats_mod =  _get_stats_module()
    return render_template('stats.html', stats_list=stats_mod.all_visits())


@app.route("/reports")
def reports():
    register_access(request.path)
    #register_access("/reports")
    return render_template('reports.html')

# Static reports

@app.route("/reports/asylum-games")
def static_asylum_games():
    register_access(request.path)
    return render_template('static_asylum_games.html')


@app.route("/reports/devir")
def static_devir_games():
    register_access(request.path)
    return render_template('static_devir.html')

@app.route("/reports/ludonova")
def static_ludonova_games():
    register_access(request.path)
    return render_template('static_ludonova.html')

@app.route("/reports/asmodee")
def static_asmodee_games():
    register_access(request.path)
    return render_template('static_asmodee.html')

@app.route("/reports/lost_games")
def static_lost_games_games():
    register_access(request.path)
    return render_template('static_lost_games.html')

@app.route("/reports/edge_ent")
def static_edge_ent():
    register_access(request.path)
    return render_template('static_edge_ent.html')

@app.route("/reports/dizemo_ent")
def static_dizemo_ent():
    register_access(request.path)
    return render_template('static_dizemo_ent.html')

@app.route("/reports/looping_games")
def static_looping_games():
    register_access(request.path)
    return render_template('static_looping_games.html')

@app.route("/reports/nestor_games")
def static_nestor_games():
    register_access(request.path)
    return render_template('static_nestor_games.html')

@app.route("/reports/morapiaf")
def static_morapiaf():
    register_access(request.path)
    return render_template('static_morapiaf.html')

# e-shops

@app.route("/reports/tienda_100_doblones")
def static_tienda_100_doblones():
    register_access(request.path)
    return render_template('static_tienda_100_doblones.html')


@app.route("/reports/tienda_click_and_rol")
def static_tienda_click_and_rol():
    register_access(request.path)
    return render_template('static_tienda_click_and_rol.html')


@app.route("/reports/tienda_dungeon_marvels")
def static_tienda_dungeon_marvels():
    register_access(request.path)
    return render_template('static_tienda_dungeon_marvels.html')


@app.route("/reports/tienda_evolution_goya")
def static_tienda_evolution_goya():
    register_access(request.path)
    return render_template('static_tienda_evolution_goya.html')


@app.route("/reports/tienda_finplay")
def static_tienda_finplay():
    register_access(request.path)
    return render_template('static_tienda_finplay.html')


@app.route("/reports/tienda_mas_que_oca")
def static_tienda_mas_que_oca():
    register_access(request.path)
    return render_template('static_tienda_mas_que_oca.html')


@app.route("/reports/tienda_planeton")
def static_tienda_planeton():
    register_access(request.path)
    return render_template('static_tienda_planeton.html')


@app.route("/reports/tienda_tablerum")
def static_tienda_tablerum():
    register_access(request.path)
    return render_template('static_tienda_tablerum.html')


@app.route("/reports/tienda_zacatrus")
def static_tienda_zacatrus():
    register_access(request.path)
    return render_template('static_tienda_zacatrus.html')


# Mocks

@app.route("/comparatives")
def comparatives():
    register_access(request.path)
    return render_template('mock_comparatives.html')

@app.route("/people")
def people():
    register_access(request.path)
    return render_template('mock_people.html')

@app.route("/following")
def following():
    register_access(request.path)
    return render_template('mock_following.html')


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