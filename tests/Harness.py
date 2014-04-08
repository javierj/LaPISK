__author__ = 'Javier'

from bs4 import BeautifulSoup
from datetime import datetime


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
<span id="msg_1216998">
<a href="http://labsk.net/index.php?topic=126314.0">Robinson Crusoe de Portal Games en espanol (al 95)</a></span>
<p>Iniciado por
<a href="http://labsk.net/index.php?action=profile;u=22255" title="Ver perfil de Borja">Borja</a>
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
src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/last_post.gif" title="Ultimo mensaje"/>
</a>
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

    msg_with_html = BeautifulSoup("""
 <div class="post_wrapper">
						<div class="poster">
							<h4>
								<a href="http://labsk.net/index.php?action=profile;u=22803" title="Ver perfil de LudoNoticias">LudoNoticias</a>
							</h4>
							<ul class="reset smalltext" id="msg_1240391_extra_info">
								<li class="postgroup">Recien Llegado</li>
								<li class="stars">
								<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/star.gif" alt="*" /></li>
								<li class="postcount">Mensajes: 8</li>
								<li class="profile">
									<ul>
										<li><a href="http://labsk.net/index.php?action=profile;u=22803">
										<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/icons/profile_sm.gif" alt="Ver Perfil" title="Ver Perfil" /></a></li>
										<li><a href="http://labsk.net/index.php?action=emailuser;sa=email;msg=1240391"
										rel="nofollow"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/email_sm.gif" alt="Email" title="Email" /></a></li>
										<li><a href="http://labsk.net/index.php?action=pm;sa=send;u=22803" title="Mensaje Privado (Desconectado)"><img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/im_off.gif" alt="Mensaje Privado (Desconectado)" /></a></li>
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
									<h5 id="subject_1240391">
										<a href="http://labsk.net/index.php?topic=128950.msg1240391#msg1240391" rel="nofollow">
										Osprey Publishing crea su division de juegos </a>
									</h5>
									<div class="smalltext">&#171; <strong> en:</strong> 08 de Marzo de 2014, 05:00:13 pm &#187;</div>
									<div id="msg_1240391_quick_mod"></div>
								</div>
								<ul class="reset smalltext quickbuttons">
									<li class="quote_button"><a href="http://labsk.net/index.php?action=post;quote=1240391;topic=128950.0;last_msg=1240391" onclick="return oQuickReply.quote(1240391);">Citar</a></li>
					<li class="thank_you_button"><span id="buttonThxID1240391" style="display: inline;"><a id="buttonThxHrefID1240391" href="http://labsk.net/index.php?action=thankyou;topic=128950.0;msg=1240391">Gracias</a></span></li>
								</ul>
							</div>
							<div class="post">
								<div class="inner" id="msg_1240391"><strong>Osprey Publishing crea su division de juegos</strong><br /><br />
								<p><a rel="nofollow" target="_blank" href="http://ludonoticias.com/2014/03/08/osprey-publishing-crea-su-division-de-juegos/">Osprey Publishing crea su divisipn de juegos</a></p><p><strong>Osprey publishing</strong>
								aumenta su linea de productos, y para ello ha creado una division dedicada a los juegos.
								<strong>Osprey Games</strong> se encargara de publicar nuevos productos, siguiendo la linea de sus exitosos wargames
								de miniaturas, al mismo tiempo que incluira juegos de tablero y de cartas;
								lo que permitira a la c fortalecer y diversificar su posicion.<span id="more-7857"></span></p
								><p><img class="aligncenter size-full wp-image-7861" alt="Field of Glory de osprey publishing"
								src="http://ludonoticias.com/wp-content/uploads/2014/03/Osprey-rules-001.jpg" width="585" height="250"/></p>
								<p>En 2008 <strong>Osprey publishing</strong> lanzo al mercado junto a <strong>Slitherine Strategies</strong> el
								wargame historico de miniaturas <strong>Field of Glory</strong>, comenzando a centrarse en un hobby con el que tenia
								mucho en comun. Los libros militares de la companyia inglesa han sido fuente
								de inspiracion para pintores, disenyadores
								de escenarios y jugadores de wargames de todas las epocas, siendo <strong>Field of Glory</strong> el primer juego
								creado por la editorial para este publico. El exito de este juego les llevo a publicar otros proyectos como
								<strong>Force on Force</strong> (en colaboracion con <strong>Ambush Alley Games</strong>) y las versiones ambientadas
								en el renacimiento y las guerras napoleonicas de <strong>Field of Glory</strong>.
								a <strong>Warlord games</strong> de las reglas de <strong>Bolt Action</strong> y la serie de pequenyos libros de reglas de
								la serie <strong>Osprey Wargames</strong>, han situado a la companya como
								una de las mayores editoriales de
								juegos de estrategia.</p><p><img class="aligncenter size-full wp-image-7859" alt="Reglas para wargames modernos de Osprey Publishing"
								src="http://ludonoticias.com/wp-content/uploads/2014/03/Osprey-rules-002.jpg" width="390" height="248"/>
								</p><p>&nbsp;</p>
								<div class="wpInsert wpInsertInPostAd wpInsertBelow" style="margin:5px auto;padding:0px;width:468px;"> &nbsp;</div>
								<p>La entrada <a rel="nofollow" target="_blank"
								href="http://ludonoticias.com/2014/03/08/osprey-publishing-crea-su-division-de-juegos/">
								Osprey Publishing crea su division de juegos</a> aparece primero en
								<a rel="nofollow" target="_blank" href="http://ludonoticias.com">LudoNoticias, todo sobre juegos de mesa y simulacion</a>.</p><br />Source:
								<a href="
								http://ludonoticias.com/2014/03/08/osprey-publishing-crea-su-division-de-juegos/?utm_source=rss&utm_medium=rss&utm_campaign=osprey-publishing-crea-su-division-de-juegos" class="bbc_link"
								target="_blank">Osprey Publishing crea su division de juegos</a><br />
								<br />Noticia gracias a: <a href="http://www.ludonoticias.com" class="bbc_link"
								target="_blank">http://www.ludonoticias.com</a></div>
							</div>
						</div>
						<div class="moderatorbar">
							<div class="smalltext modified" id="modified_1240391">
							</div>
							<div class="smalltext reportlinks"><g:plusone href="http://labsk.net/index.php?topic=128950" size="small"></g:plusone>
			<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script><a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
								<a href="http://labsk.net/index.php?action=reporttm;topic=128950.0;msg=1240391">Reportar al moderador</a> &nbsp;
								<img src="http://h2212313.stratoserver.net/Themes/SMFSimple_Theme_Skin_Samp/images/ip.gif" alt="" />
								<a href="http://labsk.net/index.php?action=helpadmin;help=see_member_ip" onclick="return reqWin(this.href);" class="help">En </a>
							</div>
						</div>
					</div>
					<span class="botslice"><span></span></span>
        """
)

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
        self.threadscalled = 0
        self.mockthread = {'title':""}

    def saveThread(self, thread):
        self.treadssaved += 1
        self.listofthreads.append(thread)
        # print thread

    def threads(self):
        self.threadscalled += 1
        return self.find_all()

    def find_one_by(self, field, value):
        return None

    def find_all(self):
        return self.listofthreads


