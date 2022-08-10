# Templates

## Template Inclusion
{% include 'navbar.html'%}

## Include Template (MAIN) hosted on templates folder
<div>
    {% block content %} {% endblock %}
</div>

## Extend Template (MAIN) hosted on templates folder
<div>
{% extends 'main.html'%} 
</div>