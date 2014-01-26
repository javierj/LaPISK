__author__ = 'Javier'

import unittest
from LaBSKApi.HTML2Objects import MsgFactory, AsuntoFactory
from bs4 import UnicodeDammit, BeautifulSoup

class HTMLFactory:
    def msg(self):
        return BeautifulSoup("""
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
        """)

    def asunto(self):
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
</tr>
        """)

class TestMsgFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().msg()
        self.factory = MsgFactory()

    def test_user(self):
        res = self.factory.createMsg(self.fragment)
        self.assertEqual(res['user'], "flOrO")

    def test_date(self):
        res = self.factory.createMsg(self.fragment)
        self.assertEqual(res['date'], u' 25 de Octubre de 2013, 12:12:00 pm \xbb')

    def test_body(self):
        res = self.factory.createMsg(self.fragment, "XX")
        self.assertEqual(res['body'], "XX")

    def test_(self):
        res = self.factory.createMsg(self.fragment, "XX")
        l = list()
        l.append(res)
        #print "List ", l
        self.assertEqual(len(l), 1)


class TestAsuntoFactory(unittest.TestCase):
    def setUp(self):
        self.fragment = HTMLFactory().asunto()
        self.factory = AsuntoFactory()

    def test_title(self):
        res = self.factory.create(self.fragment)
        print res['title']
        self.assertEqual(res['title'], u'Robinson Crusoe de Portal Games en espanol (al 95)')

    def test_link(self):
        res = self.factory.create(self.fragment)
        print res['link']
        self.assertEqual(res['link'], u'http://labsk.net/index.php?topic=126314.0')

if __name__ == '__main__':
    unittest.main()
