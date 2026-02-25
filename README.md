# Backend Python Dev

Dette er en Flask-app som krypterer data med Fernet og lagrer det i MariaDB.  
For sikkerhet bruker vi en hemmelig Fernet-nøkkel som ligger i `.env`. Denne **skal ikke deles**.

## Oppsett

1. Lag en `.env`-fil i roten av prosjektmappen:
  den skal eventuelt se ut som dette: FERNET_KEY=<din-egen-tilfeldige-32-byte-base64-nøkkel>

2. lag nøkkelen
   du kan bruke den ferdiglagde filen "lag_nokkel.py" for i lage din private Fernet nøkkel.
   ```python
   python lag_nokkel.py


