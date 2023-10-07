install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

generate_and_push:
	# Create the markdown file 
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

transform_load: 
	python main.py transform_load

query:
	python main.py general_query "SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed, SUM(CASE WHEN outcome = 'team1' THEN 1 ELSE 0 END) AS TotalMatchesWon FROM (SELECT team1 AS team, 'team1' AS outcome FROM default.MatchesDB_ONE UNION ALL SELECT team2 AS team, 'team2' AS outcome FROM default.MatchesDB_ONE) AS MatchResults JOIN (SELECT team1 AS team, 'team1' AS outcome FROM default.WWC_MATCHES_2_DB UNION ALL SELECT team2 AS team, 'team2' AS outcome FROM default.WWC_MATCHES_2_DB) AS ActualResults ON MatchResults.team = ActualResults.team GROUP BY Team ORDER BY TotalMatchesPlayed DESC;"
