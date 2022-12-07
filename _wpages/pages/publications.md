---
layout: about
title: Publications
menutype: about
menu_order: 30
---



{% for pub in site.data.pub %}
<a id="PAPER_{{ pub.key }}"></a>
* **{{ pub.title }}** <br>
_{%- for auth in pub.authors -%}
{%- unless forloop.first -%}
{{- ", " -}}
{%- endunless -%}
{%- if site.data.people[auth] -%}
[{{- auth | replace: "Abhijit Mondal","**Abhijit Mondal**" -}}]({{ site.data.people[auth] }}){:.authorlink}{:target="_blank"}
{%- else -%}
{{- auth | replace: "Abhijit Mondal","**Abhijit Mondal**" -}}
{% endif %}
{%- endfor -%}_ <br>
{{ pub.publisher }} <br>
{%- if pub.links -%}
{%- for item in pub.links -%}
{%- if item[1] contains "://" -%}
[ <a href="{{ item[1] }}" target="_blank">{{ item[0] }}</a> ]
{%- else -%}
[ <a href="{{ site.baseurl }}/published/{{ pub.key }}/{{ item[1] }}" target="_blank">{{ item[0] }}</a> ]
{%- endif -%}
{%- if forloop.last -%}
<br>
<br>
{%- endif -%}
{%- else -%}
<br>
{%- endfor -%}
{%- else -%}
<br>
{%- endif -%}

{% endfor %}
