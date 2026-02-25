# Backend Python Dev

Dette er en Flask-app som krypterer data med Fernet og lagrer det i MariaDB.  
For sikkerhet bruker vi en hemmelig Fernet-nøkkel som ligger i `.env`. Denne **skal ikke deles**.

## Oppsett

1. Lag en `.env`-fil i roten av prosjektmappen:
  den skal eventuelt se ut som dette:
  FERNET_KEY=<din-egen-tilfeldige-32-byte-base64-nøkkel>

3. lag nøkkelen
   du kan bruke den ferdiglagde filen "lag_nokkel.py" for i lage din private Fernet nøkkel.
   ```python
   python lag_nokkel.py
   ```
   nøkkelen du får skal du sette in i .env filen som du lagde tideligere.

4. lag databasen
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
5. koble sammen database
   
   
7. kjør appen
   når du har laget din egen database og koblet den sammen med python og flask, kan du kjøre appen med denne komandoen:
   ```python
   python app.py
   ```


