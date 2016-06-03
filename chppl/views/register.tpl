<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>chppL</title>
    <link href="css/bootstrap.css">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/bootstrap-theme.css" rel="stylesheet">
    <link href="css/bootstrap-theme.min.css">
  </head>
  <body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
        <div cladd="navbar-header">
          <a class="navbar-brand">chppL</a>
        <div>
        <ul class="nav navbar-nav">
          <li><a href="./">Getting started</a></li>
          <li class="active"><a href="./register">Register libraries</a></li>
          <li><a href="./search">Search libraries</a></li>
          <li><a href="./contact">Contact us</a><li>
        </ul>
      </div>
    </nav>

    <h2>Register Libraries</h2>
    <div class="container">
      <form class="form-horizontal" role="form">
        <div class="form-group">
          <label class="col-sm-2 control-label">GitHub URL</label>
          <div class="col-sm-10">
            <input type="url" class="form-control" placeholder="Your header-file URL on GitHub">
          </div>
        <div class="form-group">
          <label class="col-sm-2 control-label">Description</label>
          <div class="col-sm-10">
            <textarea class="form-control" rows="3"></textarea>
          </div>
        </div>
        <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">
            <button type="submit" class="btn btn-default">Register</button>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>
