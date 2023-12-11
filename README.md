# ontology_publication_template
### Main branch status
[![OOPS!](https://raw.githubusercontent.com/materialdigital/ontology_publication_template/gh-pages/main_oops_badge.svg)](https://oops.linkeddata.es/)
[![Styleguide check](https://raw.githubusercontent.com/materialdigital/ontology_publication_template/gh-pages/main_styleguide_badge.svg)]()
### Dev branch status
[![OOPS!](https://raw.githubusercontent.com/materialdigital/ontology_publication_template/gh-pages/develop_oops_badge.svg)](https://oops.linkeddata.es/)
[![Styleguide check](https://raw.githubusercontent.com/materialdigital/ontology_publication_template/gh-pages/develop_styleguide_badge.svg)]()

## Purpose
This repo contains a minimal example of how ontologies could be published using github-pages while maintaining availability of definition files and documentation for older versions.

## Key components
### [ontology.ttl](ontology.ttl)
The definition file for an ontology, which is actively developed and thus changes its version number more or less frequently.

### [.github/workflows/workflow.yaml](.github/workflows/workflow.yaml)
A workflow definition that does the following steps on push to main and develop:

On main and develop:
1) Check the compliance with PMD core ontology guidelines [https://github.com/materialdigital/core-ontology/blob/develop-3.0.0/modules/README.md](https://github.com/materialdigital/core-ontology/blob/develop-3.0.0/modules/README.md)
2) Run the [OOPS! OntOlogy Pitfall Scanner!](https://oops.linkeddata.es/) [[1]](#1)

And further on main:

3) Build the html documentation and the ontologies alternate serializations for the current version
4) add the current versions documentation and serializations to gh-pages, maintaining other versions and replacing the same (current) version

### [.htaccess_example](.htaccess_example)
A example .htaccess file that takes care of finding the correct version and the latest version. Currently this file has to be edited for each new version (unfortunately gh-pages does not allow symlinks). It's meant to be used at some perma-id provider e.g. at [w3id.org](https://w3id.org).

## Future work

- The github release tool is not yet part of the deploy action. This might be desirable in the future.
- A way for automatedly delivering the latest version without changing the .htaccess-file would be nice. One could simply store the versions folder in gh-pages twice (also using the name "latest").

## References
<a id="1">[1]</a> 
Poveda-Villalón, María and Gómez-Pérez, Asunción and Suárez-Figueroa, Mari Carmen (2014). 
OOPS! (OntOlogy Pitfall Scanner!): An On-line Tool for Ontology Evaluation. 
International Journal on Semantic Web and Information Systems (IJSWIS), 10(2), 7-31.
