---
title: "News"
layout: textlay
excerpt: "AI4Code Team at FPT Software AI Center, Vietnam."
sitemap: false
permalink: /allnews.html
---

# News
{% for article in site.data.news %}
<p><em>{{ article.date }}</em><br>
    {{ article.headline }}<br></p>
{% endfor %}

