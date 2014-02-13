__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup

class HTMLFactory:

    @staticmethod
    def msg_html():
        return """
        <div class="post_wrapper">
						<div class="poster">
							<h4>
								<a href="http://labsk.net/index.php?action=profile;u=19849" title="Ver perfil de flOrO">flOrO</a>
							</h4>
							<ul class="reset smalltext" id="msg_1169262_extra_info">
								<li class="postgroup">Experimentado</li>
								<li class="stars"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /></li>
								<li class="postcount">Mensajes: 412</li>
								<li class="postgroup">Ubicacion: Mallorca</li>
								<li class="profile">
									<ul>
										<li><a href="http://labsk.net/index.php?action=profile;u=19849"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/profile_sm.gif" alt="Ver Perfil" title="Ver Perfil" /></a></li>
										<li><a href="http://labsk.net/index.php?action=emailuser;sa=email;msg=1169262" rel="nofollow"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/email_sm.gif" alt="Email" title="Email" /></a></li>
										<li><a href="http://labsk.net/index.php?action=pm;sa=send;u=19849" title="Mensaje Privado (Desconectado)"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/im_off.gif" alt="Mensaje Privado (Desconectado)" /></a></li>
									</ul>
								</li>
							</ul>
						</div>
						<div class="postarea">
							<div class="flow_hidden">
								<div class="keyinfo">
									<div class="messageicon">
										<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/novedad.gif" alt="" />
									</div>
									<h5 id="subject_1169262">
										<a href="http://labsk.net/index.php?topic=119300.msg1169262#msg1169262" rel="nofollow">Fief - Feudo Ediciones MasQueOca editara Fief en Espanyol</a>
									</h5>
									<div class="smalltext">&#171; <strong> en:</strong> 25 de Octubre de 2013, 12:12:00 pm &#187;</div>
									<div id="msg_1169262_quick_mod"></div>
								</div>
								<ul class="reset smalltext quickbuttons">
									<li class="quote_button"><a href="http://labsk.net/index.php?action=post;quote=1169262;topic=119300.0;last_msg=1216124" onclick="return oQuickReply.quote(1169262);">Citar</a></li>
					<li class="thank_you_button"><span id="buttonThxID1169262" style="display: inline;"><a id="buttonThxHrefID1169262" href="http://labsk.net/index.php?action=thankyou;topic=119300.0;msg=1169262">Gracias</a></span></li>
								</ul>
							</div>

							<!-- Un mensaje concreto -->

							<div class="post">
								<div class="inner" id="msg_1169262">Parece ser que este juego de Asyncro Games se
								va a reeditar por academy games, la editorial de Conflic of heroes.
								<br />En la pagina de Asyncro Games hay
								 informacio.<br /><a href="http://www.asyncron.fr/fief-la-reimpression-en-vue/" class="bbc_link" target="_blank">
								 http://www.asyncron.fr/fief-la-reimpression-en-vue/</a><br /><br />
								 He preguntado por la bgg y esto es lo que me ha dicho un usuario:
								 <br />
								 Well - as said above it&#039;s to be redone by Academy Games. So I contacted them and to quote the very prompt reply from
								 Uwe<br /><br />&quot;we will be publishing a new version of Fief. We just got done re-writing the rules and are reviewing
								 a few changes that we would like to make with the designers to stream line the rules and game play.<br />I expect to start
								  the Kickstarter campaign in late November.
								  <img src="http://h2212313.stratoserver.net/Smileys/default/smiley.gif" alt="&#58;&#41;" title="Sonrisa" class="smiley" />
								  &quot;<br /><br />So things do appear to be moving forward and hopefully we will see this game re-issued before we are much
								  older! <br /><br /><br />Asi que parece que el juego entrara en kickstarter en noviembre. <br /><br />Una resenyaa del mismo
								  por si alguen no sabe de que juego se trata<br />
								  <a href="http://labsk.net/index.php?topic=98174.msg1000863#msg1000863" class="bbc_link" target="_blank">
								  http://labsk.net/index.php?topic=98174.msg1000863#msg1000863</a></div>
							</div>
						</div>
						<div class="moderatorbar">
							<div class="smalltext modified" id="modified_1169262">
								&#171; <em>Ultima modificacion: 25 de Octubre de 2013, 02:50:27 pm por Quas4R</em> &#187;
							</div>
							<div class="smalltext reportlinks"><g:plusone href="http://labsk.net/index.php?topic=119300" size="small"></g:plusone>
			<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script><a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
								<a href="http://labsk.net/index.php?action=reporttm;topic=119300.0;msg=1169262">Reportar al moderador</a> &nbsp;
								<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/ip.gif" alt="" />
								<a href="http://labsk.net/index.php?action=helpadmin;help=see_member_ip" onclick="return reqWin(this.href);" class="help">
								En linea</a>
							</div>
						</div>
					</div>


     <div class="post_wrapper">
						<div class="poster">
							<h4>
								<a href="http://labsk.net/index.php?action=profile;u=19849" title="Ver perfil de flOrO">flOrO</a>
							</h4>
							<ul class="reset smalltext" id="msg_1169262_extra_info">
								<li class="postgroup">Experimentado</li>
								<li class="stars"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /></li>
								<li class="postcount">Mensajes: 412</li>
								<li class="postgroup">Ubicacion: Mallorca</li>
								<li class="profile">
									<ul>
										<li><a href="http://labsk.net/index.php?action=profile;u=19849"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/profile_sm.gif" alt="Ver Perfil" title="Ver Perfil" /></a></li>
										<li><a href="http://labsk.net/index.php?action=emailuser;sa=email;msg=1169262" rel="nofollow"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/email_sm.gif" alt="Email" title="Email" /></a></li>
										<li><a href="http://labsk.net/index.php?action=pm;sa=send;u=19849" title="Mensaje Privado (Desconectado)"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/im_off.gif" alt="Mensaje Privado (Desconectado)" /></a></li>
									</ul>
								</li>
							</ul>
						</div>
						<div class="postarea">
							<div class="flow_hidden">
								<div class="keyinfo">
									<div class="messageicon">
										<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/novedad.gif" alt="" />
									</div>
									<h5 id="subject_1169262">
										<a href="http://labsk.net/index.php?topic=119300.msg1169262#msg1169262" rel="nofollow">Fief - Feudo Ediciones MasQueOca editara Fief en Espanyol</a>
									</h5>
									<div class="smalltext">&#171; <strong> en:</strong> 25 de Octubre de 2013, 12:12:00 pm &#187;</div>
									<div id="msg_1169262_quick_mod"></div>
								</div>
								<ul class="reset smalltext quickbuttons">
									<li class="quote_button"><a href="http://labsk.net/index.php?action=post;quote=1169262;topic=119300.0;last_msg=1216124" onclick="return oQuickReply.quote(1169262);">Citar</a></li>
					<li class="thank_you_button"><span id="buttonThxID1169262" style="display: inline;"><a id="buttonThxHrefID1169262" href="http://labsk.net/index.php?action=thankyou;topic=119300.0;msg=1169262">Gracias</a></span></li>
								</ul>
							</div>

							<!-- Un mensaje concreto -->

							<div class="post">
								<div class="inner" id="msg_1169262">Body</div>
							</div>
						</div>
						<div class="moderatorbar">
							<div class="smalltext modified" id="modified_1169262">
								&#171; <em>Ultima modificacion: 25 de Octubre de 2013, 02:50:27 pm por Quas4R</em> &#187;
							</div>
							<div class="smalltext reportlinks"><g:plusone href="http://labsk.net/index.php?topic=119300" size="small"></g:plusone>
			<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script><a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
								<a href="http://labsk.net/index.php?action=reporttm;topic=119300.0;msg=1169262">Reportar al moderador</a> &nbsp;
								<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/ip.gif" alt="" />
								<a href="http://labsk.net/index.php?action=helpadmin;help=see_member_ip" onclick="return reqWin(this.href);" class="help">
								En linea</a>
							</div>
						</div>
					</div>

        """

    def msg(self):
        return BeautifulSoup(HTMLFactory.msg_html())

    @staticmethod
    def asunto():
        return BeautifulSoup("""
            <tr>
<td class="icon1 windowbg">
<img alt="" src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/topic/normal_post.gif"/>
</td>
<td class="icon2 windowbg">
<img alt="" src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/xx.gif"/>
</td>
<td class="subject windowbg2">
<div>
<span id="msg_1216998"><a href="http://labsk.net/index.php?topic=126314.0">Robinson Crusoe de Portal Games en espanol (al 95)</a></span>
<p>Iniciado por <a href="http://labsk.net/index.php?action=profile;u=22255" title="Ver perfil de Borja">Borja</a>
<small id="pages1216998"></small>
</p>
</div>
</td>
<td class="stats windowbg">
						10 Respuestas
						<br/>
						490 Vistas
					</td>
<td class="lastpost windowbg2">
<a href="http://labsk.net/index.php?topic=126314.0#msg1217369"><img alt="Ultimo mensaje"
src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/last_post.gif" title="Ultimo mensaje"/></a>
<strong>Hoy</strong> a las 08:43:50 pm<br/>
						por <a href="http://labsk.net/index.php?action=profile;u=20257">Dens</a>
</td>

<td class="icon1 windowbg">
<img alt="" src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/topic/normal_post.gif"/>
</td>
<td class="icon2 windowbg">
<img alt="" src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/xx.gif"/>
</td>
<td class="subject windowbg2">
<div>
<span id="msg_1216998"><a href="http://labsk.net/index.php?topic=126314.0">Otro titulo</a></span>
<p>Iniciado por <a href="http://labsk.net/index.php?action=profile;u=22255" title="Ver perfil de Borja">Borja</a>
<small id="pages1216998"></small>
</p>
</div>
</td>
<td class="stats windowbg">
						10 Respuestas
						<br/>
						490 Vistas
					</td>
<td class="lastpost windowbg2">
<a href="http://labsk.net/index.php?topic=126314.0#msg1217369"><img alt="Ultimo mensaje"
src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/last_post.gif" title="Ultimo mensaje"/></a>
<strong>Hoy</strong> a las 08:43:50 pm<br/>
						por <a href="http://labsk.net/index.php?action=profile;u=20257">Dens</a>
</td>

</tr>
        """)

    @staticmethod
    def tablamensajes_html():
        return """
<!-- Tabla de mensajes -->
	<div class="tborder topic_table" id="messageindex">
		<table class="table_grid" cellspacing="0">
			<thead>
				<tr class="catbg">
					<th scope="col" class="first_th" width="8%" colspan="2">&nbsp;</th>
					<th scope="col" class="lefttext"><a href="http://labsk.net/index.php?board=18.0;sort=subject">Asunto</a> / <a href="http://labsk.net/index.php?board=18.0;sort=starter">Iniciado por</a></th>
					<th scope="col" width="14%"><a href="http://labsk.net/index.php?board=18.0;sort=replies">Respuestas</a> / <a href="http://labsk.net/index.php?board=18.0;sort=views">Vistas</a></th>
					<th scope="col" class="lefttext last_th" width="22%"><a href="http://labsk.net/index.php?board=18.0;sort=last_post"> mensaje</a></th>
				</tr>
			</thead>
			<tbody>

			<!-- -->
	<!-- Primer mensaje -->

				<tr>
					<td class="icon1 windowbg">
						<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/topic/normal_post.gif" alt="" />
					</td>
					<td class="icon2 windowbg">
						<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/xx.gif" alt="" />
					</td>
					<td class="subject windowbg2">
						<div >
							<span id="msg_1214396"><a href="http://labsk.net/index.php?topic=126053.0">1936 guerra civil -  D6</a></span>
							<a href="http://labsk.net/index.php?topic=126053.msg0#new" id="newicon1214396"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/spanish_es/new.gif" alt="Nuevo" /></a>
							<p>Iniciado por <a href="http://labsk.net/index.php?action=profile;u=1217" title="Ver perfil de Arturo ">Arturo </a>
								<small id="pages1214396"></small>
							</p>
						</div>
					</td>
					<td class="stats windowbg">
						0 Respuestas
						<br />
						1 Vistas
					</td>
					<td class="lastpost windowbg2">
						<a href="http://labsk.net/index.php?topic=126053.0#new"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/last_post.gif" alt=" mensaje" title=" mensaje" /></a>
						<strong>Hoy</strong> a las 08:24:49 pm<br />
						por <a href="http://labsk.net/index.php?action=profile;u=1217">Arturo </a>
					</td>
				</tr>
				<tr>
					<td class="icon1 windowbg">
						<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/topic/normal_post.gif" alt="" />
					</td>
					<td class="icon2 windowbg">
						<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/post/novedad.gif" alt="" />
					</td>
					<td class="subject windowbg2">
						<div >
							<span id="msg_1214283"><a href="http://labsk.net/index.php?topic=126044.0"> Temporada de Regionales 2014 de Edge </a></span>
							<a href="http://labsk.net/index.php?topic=126044.msg0#new" id="newicon1214283"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/spanish_es/new.gif" alt="Nuevo" /></a>
							<p>Iniciado por <a href="http://labsk.net/index.php?action=profile;u=22803" title="Ver perfil de LudoNoticias">LudoNoticias</a>
								<small id="pages1214283"></small>
							</p>
						</div>
					</td>
					<td class="stats windowbg">
						0 Respuestas
						<br />
						39 Vistas
					</td>
					<td class="lastpost windowbg2">
						<a href="http://labsk.net/index.php?topic=126044.0#new"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/last_post.gif" alt=" mensaje" title=" mensaje" /></a>
						<strong>Hoy</strong> a las 05:00:21 pm<br />
						por <a href="http://labsk.net/index.php?action=profile;u=22803">LudoNoticias</a>
					</td>
				</tr>
	    </table>
        """

    @staticmethod
    def tablamensajes():
        return BeautifulSoup(HTMLFactory.tablamensajes_html())

    @staticmethod
    def navigation_url():
        return """
            <div class="pagelinks floatleft">Paginas: [<strong>1</strong>] <a class="navPages"
             href="http://labsk.net/index.php?board=18.20">2</a> <a class="navPages"
              href="http://labsk.net/index.php?board=18.40">3</a> <span style="font-weight: bold;"
              > ... </span>
              <a class="navPages" href="http://labsk.net/index.php?board=18.2080">105</a>
              <a class="navPages" href="http://labsk.net/index.php?board=18.20">>></a>  &nbsp;&nbsp;<a href="#bot"><strong>Ir Abajo</strong></a></div>
            """


class MockWebClient(object):
    def __init__(self, code = ""):
        self.code = code
        self.url = ""

    def sourceCode(self):
        return self.code

    def load(self, link):
         self.url = link


class MockMongo(object):
    def __init__(self):
        self.treadssaved = 0
        self.listofthreads = list()

    def saveThread(self, thread):
        self.treadssaved += 1
        self.listofthreads.append(thread)
        # print thread