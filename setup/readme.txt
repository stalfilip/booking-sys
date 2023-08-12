Jag använder VC Code för text editor.

Se till att köra: pip install -r requirements.txt för att ladda ner alla dependencies.

Förslagsvis kör du 'pipenv install ..' istället för att få ner till till en virtuell env (Praxis när man jobbar inom Djanog och Frontend, tydligen.. )

Bra video för att lära sig både om virituella env och grunderna inom Django är: https://www.youtube.com/watch?v=rHux0gMZ3Eg
Jag rekommender att kolla hela, och sedan också ladda ner DeBug programmet som han pratar om i slutet, verkligen bra.

När man kan det kan det vara lämpligt att läsa på lite om HTML och JS och likande. Resten går att köra genom GPT vilket
löser typ alla problem. 

Uttöver det måste du ha en fungerande MySQL server körandes på port: 3306 (localhost) med en databas som heter 'bookings' och en användare som heter 'ErkFil' med lösenord 'ErkFil'.

När du har det och du ser att den fungerar vill du migrera databasen med: 'python manage.py migrate' och sedan köra 'python manage.py runserver' för att starta servern och 
<<<<<<< HEAD
samtidigt skapa korrekt  tables i databasen. För att lägga till lite sampledata kan du köra 'source Populate.sql' när du är inloggad i MySQL servern och har bookings databasen vald.



