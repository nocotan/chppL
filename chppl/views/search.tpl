<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>chppL</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div cladd="navbar-header">
          <a class="navbar-brand">chppL</a>
        <div>
        <ul class="nav navbar-nav">
          <li><a href="./">Getting started</a></li>
          <li><a href="./register">Register libraries</a></li>
          <li class="active"><a href="./search">Search libraries</a></li>
          <li><a href="./contact">Contact us</a><li>
        </ul>
      </div>
    </nav>
    <div class="container">
      <div class="list-group">
        {% for item in search_list %}
          <a href="#" class="list-group-item">{{ item }}</a>
        {% endfor %}
      </div>
    </div>
  </body>
</html>
