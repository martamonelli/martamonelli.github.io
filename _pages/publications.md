---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

I was contributing author to 14 additional LiteBIRD collaboration papers (2021–present). Full list available on <a href="https://inspirehep.net/authors/2153308">iNSPIRE</a>.
