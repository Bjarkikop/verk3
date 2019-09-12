<html>
<head>
<title>Index síða</title>

</head>
<body>
    
    <h1>Fréttir</h1>
    <a href="/">Home</a>
    {% for x in frettir %}
        <h2><a href="/home/{{ x[0] }}">{{ x[1] }}</a></h2>

    {% endfor %}
  

</body>
</html>