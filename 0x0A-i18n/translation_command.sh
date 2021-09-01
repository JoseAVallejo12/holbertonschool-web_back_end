# generate translation base file
pybabel extract -F babel.cfg -o messages.pot .
wait
# generate trasnlation directory for each lenguaje
pybabel init -i messages.pot -d translations -l fr
pybabel init -i messages.pot -d translations -l en
wait

# generate each binary for lenguaje in directory translations/*
pybabel compile -d translations
