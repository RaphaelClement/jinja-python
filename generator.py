from jinja2 import Template
with open('pod.conf.j2', 'r') as file_template:
   value = file_template.read()
gen_jinja = Template(value)
data = {
    "name_pod": "test-auto",
    "type_app": "frontend",
    "name_container": "nginx-serv",
    "name_image": "nginx",
    "version_image": "alpine",
    "port": 80
}
yaml_final = gen_jinja.render(data)
end_file = "deploy_pod.yaml"
with open(end_file, 'w') as fichier_sortie:
    fichier_sortie.write(yaml_final)
print(f"done")
