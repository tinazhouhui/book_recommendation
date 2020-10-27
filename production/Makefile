root_project = ..

BG =\n\033[0;36m-- # Beginning
NC =\033[0m\n# No Color

.PHONY: pip
pip:
	@(printf "${BG}Installing PIP dependencies${NC}")
		pip3 install -U pip setuptools
		cd $(root_project) && pip3 install -r requirements.txt

.PHONY: qa
qa:
	@(printf "${BG}Prepare log directory${NC}")
		mkdir -p $(root_project)/log

	@(printf "${BG}Running tests${NC}")
		cd $(root_project) && python3 -m unittest tests/**/*.py
