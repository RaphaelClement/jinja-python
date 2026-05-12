from jinja2 import Template

with open('pod.conf.j2', 'r') as fichier_template:
   value = fichier_template.read()
gen_jinja = Template(value)

data = {
    "nom_du_pod": "test-auto",
    "type_app": "frontend",
    "nom_du_conteneur": "nginx-serv",
    "nom_image": "nginx",
    "version_image": "alpine",
    "port_interne": 80
}

yaml_final = gen_jinja.render(data)
nom_fichier_sortie = "deploiement_genere.yaml"
with open(nom_fichier_sortie, 'w') as fichier_sortie:
    fichier_sortie.write(yaml_final)

print(f"done")
