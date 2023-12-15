# ontology_publication_template
[![Check and deploy](https://github.com/materialdigital/ontology_publication_template/actions/workflows/workflow.yaml/badge.svg)](https://github.com/materialdigital/ontology_publication_template/actions/workflows/workflow.yaml)

## Purpose
This repo contains a minimal example of how ontologies could be published using github-pages while maintaining availability of definition files and documentation for older versions.

## Requirements as defined by HAP 4
The requirements are specified in **TODO: Add link to requirements table**
The file [ontology.ttl](ontology.ttl) is a turtle serialization of an example ontology that conforms to the requirements given in the table.

## Key components
### [ontology.ttl](ontology.ttl)
The definition file for an ontology, which is actively developed and thus changes its version number more or less frequently.

### [.github/workflows/workflow.yaml](.github/workflows/workflow.yaml)
A workflow definition that does the following steps on push to main and develop:

1) Build the html documentation and the ontologies alternate serializations for the current version
2) add the current versions documentation and serializations to gh-pages, maintaining other versions and replacing the same (current) version

### [.htaccess_example](.htaccess_example)
A example .htaccess file that takes care of finding the correct version and the latest version. Currently this file has to be edited for each new version (unfortunately gh-pages does not allow symlinks). It's meant to be used at some perma-id provider e.g. at [w3id.org](https://w3id.org).

## Future work

- The github release tool is not yet part of the deploy action. This might be desirable in the future.
- A way for automatedly delivering the latest version without changing the .htaccess-file would be nice. One could simply store the versions folder in gh-pages twice (also using the name "latest").
