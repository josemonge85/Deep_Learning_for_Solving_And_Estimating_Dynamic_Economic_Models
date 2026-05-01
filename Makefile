# Convenience targets for the Deep Learning for Economics and Finance course.
#
# Usage:
#   make validate          # run all validation scripts; fail on first failure
#   make build-script      # build lecture_script/lecture_script.pdf
#   make build-slides      # build every lecture's slide PDF
#   make smoke             # placeholder for the smoke-test harness
#   make clean             # remove LaTeX intermediates

.PHONY: validate validate-headers validate-paths validate-landing validate-content validate-english \
        validate-readings build-script build-slides smoke clean help

PYTHON ?= python3

help:
	@echo "Targets:"
	@echo "  validate         Run the full validation suite (6 checks)."
	@echo "  build-script     Compile lecture_script.pdf."
	@echo "  build-slides     Compile every lecture and toolkit slide deck."
	@echo "  smoke            Run the smoke-test harness (placeholder)."
	@echo "  clean            Remove LaTeX intermediate files."

validate: validate-headers validate-paths validate-landing validate-content validate-english validate-readings
	@echo "All validators passed."

validate-headers:
	@$(PYTHON) scripts/validate_headers.py

validate-paths:
	@$(PYTHON) scripts/validate_no_private_paths.py

validate-landing:
	@$(PYTHON) scripts/validate_landing_page_assets.py

validate-content:
	@$(PYTHON) scripts/validate_no_content_loss.py

validate-english:
	@$(PYTHON) scripts/check_american_english.py

validate-readings:
	@$(PYTHON) scripts/validate_readings.py

build-script:
	@bash scripts/build_script.sh

build-slides:
	@bash scripts/build_slides.sh

smoke:
	@$(PYTHON) scripts/run_all_smoke_tests.py

clean:
	@find lectures toolkit lecture_script -type f \( \
	    -name '*.aux' -o -name '*.log' -o -name '*.nav' -o -name '*.out' -o \
	    -name '*.snm' -o -name '*.toc' -o -name '*.vrb' -o -name '*.synctex.gz' -o \
	    -name '*.bbl' -o -name '*.blg' -o -name '*.fls' -o -name '*.fdb_latexmk' \
	  \) -delete 2>/dev/null || true
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name '.ipynb_checkpoints' -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned."
