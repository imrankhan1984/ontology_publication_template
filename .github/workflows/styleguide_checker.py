import rdflib
import argparse
import json
import re
import numpy as np

OBO = rdflib.Namespace("http://purl.obolibrary.org/obo/")

def getSubjName(subject):
    return str(subject).split('/')[-1].split('#')[-1]

def isUpperCamelCase(s):
    return re.match(r"^([A-Z][a-z]+)*$", s) is not None

def isLowerCamelCase(s):
    return re.match(r"^([a-z]+)([A-Z][a-z]+)*$", s) is not None

def isCapitalized(s):
    return re.match(r"^([A-Z][a-z]+\s?)*$", s) is not None

def hasLanguage(lit_list, languages=None):
    if languages is None:
        languages = ['en']
    langlist = [lit.language for lit in lit_list]
    return all([language in langlist for language in languages]) and not None in langlist

def hasCurationStatus(subject, graph):
    return len(list(graph.objects(subject, OBO.IAO_0000114))) == 1

def hasValidTermEditor(subject, graph):
    termEditor_list = list(graph.objects(subject, OBO.IAO_0000117))
    return all([re.match(r"^PERSON:(.*)$", str(termEditor)) is not None for termEditor in termEditor_list]) and len(termEditor_list) > 0

def checkCommon(subject, graph):
    labels_list = list(graph.objects(subject, rdflib.RDFS.label))
    skosdef_list = list(graph.objects(subject, rdflib.SKOS.definition))
    return {
        'rdfsLabelExists': len(labels_list) > 0,
        'rdfsLabelsLang': hasLanguage(labels_list),
        'rdfsLabelsStyle': all([isCapitalized(label) for label in labels_list]),
        'skosDefinitionExists': len(skosdef_list) > 0,
        'skosDefinitionsLang': hasLanguage(skosdef_list),
        'oboCurationStatusExists': hasCurationStatus(subject, graph),
        'oboTermEditorExistsValid': hasValidTermEditor(subject, graph)
    }

def checkClass(subject, graph):
    commonChecks = checkCommon(subject, graph)
    classSpecificChecks = {
        'classNameStyle': isUpperCamelCase(getSubjName(subject)),
    }
    return {**commonChecks, **classSpecificChecks}

def checkObjectProperty(subject, graph):
    commonChecks = checkCommon(subject, graph)
    objectPropertySpecificChecks = {
        'objectPropertyNameStyle': isLowerCamelCase(getSubjName(subject))
    }
    return {**commonChecks, **objectPropertySpecificChecks}

def checkClasses(graph):
    return {str(s): checkClass(s, graph) for s in graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.Class)}

def checkObjectProperties(graph):
    return {str(s): checkObjectProperty(s, graph) for s in graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.ObjectProperty)}

def checkGraph(graph):
    return {
        'classes': checkClasses(graph),
        'objectProperties': checkObjectProperties(graph)
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ontology_file', type=str)
    parser.add_argument('-r', '--report_file', type=str, default='styleguide_report.json')
    parser.add_argument('-b', '--create_badge', action='store_true')
    parser.add_argument('--badge_cmdfile', type=str, default='styleguide_badge.sh')
    parser.add_argument('--badge_svgfile', type=str, default='styleguide_badge.svg')
    args = parser.parse_args()

    g = rdflib.Graph()
    g.parse(args.ontology_file)

    report = checkGraph(g)

    number_classes = len(report['classes'].keys())
    number_valid_classes = [all(list(cl_res.values())) for _, cl_res in report['classes'].items()].count(True)
    number_object_properties = len(report['objectProperties'].keys())
    number_valid_object_properties = [all(list(cl_res.values())) for _, cl_res in report['objectProperties'].items()].count(True)
    number_definitions = number_classes + number_object_properties
    number_valid_definitions = number_valid_classes + number_valid_object_properties

    print('=============== Style guide compliance report ===============')
    print(f'Classes: {number_valid_classes} of {number_classes} classes comply with the style guide')
    print(f'Object properties: {number_valid_object_properties} of {number_object_properties} object properties comply with the style guide')
    print(f'Overall Definitions: {number_valid_definitions} of {number_definitions} definitions comply with the style guide')
    print('=============================================================')

    frac_valid = number_valid_definitions/number_definitions
    def badge_color(frac):
        if frac > 1.0 or frac < 0.0:
            raise ValueError('frac_valid must be between 0.0 and 1.0')
        else:
            for frac_thr, b_color in zip(np.flip(np.linspace(0.0, 1.0, 6, endpoint=False)), ['lightgreen', 'green', 'yellow', 'yellowgreen', 'orange', 'red']):
                if frac >= frac_thr:
                    return b_color

    if args.create_badge:
        with open(args.badge_cmdfile, 'w', encoding='utf8') as f:
            f.write(f'badge "Styleguide compliance" "{frac_valid*100.0:.1f}%" :{badge_color(frac_valid)} > {args.badge_svgfile}')

    with open(args.report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
