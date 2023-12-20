# ontology_publication_template
[![Check and deploy](https://github.com/materialdigital/ontology_publication_template/actions/workflows/workflow.yaml/badge.svg)](https://github.com/materialdigital/ontology_publication_template/actions/workflows/workflow.yaml)

## Purpose
This repo contains a minimal example of how ontologies could be published using github-pages while maintaining availability of definition files and documentation for older versions.

## Requirements as defined by HAP 4
The requirements are specified in [Technical requirements for ontologies](README.md#technical-requirements-for-ontologies) and [Additional requirements for publishing ontologies](README.md#additional-requirements-for-publishing-ontologies).
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

## Technical requirements for ontologies

### Ontology metadata
| Requirement | Description | Prefered property | Example |
| ----------- | ----------- | ----------------- | ------- |
| Title | Title of the ontology | `dcterms:title` | |
| Author, Creator, Maintainer | Identification of the creator(s) or maintainer(s) of the ontology. Wherever possible use an ORCID | `dcterms:creator` | `<https://orcid.org/0000-0000-0000-0000>` |
| Creation Date | Date of creation of the ontology | `dcterms:created` | |
| Version | Details about the version of the ontology, including updates and revisions. | `owl:versionInfo` **and** `owl:versionIRI` | |
| Ontology Description and Scope | Clear and concise decription of the onotlogy and its scope. | `rdfs:comment` | |
| Project | Identification of the projects creator(s) or maintainer(s) of the ontology. Include this in the rdfs:comment for "Ontology description and scope" | | |
| License | Information about the licensing and usage rights of the ontology. If you have not thought about this before, we recommend to consider CC-BY-4.0 | `dcterms:license` | `<http://creativecommons.org/licenses/by/4.0/>` |
| How to cite | Provide a citation example for the ontology, e.g. a scientific paper you published about your ontology. | `dcterms:bibliographicCitation` | |

### IRIs
| Requirement | Description | Prefered property | Example |
| ----------- | ----------- | ----------------- | ------- |
| Namespace | A **unique** namespace for the ontology to avoid conflicts and ensure clear identification. | | https://w3id.org/pmd/new_ontology/ |
| Dereferenceable IRIs | Internationalized Resource Identifiers (IRIs) should be dereferenciable for easy access and reference, if you have the capabilities to do so. | | |

### IRIs
| Requirement | Description | Prefered property | Example |
| ----------- | ----------- | ----------------- | ------- |
| Labels | Label of the classes and properties | `rdfs:label` or `skos:prefLabel` | |
| Definitions | Clear and concise definitions for all terms, concepts, and relationships within the ontology. | `rdfs:comment` or `skos:description` | |

## Additional requirements for publishing ontologies
### General
| Requirement | Description | Example |
| ----------- | ----------- | ------- |
| Documentation | Comprehensive documentation covering the ontology's purpose, scope, and structure. | |
| Accessibility | Accessable through www, publicly available | https://github.com/materialdigital/ontology_publication_template |
| Findability | Already published via scientific journal or terminology service or ontology repo or similar | |

### Interoperability
| Requirement | Description | Example |
| ----------- | ----------- | ------- |
| Top-Level grounding | To which top-level or mid-level is the ontology based on? | BFO, EMMO, PMDco, etc |
| Concept reuse | From which other ontologies are concepts reused? | QUDT, CHEBI, etc. |
| Format Standards | Serialize the ontology in RDF turtle. | ttl |
| OWL Complexity | Is the ontology OWL-DL conform or does it use other OWL variants | |
