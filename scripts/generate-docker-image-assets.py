import requests
from jinja2 import Template

image_groups = [
    {
        "key": "alpine",
        "title": "docker-alpine-images",
        "description": "Repository for Docker Alpine Images",
        "src_repo": "docker-alpine-images"
    },
    {
        "key": "ci",
        "title": "docker-ci-images",
        "description": "Repository for Docker CI Images",
        "src_repo": "docker-ci-images"
    },
    {
        "key": "devcontainer",
        "title": "devcontainers",
        "description": "Repository for devcontainers",
        "src_repo": "devcontainers"
    },
    {
        "key": "ubuntu",
        "title": "docker-ubuntu-images",
        "description": "Repository for Docker Ubuntu Images",
        "src_repo": "docker-ubuntu-images"
    }
]

template = Template("""
{% for group in groups %}
## {{ group.title }}

{{ group.description }}

| # | Image | Group | URI | Latest Tag | Size(MB) | SHA256 | Source | Last Push |
|---|---|---|---|---|---|---|---|---|
{% for image in group.images -%}
| {{ loop.index }} | [{{ image.image_name.split('/')[-1] }}](https://gallery.ecr.aws/dev1-sg/{{ image.image_name }}) | {{ image.image_group }} | {{ image.uri }} | {{ image.latest_tag }} | {{ image.size_mb }} MB | {{ image.latest_sha }} | [Source](https://github.com/dev1-sg/{{ group.src_repo }}/tree/main/src/{{ image.image_name.split('/')[-1] }}) | {{ image.last_push }} |
{% endfor %}

{% endfor %}
""")

for group in image_groups:
    url = f"https://api.dev1-sg.com/v1/public/images/{group['key']}"
    group["images"] = next(iter(requests.get(url).json().values()))

print(template.render(groups=image_groups))
