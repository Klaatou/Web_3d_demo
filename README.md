# Démo de Web_3d / Web_3d demo

[Français](#français) | [English](#english)

[![Promenade sur la plage de PalmIsland / Walking on the beach of PalmIsland](https://raw.githubusercontent.com/Klaatou/Web_3d/main/docs/images/PalmIsland_demo.gif)](https://klaatou.github.io/Web_3d_demo/)

## Français

Quatre "régions" à visiter dans le navigateur (trois régions OpenSim et une galerie de photos en 3D), sans rien installer : **[ouvrir la démo](https://klaatou.github.io/Web_3d_demo/)**.

**[Menu des "régions" en démo](https://klaatou.github.io/Web_3d_demo/carte.html)**

- **Le projet** : [Web_3d](https://github.com/Klaatou/Web_3d) (présentation, documentation, code sous licence MIT).
- **Les régions** : PalmIsland (une île), Hobbit (un **fragment** de région : seule une partie a été sauvée dans l'OAR d'origine), ShowRoom3D (une galerie de photos en 3D, avec ses panneaux cliquables, du même genre que `galerie-photos.zip`) et **Houses**, nouvelle : une **grande région découpée en tuiles** (une galerie de maisons sur 4 x 4 régions). PalmIsland et Hobbit sont reliées par des portails, et `carte.html` affiche la carte des quatre.
- **Houses, une grosse région en "tuiles"** : la page affiche d'abord une vue d'ensemble légère, puis charge au fur et à mesure les morceaux (les "tuiles") proches du promeneur ; on ne télécharge jamais toute la région. **[Ouvrir Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.
- **Sandbox_BMoG, pour les PBR** : une région de la grille OpenSim **BloodMoon**, ajoutée pour montrer les **matériaux PBR** d'OpenSim 0.9.3 et leur nouvel éclairage. **[Ouvrir Sandbox_BMoG](https://klaatou.github.io/Web_3d_demo/index.html?region=Sandbox_BMoG/Sandbox_BMoG#spawn=default)**. Au centre de la région, un cercle est une zone de saut : on marche dessus (ou clic, ou `E`) pour ouvrir un lien `hop://` vers la région équivalente dans la grille BloodMoon (il faut un viewer OpenSim enregistré pour `hop://` ; le navigateur demande confirmation). Merci à Vlad, propriétaire de la grille.
- **Utilisation** : touche `P` pour se promener, `H` pour l'aide, `?` pour la présentation d'une région quand elle en a une.
- **Présence** : un serveur de présence, hébergé par l'auteur, permet de voir les autres visiteurs en promenade et de tchatter ; la carte indique combien de visiteurs sont en promenade dans chaque région.
- **Téléchargement** : la première ouverture télécharge les modèles (environ 13 Mo pour PalmIsland, 28 Mo pour Hobbit, 7 Mo pour ShowRoom3D). Pour Houses : environ 4 Mo pour la vue d'ensemble, puis les tuiles autour du promeneur (jusqu'à environ 200 Mo gardés en mémoire à la fois).
- **Navigateurs** : Edge et Chromium (Chrome) sont ceux avec lesquels le projet est testé ; Firefox et Safari n'ont pas été essayés.
- **Origine des contenus** : les modèles viennent du site [Outworldz](https://www.outworldz.com/cgi/freesculpts.plx?q=OAR-). Ils ne sont pas couverts par la licence MIT du code. Si tu es l'auteur d'un contenu et souhaites son retrait, ouvre une *issue* sur ce dépôt : il sera retiré.

### Chez vous, sans lire toute la documentation

Deux paquets prêts à l'emploi, à télécharger sur la [page des versions](https://github.com/Klaatou/Web_3d/releases/latest) :

- **`region-simple.zip`** : votre région OpenSim (un fichier GLB) dans un navigateur.
- **`galerie-photos.zip`** : une galerie de 30 photos en 3D.

Dézipper, lire `README.txt`, double-cliquer sur le lanceur (Windows, macOS) ou taper `sh lancer-region.sh` dans un terminal (Linux). Pour aller plus loin : le [guide](https://github.com/Klaatou/Web_3d/blob/main/docs/fr/GUIDE.md) du projet [Web_3d](https://github.com/Klaatou/Web_3d).

[![Carte des régions de la démo / Map of the demo regions](https://raw.githubusercontent.com/Klaatou/Web_3d/main/docs/images/carte.jpg)](https://klaatou.github.io/Web_3d_demo/carte.html)

## English

Four "regions" to visit in the browser (three OpenSim regions and a 3D photo gallery), with nothing to install: **[open the demo](https://klaatou.github.io/Web_3d_demo/)**.

**[Demo "regions" menu](https://klaatou.github.io/Web_3d_demo/carte.html)**

- **The project**: [Web_3d](https://github.com/Klaatou/Web_3d) (overview, documentation, MIT-licensed code).
- **The regions**: PalmIsland (an island), Hobbit (a **fragment** of a region: only a part was saved in the original OAR), ShowRoom3D (a 3D photo gallery with clickable panels, of the same kind as `galerie-photos.zip`) and **Houses**, new: a **large region split into tiles** (a gallery of houses over 4 x 4 regions). PalmIsland and Hobbit are linked by portals, and `carte.html` shows the map of the four.
- **Houses, a "tiled" big region**: the page first shows a light overview, then loads the pieces (the "tiles") near the walker as they go; the whole region is never downloaded. **[Open Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.
- **Sandbox_BMoG, for PBR**: a region of the **BloodMoon** OpenSim grid, added to show OpenSim 0.9.3 **PBR materials** and their new lighting. **[Open Sandbox_BMoG](https://klaatou.github.io/Web_3d_demo/index.html?region=Sandbox_BMoG/Sandbox_BMoG#spawn=default)**. In the middle of the region, a circle is a hop zone: walk onto it (or click it, or press `E`) to open a `hop://` link to the equivalent region in the BloodMoon grid (you need an OpenSim viewer registered for `hop://`; the browser asks for confirmation). Thanks to Vlad, the grid's owner.
- **Use**: press `P` to walk around, `H` for help, `?` for the presentation of a region when it has one.
- **Presence**: a presence server, hosted by the author, lets you see the other visitors who are walking and chat; the map shows how many visitors are walking in each region.
- **Download**: the first opening downloads the models (about 13 MB for PalmIsland, 28 MB for Hobbit, 7 MB for ShowRoom3D). For Houses: about 4 MB for the overview, then the tiles around the walker (up to about 200 MB kept in memory at once).
- **Browsers**: Edge and Chromium (Chrome) are the ones the project is tested with; Firefox and Safari have not been tried.
- **Origin of the content**: the models come from the [Outworldz](https://www.outworldz.com/cgi/freesculpts.plx?q=OAR-) site. They are not covered by the MIT licence of the code. If you are the author of a piece of content and want it removed, open an *issue* on this repository: it will be removed.

### At home, without reading all the documentation

Two ready-to-use packages, to download from the [releases page](https://github.com/Klaatou/Web_3d/releases/latest):

- **`region-simple.zip`**: your OpenSim region (a GLB file) in a browser.
- **`galerie-photos.zip`**: a 3D gallery of 30 photos.

Unzip, read `README.txt`, double-click the launcher (Windows, macOS) or type `sh lancer-region.sh` in a terminal (Linux). To go further: the [guide](https://github.com/Klaatou/Web_3d/blob/main/docs/en/GUIDE.md) of the [Web_3d](https://github.com/Klaatou/Web_3d) project.

[![Map of the demo regions](https://raw.githubusercontent.com/Klaatou/Web_3d/main/docs/images/carte.jpg)](https://klaatou.github.io/Web_3d_demo/carte.html)
