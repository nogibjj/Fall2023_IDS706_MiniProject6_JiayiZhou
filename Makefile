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
	python main.py general_query "SELECT MatchDate, t1.TeamName AS Team1Name, t2.TeamName AS Team2Name,
            m.Team1Goals, m.Team2Goals, m.Team1Goals + m.Team2Goals AS TotalGoals
            FROM default.matchesdb_one AS m
            JOIN team_names AS t1 ON m.Team1 = t1.TeamID
            JOIN team_names AS t2 ON m.Team2 = t2.TeamID
            UNION ALL
            SELECT MatchDate, t1.TeamName AS Team1Name, t2.TeamName AS Team2Name,
            m.Team1Goals, m.Team2Goals, m.Team1Goals + m.Team2Goals AS TotalGoals
            FROM default.wwc_matches_2_db AS m
            JOIN team_names AS t1 ON m.Team1 = t1.TeamID
            JOIN team_names AS t2 ON m.Team2 = t2.TeamID
            ORDER BY MatchDate;"