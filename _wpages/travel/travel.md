---
layout: travel
title: Travel
menutitle: Travel
menutype: None
menu_order: 100
---

# Travel

----

This page serves as a landing page for the list of my documented travels. I have a deep love for traveling, and I frequently find myself journeying to nearby locations as well as far-off destinations. I have been exploring various places since 2010. Nevertheless, it's quite challenging to capture all these experiences on this website. Therefore, I am sharing stories about the experiences I remember and cherish the most.

This entire website is dedicated to my travel experiences, which are entirely personal to me. Whether you like it or not, this documentation is about my adventures. Furthermore, it's important to note that these documents are not in the form of a blog; rather, they serve as a gallery to display my photos.

<br>


{% assign lastYear = "" %}
{% assign pages_list_travel = site.wpages | where: "menutype", "travel"  | sort: 'tripDate' | reverse %}
{% for node in pages_list_travel %}
    {% if node.title != null %}
    {% if node.menutype == "travel" %}
        {% assign curYear = node.path | split: "/" | slice: -2,1 %}
        {% if curYear != lastYear %}
### {{ curYear }}
        {% assign lastYear = curYear %}
        {% endif %}
* [{{ node.title }}]({{ site.baseurl }}{{ node.url }})
    {% endif %}
    {% endif %}
{% endfor %}
