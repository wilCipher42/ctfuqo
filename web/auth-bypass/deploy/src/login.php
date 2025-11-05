<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Connexion — Mon Site</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
</head>

<!--
<body>
    
    <div class="container">
        <header class="card">
            <nav>
                <div class="brand">
                    <span class="logo" aria-hidden="true"></span>
                    <span>Mon Site</span>
                </div>
                <div class="menu" aria-label="Navigation principale">
                    <a href="index.html">Accueil</a>
                    <a href="#" class="active">Login</a>
                </div>
            </nav>
        </header>

        <main>
            <section class="card" aria-labelledby="login-title" style="max-width: 400px; margin: 0px auto;">
                <h1 id="login-title">Connexion</h1>
                <form class="login-field" action="check-auth.php" method="post">
                    <label>
                        <input type="text" name="username" placeholder="Nom d'utilisateur" required>
                    </label>
                    <label>
                        <input type="password" name="password" placeholder="Mot de passe" required>
                    </label>
                    <div style="display:flex;gap:8px;align-items:center;justify-content:flex-end;margin-top:8px;">
                        <button type="submit" class="primary">Se connecter</button>
                    </div>
                </form>
            </section>
        </main>
        
        <footer>
            © <span></span>2025 REI — CTF Uqo 
        </footer>
    </div>

    
</body>
-->
<body>

  <!-- NAVBAR -->
  <nav>
        <div class='logo'>Rassemblement des Etudiants en Informatique</div>
    <ul>
      <li><a href="index.html">Accueil</a></li>
      <li><a href="#">Connexion</a></li>
    </ul>
  </nav>

  <!-- CONTENU -->
  <div class="login-container">
    <div class="login-box">
      <h2>Connexion</h2>
      <form action='check-auth.php' method='post'>
            <input type='text' name='username' placeholder='username' required>
            <input type='password' name='password' placeholder='Mot de passe' required>
            <button type='submit'>Se connecter</button>
        </form>
    </div>
  </div>
</body>
</html>