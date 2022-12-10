all:
	@echo  "Para ejecutar el test de api1 use:"
	@echo  "make test"
	@echo  "Para ejecutar el test de api2 use:"
	@echo  "make test2"

API=http://localhost:5000/api/recipes
API2=http://localhost:5000/api2/recipes/

test: get post put delete
test2: get2 post2 put2 delete2

get:
	http GET $(API)
	http GET $(API)/5f7daa028ec9dfb536781afb 

post:
	http POST $(API) name="Flying Granadian" instructions:='["Get grenade juice and pour it into vodka"]' ingredients:='[{"name": "Scotch", "quantity": { "quantity":"1", "unit":"oz"}}]' slug="flying-granadian"

put:
	http PUT $(API)/5f7daa028ec9dfb536781afb instructions:='["This instructions have been modified by API1"]'

delete:
	http DELETE $(API)/63492a76abc82c754faf99bc


get2:
	http GET $(API2)
	http GET $(API2)/5f7daa028ec9dfb536781afb 

post2:
	http POST $(API2) name="Flying Granadian" instructions:='["Get grenade juice and pour it into vodka"]' ingredients:='[{"name": "Scotch", "quantity": { "quantity":"1", "unit":"oz"}}]' slug="flying-granadian"

put2:
	http PUT $(API2)/5f7daa028ec9dfb536781afb instructions:='["This instructions have been modified by API1"]'

delete2:
	http DELETE $(API2)/63492a76abc82c754faf99bc


