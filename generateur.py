from jinja2 import Template
with open('nginx.conf.j2', 'r') as fichier:
    contenu_template = fichier.read()
mon_template_jinja = Template(contenu_template)
mes_donnees = {
    "port": 443,
    "domaine": "test.dev",
    "dossier_racine": "/var/www/jinja-site",
    "securise": True,
    "admins": ["192.168.1.10", "10.0.0.5", "127.0.0.1"]
}
resultat_final = mon_template_jinja.render(mes_donnees)
print("=== FICHIER NGINX GÉNÉRÉ AVEC SUCCÈS ===\n")
print(resultat_final)
