# {{ project_name }}

![example workflow](https://github.com/{{repo_owner}}/{{project_slug}}/actions/workflows/main.yml/badge.svg)

A [tackle-box](https://github.com/robcxyz/tackle-box) provider for...

### Usage

```shell
pip install tackle-box
tackle robcxyz/{{project_slug}}
```

{% if tests_enable %}
### Testing

```shell
make test
```
{% endif %}


### License

[{{ license }}](LICENSE)
