# Backend Python Dev

Dette er en Flask-app som krypterer data med Fernet og lagrer det i MariaDB.  
For sikkerhet bruker vi en hemmelig Fernet-nøkkel som ligger i `.env`. Denne **skal ikke deles**.

## Oppsett

1. Lag en `.env`-fil i roten av prosjektmappen:
  den skal eventuelt se ut som dette:
  FERNET_KEY=<din-egen-tilfeldige-32-byte-base64-nøkkel>

2. lag nøkkelen
   du kan bruke den ferdiglagde filen "lag_nokkel.py" for i lage din private Fernet nøkkel.
   ```python
   python lag_nokkel.py
   ```
   Nøkkelen du får, skal du sette inn i .env-filen som du lagde tideligere.

3. Hvordan bruke mariaDB
   aller først må du installere mariaBD
   mac:
   ```bash
   brew install mariadb
   brew services start mariadb
   ```
   linux:
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
   ```bash
   CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'sikker_passord';
   ```

4. Lag databasen
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
   ```bash
   GRANT ALL PRIVILEGES ON <database-navn>.* TO 'brukernavn'@'localhost';
   ```
   ```bash
   FLUSH PRIVILEGES;
   ```
   dette er et eksempel på hvordan denne prosessen kan se ut som:
   ```bash
   CREATE USER 'cool-user'@'localhost' IDENTIFIED BY 'Web2026!';
   GRANT ALL PRIVILEGES ON cool-database.* TO 'cool-user'@'localhost';
   FLUSH PRIVILEGES;
   ```

   etter du har laget en bruker, kan du logge på som dette:
   ```bash
   mariadb -u brukernavn -p
   ```

   
5. koble sammen database
   for å kunne la python lese og inserte ting i _din_ database, må du skrive in brukeren sit brukernavn og passord
   du må kopiere inn dette og fylle inn din informasjon, den vil til slutt se slik ut:
   ```python
   FERNET_KEY=<din-genererte-nøkkel>
   
   DB_HOST=localhost
   DB_USER=ditt_brukernavn
   DB_PASSWORD=ditt_passord
   DB_NAME=backend_db
   ```
   
6. kjør appen
   når du har laget din egen database og koblet den sammen med python og flask, kan du kjøre appen med denne komandoen:
   ```python
   python app.py
   ```


