# arduino_photon_to_GUI_sqlite_css3_graph.js
<h1>ARDUINO PHOTON TO GUI SQLITE CSS3 GRAPH.JS</h1>
<br/>
1 - installer les librairies javascipt necessaire
<br/>
2 - televerser le code arduino.ino
<br/>
3 - Creer base de donnée sqlite avec script sqlite.py
<br/>
4 - lancer l'interface visuel GUI (avec ou sans sqlite)
<br/>
5 - lancer l'interface web pour visualiser la courbe du capteur en utilisant graph.js.
<br/><br/>
<a href="https://ibb.co/dr6r2Z8"><img src="https://i.ibb.co/0cZcM5H/Nouveau-projet-5.jpg" alt="Nouveau-projet-5" border="0"></a>
<br/><br/>
<h2>appgui_avecsqlite.py</h2>
<br/><a href="https://ibb.co/DQ2pZC2"><img src="https://i.ibb.co/0rbtxMb/guitemp.png" alt="guitemp" border="0"></a><br/>
<p>Ce projet est une interface graphique d&eacute;velopp&eacute;e avec Python et Tkinter pour surveiller les donn&eacute;es d'un capteur connect&eacute; via un port s&eacute;rie. Les donn&eacute;es captur&eacute;es sont stock&eacute;es dans une base de donn&eacute;es SQLite, affich&eacute;es en temps r&eacute;el sous forme de graphique, et une jauge de progression visualise la valeur actuelle du capteur. Ce projet permet &eacute;galement de d&eacute;finir une plage de temps pour visualiser plus ou moins de points de donn&eacute;es sur le graphique.</p>
<h3>Fonctionnalit&eacute;s Principales</h3>
<ol>
<li>
<p><strong>Communication S&eacute;rie</strong> :</p>
<ul>
<li>Le projet communique avec un capteur (par exemple, un capteur analogique Arduino) via le port s&eacute;rie configur&eacute; &agrave; un taux de 9600 bauds.</li>
<li>Les donn&eacute;es sont lues et trait&eacute;es en temps r&eacute;el, puis affich&eacute;es dans l'interface.</li>
</ul>
</li>
<li>
<p><strong>Stockage des Donn&eacute;es dans SQLite</strong> :</p>
<ul>
<li>Les donn&eacute;es re&ccedil;ues du capteur sont enregistr&eacute;es dans une base de donn&eacute;es SQLite. Chaque enregistrement est horodat&eacute; automatiquement.</li>
</ul>
</li>
<li>
<p><strong>Interface Graphique avec Tkinter</strong> :</p>
<ul>
<li>L'interface utilisateur est construite avec <strong>Tkinter</strong>, avec une palette de couleurs sombres et des widgets stylis&eacute;s.</li>
<li>Un graphique en temps r&eacute;el montre l'&eacute;volution des valeurs du capteur. Ce graphique est g&eacute;n&eacute;r&eacute; avec <strong>Matplotlib</strong> et int&eacute;gr&eacute; dans la fen&ecirc;tre Tkinter.</li>
<li>Une jauge de progression visualise la valeur du capteur sous forme de pourcentage.</li>
</ul>
</li>
<li>
<p><strong>Choix de la Plage de Temps</strong> :</p>
<ul>
<li>L'utilisateur peut s&eacute;lectionner la plage de temps (en nombre de points) &agrave; afficher sur le graphique. Un menu d&eacute;roulant et un bouton "Appliquer" permettent de mettre &agrave; jour cette plage dynamiquement.</li>
</ul>
</li>
<li>
<p><strong>Gestion d'Erreurs</strong> :</p>
<ul>
<li>Le code g&egrave;re les erreurs de connexion au port s&eacute;rie et d'acquisition des donn&eacute;es. Si une donn&eacute;e non valide ou hors des limites est re&ccedil;ue, elle est trait&eacute;e et affich&eacute;e &agrave; l'utilisateur.</li>
</ul>
</li>
</ol>
<h3>Biblioth&egrave;ques Utilis&eacute;es</h3>
<ul>
<li><strong>serial</strong> : Pour la communication avec le port s&eacute;rie.</li>
<li><strong>time</strong> : Pour la gestion des temporisations.</li>
<li><strong>Tkinter</strong> : Pour la cr&eacute;ation de l'interface utilisateur.</li>
<li><strong>Matplotlib</strong> : Pour la visualisation des donn&eacute;es du capteur sous forme de graphique.</li>
<li><strong>sqlite3</strong> : Pour la gestion et le stockage des donn&eacute;es dans une base de donn&eacute;es locale SQLite.</li>
<li><strong>NumPy</strong> : Pour la gestion efficace des tableaux et des donn&eacute;es num&eacute;riques.</li>
</ul>
<h3>Fonctionnement du Code</h3>
<ol>
<li>
<p><strong>Configuration et Connexion S&eacute;rie</strong> :</p>
<ul>
<li>Le programme tente d'ouvrir le port s&eacute;rie (d&eacute;fini &agrave; <code>COM4</code> par d&eacute;faut, &agrave; ajuster selon la configuration).</li>
<li>Si la connexion &eacute;choue, le programme ne continue pas.</li>
</ul>
</li>
<li>
<p><strong>Connexion &agrave; SQLite</strong> :</p>
<ul>
<li>Une table est cr&eacute;&eacute;e si elle n'existe pas d&eacute;j&agrave;, pour stocker les valeurs du capteur avec un horodatage.</li>
</ul>
</li>
<li>
<p><strong>Affichage des Donn&eacute;es</strong> :</p>
<ul>
<li>Les donn&eacute;es du capteur sont lues et affich&eacute;es dans l'interface graphique toutes les 100 ms.</li>
<li>Elles sont &eacute;galement enregistr&eacute;es dans la base de donn&eacute;es.</li>
</ul>
</li>
<li>
<p><strong>Mise &agrave; Jour du Graphique</strong> :</p>
<ul>
<li>Les valeurs r&eacute;centes sont trac&eacute;es en temps r&eacute;el sur un graphique.</li>
<li>La plage de temps peut &ecirc;tre ajust&eacute;e via l'interface (par exemple, 50 &agrave; 2000 points).</li>
</ul>
</li>
<li>
<p><strong>Fermeture Gracieuse</strong> :</p>
<ul>
<li>&Agrave; la fermeture de la fen&ecirc;tre Tkinter, le port s&eacute;rie et la connexion &agrave; la base de donn&eacute;es sont proprement ferm&eacute;s.</li>
</ul>
</li>
</ol>
<h3>Utilisation</h3>
<ol>
<li>
<p><strong>Pr&eacute;requis</strong> :</p>
<ul>
<li>Assurez-vous d'avoir Python 3.x install&eacute; ainsi que les biblioth&egrave;ques n&eacute;cessaires : <code>pyserial</code>, <code>tkinter</code>, <code>matplotlib</code>, <code>numpy</code>, <code>sqlite3</code>.</li>
</ul>
</li>
<li>
<p><strong>Ex&eacute;cution</strong> :</p>
<ul>
<li>Lancez le script Python apr&egrave;s avoir connect&eacute; votre capteur via un port s&eacute;rie (modifiez <code>COM4</code> selon votre configuration).</li>
</ul>
</li>
<li>
<p><strong>Interface</strong> :</p>
<ul>
<li>La fen&ecirc;tre principale affiche la valeur actuelle du capteur, la jauge de progression, et un graphique des donn&eacute;es.</li>
<li>Utilisez le menu d&eacute;roulant pour ajuster la plage de temps du graphique.</li>
</ul>
</li>
</ol>
<br/>
<h2>api_to_generate_html.py</h2>
<br/><a href="https://ibb.co/jLDtb77"><img src="https://i.ibb.co/tbDRQyy/repssssss.png" alt="repssssss" border="0"></a><br/>
<p>Ce projet est une application web bas&eacute;e sur Flask, qui permet de visualiser les donn&eacute;es collect&eacute;es par un capteur &agrave; partir d'une base de donn&eacute;es SQLite. L'application sert une page HTML et expose une API pour acc&eacute;der aux donn&eacute;es du capteur sous forme de JSON. Cette application est id&eacute;ale pour les projets IoT ou autres o&ugrave; les donn&eacute;es du capteur doivent &ecirc;tre visualis&eacute;es ou trait&eacute;es dans une interface web.</p>
<h3>Fonctionnalit&eacute;s Principales</h3>
<ol>
<li>
<p><strong>Serveur Web avec Flask</strong> :</p>
<ul>
<li>L'application utilise Flask pour cr&eacute;er un serveur web simple.</li>
<li>Une page HTML est servie via Flask, accessible &agrave; la racine du site (<code>/</code>).</li>
<li>Une API est expos&eacute;e &agrave; l'URL <code>/data</code>, qui renvoie les donn&eacute;es du capteur au format JSON.</li>
</ul>
</li>
<li>
<p><strong>Connexion &agrave; une Base de Donn&eacute;es SQLite</strong> :</p>
<ul>
<li>Les donn&eacute;es des capteurs sont r&eacute;cup&eacute;r&eacute;es &agrave; partir d'une base de donn&eacute;es SQLite existante (<code>sensor_data.db</code>).</li>
<li>La table <code>capteur</code> contient les valeurs des capteurs et leurs horodatages.</li>
<li>Les donn&eacute;es sont extraites et organis&eacute;es en listes (une pour les timestamps et une pour les valeurs) et renvoy&eacute;es sous forme de r&eacute;ponse JSON.</li>
</ul>
</li>
<li>
<p><strong>Rendu HTML Dynamique</strong> :</p>
<ul>
<li>La page HTML est servie &agrave; partir du dossier <code>templates</code> via le fichier <code>index.html</code>.</li>
<li>Ce fichier peut &ecirc;tre utilis&eacute; pour afficher les donn&eacute;es de mani&egrave;re visuelle, par exemple avec un graphique JavaScript.</li>
</ul>
</li>
</ol>
<h3>Biblioth&egrave;ques Utilis&eacute;es</h3>
<ul>
<li><strong>Flask</strong> : Pour cr&eacute;er le serveur web et g&eacute;rer les routes.</li>
<li><strong>sqlite3</strong> : Pour interagir avec la base de donn&eacute;es SQLite o&ugrave; sont stock&eacute;es les donn&eacute;es des capteurs.</li>
<li><strong>jsonify</strong> : Pour retourner les donn&eacute;es sous forme de JSON dans une r&eacute;ponse HTTP.</li>
</ul>
<h3>Fonctionnement du Code</h3>
<ol>
<li>
<p><strong>Route Principale (<code>/</code>)</strong> :</p>
<ul>
<li>Cette route sert une page HTML (<code>index.html</code>) qui est le point d'entr&eacute;e principal de l'application web.</li>
<li>Le fichier <code>index.html</code> doit &ecirc;tre plac&eacute; dans un dossier nomm&eacute; <code>templates</code>, comme exig&eacute; par Flask.</li>
</ul>
</li>
<li>
<p><strong>Route API (<code>/data</code>)</strong> :</p>
<ul>
<li>Cette route interroge la base de donn&eacute;es SQLite pour r&eacute;cup&eacute;rer les donn&eacute;es du capteur.</li>
<li>Les donn&eacute;es sont organis&eacute;es en deux listes : une liste de timestamps et une liste de valeurs de capteur.</li>
<li>Ces donn&eacute;es sont ensuite renvoy&eacute;es au format JSON pour &ecirc;tre consomm&eacute;es par des clients (comme une interface JavaScript dans <code>index.html</code>).</li>
</ul>
</li>
<li>
<p><strong>Connexion &agrave; la Base de Donn&eacute;es</strong> :</p>
<ul>
<li>Une connexion &agrave; la base de donn&eacute;es <code>sensor_data.db</code> est ouverte &agrave; chaque requ&ecirc;te sur <code>/data</code>.</li>
<li>Les donn&eacute;es sont r&eacute;cup&eacute;r&eacute;es avec une simple requ&ecirc;te SQL : <code>SELECT timestamp, valeur FROM capteur</code>.</li>
<li>Apr&egrave;s r&eacute;cup&eacute;ration, la connexion est ferm&eacute;e pour &eacute;viter les fuites de ressources.</li>
</ul>
</li>
<li>
<p><strong>Ex&eacute;cution en Mode D&eacute;bogage</strong> :</p>
<ul>
<li>Le serveur est d&eacute;marr&eacute; en mode debug (<code>app.run(debug=True)</code>), ce qui permet de voir en direct les changements de code et d'afficher les erreurs de mani&egrave;re d&eacute;taill&eacute;e.</li>
</ul>
</li>
</ol>
<h3>Utilisation</h3>
<ol>
<li>
<p><strong>Pr&eacute;requis</strong> :</p>
<ul>
<li>Assurez-vous d'avoir Python 3.x install&eacute; ainsi que les biblioth&egrave;ques n&eacute;cessaires (<code>Flask</code> et <code>sqlite3</code>).</li>
<li>Assurez-vous &eacute;galement que la base de donn&eacute;es SQLite (<code>sensor_data.db</code>) est pr&ecirc;te et contient une table <code>capteur</code> avec les colonnes <code>timestamp</code> et <code>valeur</code>.</li>
</ul>
</li>
<li>
<p><strong>Ex&eacute;cution</strong> :</p>
<ul>
<li>Pour lancer le serveur, ex&eacute;cutez le script :
<div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950">
<div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">bash</div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1">Copier le code</button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python app.py </code></div>
</div>
</li>
<li>Acc&eacute;dez ensuite &agrave; l'application via un navigateur &agrave; l'adresse suivante : <a target="_new" rel="noopener">http://127.0.0.1:5000/</a>.</li>
</ul>
</li>
<li>
<p><strong>Consommation des Donn&eacute;es JSON</strong> :</p>
<ul>
<li>L'API peut &ecirc;tre appel&eacute;e via l'URL <code>/data</code>. Elle renvoie les donn&eacute;es sous forme JSON structur&eacute;es comme suit :
<div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950">
<div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">json</div>
<div class="sticky top-9 md:top-[5.75rem]">
<div class="absolute bottom-0 right-2 flex h-9 items-center">
<div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1">Copier le code</button></span></div>
</div>
</div>
<div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">{</span> <span class="hljs-attr">"timestamps"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"2024-10-20 14:30:00"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"2024-10-20 14:31:00"</span><span class="hljs-punctuation">,</span> ...<span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span> <span class="hljs-attr">"values"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-number">523</span><span class="hljs-punctuation">,</span> <span class="hljs-number">510</span><span class="hljs-punctuation">,</span> ...<span class="hljs-punctuation">]</span> <span class="hljs-punctuation">}</span> </code></div>
</div>
</li>
</ul>
</li>
<li>
<p><strong>Personnalisation de l'Interface HTML</strong> :</p>
<ul>
<li>Le fichier <code>index.html</code> dans le dossier <code>templates</code> peut &ecirc;tre personnalis&eacute; pour afficher les donn&eacute;es sous forme de tableau ou de graphique, en utilisant des biblioth&egrave;ques JavaScript comme Chart.js ou D3.js.</li>
</ul>
</li>
</ol>
<br/>
<h2>Schema de montage arduino</h2>
<br/>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/fqMqTTc/arduinotemp.png" alt="arduinotemp" border="0"></a><br /><a target='_blank' href='https://usefulwebtool.com/characters-cyrillic'>cyrillic character</a><br />

