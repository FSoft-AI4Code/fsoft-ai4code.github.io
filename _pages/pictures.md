---
title: "FSoft AI4Code - Pictures"
layout: piclay
excerpt: "FSoft AI4Code -- Pictures"
permalink: /pictures/
---

# Gallery




{% assign number_printed = 0 %}
{% for pic in site.data.pictures %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/gallery/{{ pic.image }}" class="img-responsive" width="150%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


<p> &nbsp; </p>
