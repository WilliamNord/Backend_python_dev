# Backend Python Dev

Dette er en Flask-app som krypterer data med Fernet og lagrer det i MariaDB.  
For sikkerhet bruker vi en hemmelig Fernet-nøkkel som ligger i `.env`. Denne **skal ikke deles**.

## Teknologi
- Python 3
- Flask
- cryptography (Fernet)
- MariaDB

## Oppsett

1. Lag en venv fil
   for å lage et virituelt miljø kan du bruke disse kommandoene:
   ```python
   python -m venv venv
   ```
   macOS og Linux:
   ```python
   source venv/bin/activate
   ```
   windows:
   ```python
   venv\Scripts\activate
   ```
   Installer alle nødvendige pakker.
   ```python
   pip install -r requirements.txt
   ```
2. Lag en `.env`-fil i roten av prosjektmappen:
  den skal eventuelt se ut som dette:
  FERNET_KEY=<din-egen-tilfeldige-32-byte-base64-nøkkel>
   
3. lag nøkkelen
   du kan bruke den ferdiglagde filen "lag_nokkel.py" for i lage din private Fernet nøkkel.
   ```python
   python lag_nokkel.py
   ```
   Nøkkelen du får, skal du sette inn i .env-filen som du lagede i forje trinn.


4. Hvordan bruke mariaDB
   aller først må du installere mariaBD
   macOS:
   ```bash
   brew install mariadb
   brew services start mariadb
   ```
   Linux (Debian/Ubuntu):
   ```bash
   sudo apt update
   sudo apt install mariadb-server
   sudo systemctl start mariadb
   ```

   hvis du ikke har en bruker og trenger å logge inn uten passord:
   ```bash
   sudo mariadb -u root
   ```
   lag en ny bruker for prosjektet:
   ```SQL
   CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'sikker_passord';
   ```

5. Lag databasen
   dette prosjektet bruker mariaDB som database og koden er laget rundt dette.
   ```SQL
   CREATE DATABASE <database-navn>;
    USE <database-navn>;
    
    CREATE TABLE <table-navn> (
        id INT AUTO_INCREMENT PRIMARY KEY,
        encrypted_data BLOB,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
   ```
   når du har laget databasen må du la den nye brukeren din få rettigheter til å redigere den.
   ```SQL
   GRANT ALL PRIVILEGES ON <database-navn>.* TO 'brukernavn'@'localhost';
   ```
   ```SQL
   FLUSH PRIVILEGES;
   ```
   dette er et eksempel på hvordan denne prosessen kan se ut som:
   ```SQL
   CREATE USER 'cool-user'@'localhost' IDENTIFIED BY 'Web2026!';
   GRANT ALL PRIVILEGES ON cool-database.* TO 'cool-user'@'localhost';
   FLUSH PRIVILEGES;
   ```

   etter du har laget en bruker, kan du logge på som dette:
   ```SQL
   mariadb -u brukernavn -p
   ```

   
6. koble sammen database
   for å kunne la python lese og inserte ting i _din_ database, må skrive inn din brukers brukernavn og passord.
   du må kopiere inn dette og fylle inn din informasjon, den vil til slutt se slik ut:
   ```python
   FERNET_KEY=<din-genererte-nøkkel>
   
   DB_HOST=localhost
   DB_USER=ditt_brukernavn
   DB_PASSWORD=ditt_passord
   DB_NAME=backend_db
   ```
   disse variablene blir lest av python når du kjører prosjektet lokalt med egener verdier.


   
7. kjør appen
   Når du har fulgt denne guiden burde filene dine se slik ut:
   ```bash
   Backend_python_dev/
     static/
     templates/
     venv/
   
     .gitattributes
     .gitignore
     README.md
     app.py
     db.py
     lag_nokkel.py
     requirements.txt
     security.py
   ```

   når du har laget din egen database og koblet den sammen med python og flask, kan du kjøre appen med denne komandoen i terminalen:
   ```python
   python app.py
   ```