class ObjectId(object):
    """Mock for using SON copied from MondoDB """
    def __init__(self, key):
        pass


class Reports(object):
    """ Sample reports
    """
    asylum = {'Polis':
                  [{u'source': u'LaBSK', u'_id': ObjectId('530370f6c6a54a1a4c3d83a2'),
                    u'link': u'http://labsk.net/index.php?topic=97887.0',
                    u'msgs': [{u'date': u' 21 de Noviembre de 2012, 10:28:38 am \xbb',
                               u'body': u'ASEG\xdaRATE DE QUE TU DUDA NO EST\xc9 YA RESPONDIDA.\n LEE PRIMERO ESTAS FAQ ANTES DE PREGUNTAR.PREPARACI\xd3N Y COMPONENTESLas flechas representan el comercio exterior, por eso se consiguen monedas en esas zonas de mar.Las 5 fichas de cart\xf3n redondas que representan a las criaturas fueron dise\xf1adas cuando las equivalentes a miniaturas en pl\xe1stico no estaban todav\xeda listas. Pueden usarse como recordatorio respecto a qu\xe9 jugador la tiene a su servicio. Ten en cuenta que en muchas ocasiones, la criatura jugada no tiene por qu\xe9 ponerse en una isla tuya, y eso puede inducir a error.SOBRE EL FUNCIONAMIENTO DEL CICLOAs\xed es.LOS INGRESOSNo.LAS OFRENDAS (LA PUJA)El orden para pujar es inverso al orden en que se hicieron las acciones en el turno anterior.La puja es a tantas vueltas como sea necesario. Si te sobrepujan, t\xfa ser\xedas el siguiente en pujar y no lo podr\xedas hacer al mismo dios. Cuando todos los jugadores pujan por un dios y no se sobrepuja a nadie es cuando acaba.No tiene por qu\xe9: te "echan" de ese dios y t\xfa sobrepujas a otro, desplaz\xe1ndolo a su vez, que deber\xe1 desplazar a otro y quiz\xe1s ese otro acabe por sobrepujarte a ti, con lo que puede que regreses a ese dios. Adem\xe1s, si un determinado dios es vital para ti, deber\xedas hacerle una ofrenda "extraordinariamente generosa" para evitar que cualquier advenedizo te pueda mover con unas pocas monedas. Ahora, si eres un taca\xf1o... Otra manera de jugar es al despiste, arriesg\xe1ndote y no yendo primero al que quieres.S\xed.Seg\xfan las reglas: cada sacerdote reduce el coste de la ofrenda a pagar al comienzo del ciclo en una pieza de oro... Y es una moneda por sacerdote. As\xed que si es una partida de dos jugadores y tienes un sacerdote y has "ofrendado" por Ares 3 y por Zeus 4, y te las llevas, pagas 6. LAS ACCIONESExacto.No y no.No puedes destruir edificios (excepto con el gigante) a no ser que sea para construir una metr\xf3polis. Y nunca puedes trasladar edificios.No es una restricci\xf3n visual, es una restricci\xf3n real. Solo se puede construir edificios en los espacios libres, la excepci\xf3n es cuando colocas una Metr\xf3polis que si hay lugares ocupados, puedes destruir el edificio para poner la Metr\xf3polis.S\xed, las acciones inmediatas de las criaturas son obligatorias, mientras se pueda (Ej.: Se puede comprar el S\xe1tiro, aunque no hayan fil\xf3sofos para robar). \xa0La excepci\xf3n son el Silfo y la Esfinge, cuyas acciones son opcionales.Seg\xfan las reglas: \x93La carta de la criatura se descarta s\xf3lo cuando realizas las acciones de tu dios durante el siguiente Ciclo", con lo que la carta la tienes ante ti y nadie m\xe1s puede contratar a ese bicho simult\xe1neamente. Tampoco t\xfa puedes contratarlo durante tu segundo turno, porque la carta se descarta al final de tus acciones. Eso se aplica a todas las figuras excepto al kraken, cuya carta va directamente a la pila de descartes.S\xed: una segunda figura que hiciese su aparici\xf3n en esa isla destruir\xeda a la primera y ambas figuras se eliminar\xedan.Se quedan en la isla donde se ponen hasta que le llegue el turno de nuevo al jugador que las puso (excepto el kraken, que se queda en el sitio hasta que alguien vuelva a jugar su carta).DUDAS SOBRE DIOSES EN CONCRETOSi no puedes colocarla , autom\xe1ticamente pierdes los 4 fil\xf3sofos obtenidos con esfuerzo.S\xed, es leg\xedtima la maniobra. El poder especial de Zeus lo puedes invocar tantas veces te lo permita tu dinero (teniendo en cuenta que el descuento por templo se usa solo una vez por turno), pero como mucho podr\xe1s usar 3 CARTAS, ya que el poder de Zeus permite CAMBIAR cartas pero no colocar cartas nuevas en espacios vac\xedos. Adem\xe1s, se debe tener en cuenta que si la Chimera va a la pila de descartes, se vuelve a mezclar todo el mazo.S\xed, aunque es dif\xedcil que se agoten. Pero a\xfan as\xed Apolo sigue dando oro, eso si, ya dar\xeda igual ser el primero en pujar por \xe9l.No.DUDAS SOBRE CRIATURAS EN CONCRETOEl Silfo habla de TUS FLOTAS, al contrario que Poseid\xf3n que especifica que puedes mover UNA flota 3 espacios. La carta otorga en realidad lo que comentas, 10 movimientos a cualquiera/todas tus flotas. Respecto a lo de entrar en batalla, luego de esta puedes seguir moviendo, al contrario que con Poseid\xf3n.El coste inicial del Kraken para ponerlo en el tablero es el que sea, dependiendo del n\xfamero de templos que tengas. Una vez puesto en el tablero (y arrasado convenientemente) puedes moverlo un espacio (con el consiguiente destrozo) al coste de una moneda. Esto lo peudes hacer tantas veces como quieras. Es decir, si pagas el coste y adem\xe1s tres monedas extras, podr\xe1s poner al kraken y moverlo tres veces por el tablero, arrasando con todo.No, es la figura la que permanece (en el tablero). La carta va directa al mazo de descartes.Si el Minotauro est\xe1 s\xf3lo defendiendo una isla, el atacante debe ganar o empatar una ronda con los dados para vencer al Minotauro. \xa0Es decir, si bien esta criatura vale como dos, s\xf3lo se aplica para aumentar el poder de los dados y no es que se le tenga que ganar dos veces.S\xed, Polifemo fecta tanto los barcos propios como ajenos.S\xed.Error: una vez que todos los jugadores han elegido a su dios correspondiente se realiza el pago de las ofrendas de TODOS los jugadores. Por ello, cuando llega el turno de esquilmarle a alguien la mitad de sus ingresos, la deuda con su dios ya ha quedado satisfecha, con lo que podr\xe1 hacer cuanto pueda con el dinero que le quede.Cuando alguien compra la Quimera, cuando alguien la sabotea con Zeus o cuando esta llega a la pila de descartes sin ser comprada.LA BATALLAEl jugador que consiga la ofrenda a Ares puede atacar con las tropas terrestres, adem\xe1s de todos los efectos que conlleva Ares, y del mismo modo con Poseidon. Adem\xe1s, algunas criaturas te permiten destruir tropas o flotas sin necesidad de haber ganado dichas ofrendas.Solo cuando te est\xe1n atacando.Te las quedas.', u'user': u'Galaena'},
                              {u'date': u' 24 de Diciembre de 2012, 01:32:10 pm \xbb', u'body': u'Una duda:Gano la puja por Ares.Tengo 5 soldados en una isla, pago 1 moneda y los llevo a otra isla, combato, gano.Vuelvo a pagar 1 moneda y desplazo otra vez a esos 5 soldados a una tercera isla, combato, ganoCompro a Pegaso, muevo a los 5 soldados a una cuarta isla, combato, gano.He ganado 3 metr\xf3polis de una tacada.....Esto nos pas\xf3 el otro d\xeda, evidentemente quien lo hizo gan\xf3 la partida....\xbfEs legal?', u'user': u'Brux'},
                              {u'date': u' 22 de Febrero de 2013, 04:50:33 pm \xbb', u'body': u'En las reglas solo se indica que se puede destruir un edificio para construir una metropolis. Sobre destruir un edificio para poner otro no dice nada ', u'user': u'mrkaf'},
                              {u'date': u' 22 de Febrero de 2013, 11:20:48 pm \xbb', u'body': u'Pero la Metr\xf3polis en realidad es un edificio. En las reglas no pondr\xe1 nada sobre destruir un edificio propio (no metr\xf3polis) para construir otro porque salvo en alg\xfan caso concreto no creo que sea algo muy pr\xe1ctico. Nosotros llevamos muchas partidas y nunca se ha dado el caso\xa0 ', u'user': u'Zaranthir'},
                              {u'date': u' 23 de Febrero de 2013, 10:47:37 am \xbb', u'body': u'No se puede, est\xe1 confirmado en el FAQ oficial:Solo se puede (debe) destruir si vas a contruir una metr\xf3polis o con el Gigante.', u'user': u'Galaena'}
                    ], u'title': u'CYCLADES (DUDAS)'}],
              'title': 'Result for report Informe de Asylum Games', ''
              'Banjooli': [
                {u'source': u'LaBSK', u'_id': ObjectId('530370a9c6a54a1a4c3d837c'),
                 u'link': u'http://labsk.net/index.php?topic=119092.0',
                 u'msgs': [{u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb',
                            u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}],
                 u'title': u'ESSEN 2013 - Emisi\xf3n en Streaming'}
                ],
              'report_date': "19/02/2014",
              'Mutinies': [
                  {u'source': u'LaBSK', u'_id': ObjectId('530370a9c6a54a1a4c3d837c'),
                   u'link': u'http://labsk.net/index.php?topic=119092.0',
                   u'msgs': [{u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb', u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.En el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}], u'title': u'ESSEN 2013 - Emisi\xf3n en Streaming'}],
              'Asylum Games': [{u'source': u'LaBSK', u'_id': ObjectId('530370a9c6a54a1a4c3d837c'),
                                u'link': u'http://labsk.net/index.php?topic=119092.0',
                                u'msgs': [{u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb', u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.En el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}], u'title': u'ESSEN 2013 - Emisi\xf3n en Streaming'}
              ]}

    asylum_msg_list = [{u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb',
                u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}
                ]

    asylum_keywords = ('Asylum Games', 'Banjooli', 'Mutinies', 'Polis')

    asylum_report_request = {'name': 'Informe de Asylum Games',
                           'keywords': ["Asylum Games", "Polis", "Mutinies", "Banjooli"]}
    threats_with_newline = {u'source': u'LaBSK', u'_id': ObjectId('530370a9c6a54a1a4c3d837c'),
                     u'link': u'http://labsk.net/index.php?topic=119092.0',
                     u'msgs': [{u'id':'msg_1169262',
                                   u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb',
                                u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued",
                                u'user': u'winston smith'}
                              ],
                 u'title': u'ESSEN 2013 - Emisi\xf3n en Streaming',
                 }

    report_stat_json = {u'stats': [{u'date': u'2014-3-22', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'},
                              {u'date': u'2014-3-23', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'},
                              {u'date': u'2014-3-24', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'},
                              {u'date': u'2014-3-25', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'},
                              {u'date': u'2014-3-26', u'blogs': u'0', u'threads': u'0', u'msgs': u'0'}],
                   u'name': u'HootBoardGame'}

    edge_report_stats = {u'stats': [{u'date': u'2014-3-26', u'blogs': u'0', u'threads': u'324', u'msgs': u'1207'}],
                         u'name': u'Editorial EDGE Entertainment'}

    @staticmethod
    def get_asylum_thread():
        thread = Reports.threats_with_newline.copy()
        thread['msgs'] = list()
        for msg in Reports.threats_with_newline['msgs']:
            thread['msgs'].append(msg.copy())
        return thread

    @staticmethod
    def get_asylum_report():
        report = Reports.asylum.copy()
        for word in Reports.asylum_keywords:
            report[word] = list()
            for t in Reports.asylum[word]:
                new_t = t.copy()
                report[word].append(new_t)
                new_t['msgs'] = list()
                for msg in t['msgs']:
                    new_t['msgs'].append(msg.copy())

        return report

    @staticmethod
    def get_asylum_polis_thread():
        report = Reports.get_asylum_report()
        return report['Polis'][0]


class MockDatetime(object):

    def __init__(self, date = None):
        self.dt = self.set_datetime("01/01/2014", "14:10")

    def now(self):
        return self.dt

    def set_datetime(self, date, hour):
        datos_hora = hour.split(':')
        datos_fecha = date.split('/')
        self.dt = datetime(int(datos_fecha[2]), int(datos_fecha[1]), int(datos_fecha[0]),
                    int(datos_hora[0]), int(datos_hora[1]))
        return self.dt


class MockKimonoPlanetaLudicoAPI(object):

    json = {
         "name": "planeta_ludico",
        "count": 15,
     "frequency": "hourly",
     "version": 13,
  #"newdata": false,
  "lastrunstatus": "success",
  "lastsuccess": "Fri Mar 21 2014 20:57:35 GMT+0000 (UTC)",
  "nextrun": "Fri Mar 21 2014 21:57:35 GMT+0000 (UTC)",
  "results": {
    "titles": [
      {
        "title": {
          "href": "http://mijuegodelmes.com/2014/03/21/lla-partida-y-iii/",
          "text": u"LA  Partida y III"
        },
        "date": "21 marzo, 2014",
        "source": {
          "href": "http://planetaludico.es/author/mi-juego-del-mes/",
          "text": u"Mi Juego del Mes"
        }
      },
      {
        "title": {
          "href": "http://feedproxy.google.com/~r/analisis-paralisis-web/~3/1SX8WcZVKBc/",
          "text": u"Desprecintando Lewis Clark"
        },
        "date": "21 marzo, 2014",
        "source": {
          "href": "http://planetaludico.es/author/ushikai/",
          "text": u"Ushikai"
        }
      }
    ]
  }
    }

    entry_json =  {
        "title": {
          "href": "http://feedproxy.google.com/~r/analisis-paralisis-web/~3/1SX8WcZVKBc/",
          "text": u"Desprecintando Lewis Clark"
        },
        "date": "21 marzo, 2014",
        "source": {
          "href": "http://planetaludico.es/author/mi-juego-del-mes/",
          "text": u"Mi Juego del Mes"
        }
    }