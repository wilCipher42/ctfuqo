import os
import time  # <-- AJOUTEZ CECI
from flask import Flask, render_template, request
from neo4j import GraphDatabase, basic_auth
import atexit

app = Flask(__name__)

# Récupérer les infos de connexion depuis les variables d'environnement
uri = os.getenv("NEO4J_URI", "neo4j://db:7687")
user = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "password123")


def connect_to_db():
    """Tente de se connecter à la BDD avec plusieurs essais."""
    retries = 10
    delay = 5  # secondes
    
    for i in range(retries):
        try:
            # Tente de créer le driver
            driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))
            
            # Tente une vraie connexion pour vérifier que tout est prêt
            # C'est cette ligne qui va échouer avec "Cannot resolve address"
            driver.verify_connectivity() 
            
            print("Connexion à Neo4j réussie !")
            return driver
            
        except Exception as e:
            print(f"Échec de la connexion à Neo4j (Essai {i+1}/{retries}): {e}")
            if i < retries - 1:
                print(f"Nouvel essai dans {delay} secondes...")
                time.sleep(delay)
            else:
                print("Impossible de se connecter à Neo4j. Abandon.")
                raise e # Fait planter le conteneur, ce qui est correct

# Initialiser le driver en appelant la fonction
# Le script va "pauser" ici jusqu'à ce que la connexion réussisse


driver = connect_to_db()


def init_db():
    """Initialise la base de données avec l'utilisateur et le drapeau."""
    with driver.session() as session:
        # Nettoyer la base pour les redémarrages
        session.run("MATCH (n) DETACH DELETE n")
        
        # Créer l'utilisateur admin avec le drapeau
        session.run("""
            CREATE (u:User {
                name: 'admin', 
                password: 'DifficultPassword!@#$', 
                flag: 'CTF{Cyph3r_1nj3cti0n_R0cks!}'
            })
        """)
        print("Base de données initialisée avec l'utilisateur 'admin'.")

@app.route('/', methods=['GET', 'POST'])
def login():
    message = "Veuillez vous connecter pour voir le drapeau."
    flag = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # --- LA FAILLE D'INJECTION CYPHERS ---
        # La requête est construite par concaténation.
        # C'est dangereux car l'utilisateur contrôle les variables `username` et `password`.
        
        query = "MATCH (u:User {name: '" + username + "', password: '" + password + "'}) RETURN u.name AS name, u.flag AS flag"
        
        print(f"Executing query: {query}") # Utile pour le debug (et pour le CTF !)
        
        try:
            with driver.session() as session:
                result = session.run(query)
                record = result.single()
                
                if record:
                    message = f"Connexion réussie ! Bienvenue, {record['name']}."
                    flag = record['flag']
                else:
                    message = "Échec de la connexion. Nom d'utilisateur ou mot de passe incorrect."
        except Exception as e:
            message = f"Une erreur est survenue : {str(e)}"
            
    return render_template('index.html', message=message, flag=flag)

# S'assurer de fermer la connexion à la BDD
@atexit.register
def close_driver():
    driver.close()

# Initialiser la BDD au démarrage de l'app
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)