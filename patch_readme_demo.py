#!/usr/bin/env python3
# patch_readme_demo.py : annonce de Sandbox_BMoG dans le README du depot de demo (fr et en). ASCII, Python 3.8. A lancer a la racine du depot de demo.
import sys, os, datetime, json
EDITS = json.loads('{"README.md": [["**[Ouvrir Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.\\n", "**[Ouvrir Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.\\n- **Sandbox_BMoG, pour les PBR** : une r\\u00e9gion de la grille OpenSim **BloodMoon**, ajout\\u00e9e pour montrer les **mat\\u00e9riaux PBR** d\'OpenSim 0.9.3 et leur nouvel \\u00e9clairage. **[Ouvrir Sandbox_BMoG](https://klaatou.github.io/Web_3d_demo/index.html?region=Sandbox_BMoG/Sandbox_BMoG#spawn=default)**. Au centre de la r\\u00e9gion, un cercle est une zone de saut : on marche dessus (ou clic, ou `E`) pour ouvrir un lien `hop://` vers la r\\u00e9gion \\u00e9quivalente dans la grille BloodMoon (il faut un viewer OpenSim enregistr\\u00e9 pour `hop://` ; le navigateur demande confirmation). Merci \\u00e0 Vlad, propri\\u00e9taire de la grille.\\n"], ["**[Open Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.\\n", "**[Open Houses](https://klaatou.github.io/Web_3d_demo/index.html?region=houses/houses)**.\\n- **Sandbox_BMoG, for PBR**: a region of the **BloodMoon** OpenSim grid, added to show OpenSim 0.9.3 **PBR materials** and their new lighting. **[Open Sandbox_BMoG](https://klaatou.github.io/Web_3d_demo/index.html?region=Sandbox_BMoG/Sandbox_BMoG#spawn=default)**. In the middle of the region, a circle is a hop zone: walk onto it (or click it, or press `E`) to open a `hop://` link to the equivalent region in the BloodMoon grid (you need an OpenSim viewer registered for `hop://`; the browser asks for confirmation). Thanks to Vlad, the grid\'s owner.\\n"]]}')

def main():
    dry = "--dry-run" in sys.argv
    out = {}
    for f, l in EDITS.items():
        if not os.path.isfile(f):
            sys.exit("ERREUR : fichier introuvable : " + f + " (lance le patch a la racine du depot de demo)")
        raw = open(f, "rb").read()
        crlf = b"\r\n" in raw
        txt = raw.decode("utf-8")
        if crlf: txt = txt.replace("\r\n", "\n")
        for old, new in l:
            n = txt.count(old)
            if n != 1:
                sys.exit("ERREUR : %s : passage trouve %d fois (attendu 1) : %r : rien n'a ete touche" % (f, n, old[:70]))
            if new in txt:
                sys.exit("ERREUR : %s : annonce deja presente : rien n'a ete touche" % f)
            txt = txt.replace(old, new)
        if crlf: txt = txt.replace("\n", "\r\n")
        data = txt.encode("utf-8"); data.decode("utf-8")
        out[f] = data
    if dry:
        print("essai a blanc : %d fichier(s) seraient modifies : %s" % (len(out), ", ".join(sorted(out)))); return
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs("_bak", exist_ok=True)
    for f, data in out.items():
        open(os.path.join("_bak", f.replace("/", "__").replace("\\", "__") + ".bak-" + stamp), "wb").write(open(f, "rb").read())
        open(f, "wb").write(data)
    print("%d fichier(s) modifies : %s" % (len(out), ", ".join(sorted(out))))

main()
