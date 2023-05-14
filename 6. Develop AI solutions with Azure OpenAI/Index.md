---
title: Azure OpenAI Exercises
permalink: index.html
layout: home
---

# Azure OpenAI Exercises

The following exercises are designed to support course material of this module. 


{% assign labs = site.pages | where_exp:"page", "page.url contains '/Instructions/Labs'" %}
{% for activity in labs  %}
- [{{ activity.lab.title }}]({{ site.github.url }}{{ activity.url }})
{% endfor %}