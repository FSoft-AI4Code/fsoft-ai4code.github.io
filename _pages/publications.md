---
title: "FSoft AI4Code- Publications"
layout: gridlay
excerpt: "FSoft AI4Code -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

{% for publi in site.data.publist %}

  <b>{{ publi.title }} </b> <br />
  <em>{{ publi.authors }} </em><br />
  {{ publi.conference }}
  (<a href="{{ publi.link.url }}">Github</a>)

{% endfor %}
