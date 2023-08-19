Såhär sätter du upp ditt venv.

1. Kör "pip install pipenv" i cmd.
2. Gå till önskad mapp, klona repot" git clone https://github.com/stalfilip/booking-sys.git"
3. I repot finns 2 viktiga filer, pipfile & pipfile.lock. Dessa innehåler all information om vilket venv vi kör.
    Dessa används för att ladda ner alla dependencies automatiskt.
4. Kör "pipenv shell".
5. Kör "pipenv sync", nu laddas alla dependences ner till ditt venv.
6. Kör "pipenv --venv", och du får nu en sökväg: path.
7. Gå in i VS Code och välj intepreter, lägg till din path/scripts/python.exe (alternativt stället där din python i din venv körs)
8. Klart! 