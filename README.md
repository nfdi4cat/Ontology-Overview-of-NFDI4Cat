[<img src="./logo_NFDI4Cat.jpg" width="300" />](https://nfdi4cat.org/)
# Ontology World Map of NFDI4Cat
Repository which lists ontologies relevant for catalysis research.

For remarks, additions, or general questions either use the issues or contact the responsible person (see below).
For contributions please download the [markdown file](./General_Template.md) called [General Template] and contact us either via mail, issue or pull request with your updated markdown file. 
A condensed view on the data provided in the markdown-files is given in [master_table](./master_table/Possible_Template_TF_OntoWorldMap_2023-03-28_10-52.xlsx).
The respective markdown files for each ontology listed in the table below are located in [ontology_metadata](./ontology_metadata).
In the subdirectory [json](./json), the information contained for each ontology is stored in json-format for an ease in access of the data presented in markdown.

Contact: <a href="mailto:alexander.behr@tu-dortmund.de?subject=Contact for Software Collection from NFDI4Cat">alexander.behr@tu-dortmund.de</a>

## Ontology Metadata files
These are the ontologies and links to the ontology markdown files, NFDI4Cat deems as relevant:

| Link to Markdown | Ontology Name |
 |:---:|:---|
| [AFO] |Allotrope Foundation Ontology |
| [BAO] |BioAssay Ontology |
| [BFO] |Basic Formal Ontology |
| [CAO] |Chemical Analysis Ontology |
| [ChEBI] |Chemical Entities of Biological Interest |
| [CHEMINF] |Chemical Information Ontology |
| [CHMO] |Chemical Methods Ontology |
| [CIF] |Crystallographic Information Framework Ontology |
| [EDAM] |EDAM - Bioscientific data analysis ontology |
| [EMMO] |Elementary Multiperspective Material Ontology |
| [ENVO] |Environmental Ontology |
| [M3] |Machine to Machine Measurements Ontology |
| [metadata4ing] |Metadata4Ing: An ontology for describing the generation of research data within a scientific activity. |
| [MOP] |Molecular Process Ontology |
| [MS] |Mass Spectrometry Ontology |
| [OBI] |Ontology for Biomedical Investigations |
| [OM] |Ontology of units of Measure |
| [OntoCAPE] |Ontology for the domain of Computer Aided Process Engineering |
| [OSMO] |Ontology for Simulation, Modelling, and Optimization |
| [REX] |Physico-chemical process |
| [RXNO] |RXNO: name reaction ontology |
| [SBO] |Systems Biology Ontology |
| [VIMMP] |Virtual Materials Marketplace Ontology |

## Map of Catalysis Research Domains
The ontologies in this table contain the respective domain of knowledge or are narrower related to them.
|    | Biocatalysis   | Heterogenous catalysis   | Homogenous catalysis   | Chemical Substance Modeling   | Material Modeling   | Process Modeling   | Synthesis Data   | Operando Data   | Performance Data   | Characterisation Data   | Heat, Transport and Kinetic Data   | Process Design, Energy and Cost Data   | Top Level Ontology   |
|---:|:---------------|:-------------------------|:-----------------------|:------------------------------|:--------------------|:-------------------|:-----------------|:----------------|:-------------------|:------------------------|:-----------------------------------|:---------------------------------------|:---------------------|
|  0 | [EDAM]         | [MOP]                    | [MOP]                  | [AFO]                         | [AFO]               | [AFO]              |                  | [OSMO]          | [CHMO]             | [AFO]                   | [OntoCAPE]                         | [OntoCAPE]                             | [AFO]                |
|  1 | [SBO]          | [REX]                    | [REX]                  | [BAO]                         | [ChEBI]             | [BAO]              |                  |                 | [EDAM]             | [BAO]                   |                                    |                                        | [BFO]                |
|  2 |                | [RXNO]                   | [RXNO]                 | [CAO]                         | [CHEMINF]           | [EMMO]             |                  |                 | [OSMO]             | [CHEMINF]               |                                    |                                        | [CAO]                |
|  3 |                |                          |                        | [ChEBI]                       | [EMMO]              | [metadata4Ing]     |                  |                 |                    | [CHMO]                  |                                    |                                        | [ChEBI]              |
|  4 |                |                          |                        | [MOP]                         | [OSMO]              | [MOP]              |                  |                 |                    | [EDAM]                  |                                    |                                        | [CHEMINF]            |
|  5 |                |                          |                        | [OBI]                         | [SBO]               | [OBI]              |                  |                 |                    | [MS]                    |                                    |                                        | [CHMO]               |
|  6 |                |                          |                        | [OntoCAPE]                    |                     | [OntoCAPE]         |                  |                 |                    |                         |                                    |                                        | [CIF]                |
|  7 |                |                          |                        | [RXNO]                        |                     | [OSMO]             |                  |                 |                    |                         |                                    |                                        | [EMMO]               |
|  8 |                |                          |                        | [SBO]                         |                     | [RXNO]             |                  |                 |                    |                         |                                    |                                        | [ENVO]               |
|  9 |                |                          |                        |                               |                     | [SBO]              |                  |                 |                    |                         |                                    |                                        | [MOP]                |
| 10 |                |                          |                        |                               |                     | [VIMMP]            |                  |                 |                    |                         |                                    |                                        | [MS]                 |
| 11 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [OBI]                |
| 12 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [OntoCAPE]           |
| 13 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [OSMO]               |
| 14 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [RXNO]               |
| 15 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [SBO]                |
| 16 |                |                          |                        |                               |                     |                    |                  |                 |                    |                         |                                    |                                        | [VIMMP]              |

## Mappings
Here, you can see a mapping that lists the amount of common ontology classes for each ontology, focusing on IRI, label, prefLabel, altLabel and name of the classes.

|                | [AFO]                              | [BAO]                             | [BFO]                             | [CAO]                             | [ChEBI]                             | [CHMO]                             | [EDAM]                             | [ENVO]                             | [metadata4Ing]                        | [MOP]                        | [MS]                        | [OBI]                        | [OFM]                        | [OSMO]                        | [PIMS-II]                       | [REX]                      | [RXNO]                      | [SBO]                      | [VIMMP]   |
|:---------------|:-----------------------------------|:----------------------------------|:----------------------------------|:----------------------------------|:------------------------------------|:-----------------------------------|:-----------------------------------|:-----------------------------------|:--------------------------------------|:-----------------------------|:----------------------------|:-----------------------------|:-----------------------------|:------------------------------|:--------------------------------|:---------------------------|:----------------------------|:---------------------------|:----------|
| [AFO]          | 2876                               |                                   |                                   |                                   |                                     |                                    |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [BAO]          | [104](/mapping/AFO_BAO.md)         | 7512                              |                                   |                                   |                                     |                                    |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [BFO]          | [36](/mapping/AFO_BFO.md)          | [4](/mapping/BAO_BFO.md)          | 35                                |                                   |                                     |                                    |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [CAO]          | [121](/mapping/AFO_CAO.md)         | [24](/mapping/BAO_CAO.md)         | [14](/mapping/BFO_CAO.md)         | 445                               |                                     |                                    |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [ChEBI]        | [58](/mapping/AFO_ChEBI.md)        | [1489](/mapping/BAO_ChEBI.md)     | [1](/mapping/BFO_ChEBI.md)        | [45](/mapping/CAO_ChEBI.md)       | 176873                              |                                    |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [CHMO]         | [249](/mapping/AFO_CHMO.md)        | [37](/mapping/BAO_CHMO.md)        | [12](/mapping/BFO_CHMO.md)        | [69](/mapping/CAO_CHMO.md)        | [23](/mapping/ChEBI_CHMO.md)        | 3101                               |                                    |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [EDAM]         | [50](/mapping/AFO_EDAM.md)         | [35](/mapping/BAO_EDAM.md)        | [0](/mapping/BFO_EDAM.md)         | [12](/mapping/CAO_EDAM.md)        | [3](/mapping/ChEBI_EDAM.md)         | [9](/mapping/CHMO_EDAM.md)         | 3473                               |                                    |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [ENVO]         | [207](/mapping/AFO_ENVO.md)        | [192](/mapping/BAO_ENVO.md)       | [26](/mapping/BFO_ENVO.md)        | [78](/mapping/CAO_ENVO.md)        | [938](/mapping/ChEBI_ENVO.md)       | [32](/mapping/CHMO_ENVO.md)        | [9](/mapping/EDAM_ENVO.md)         | 6566                               |                                       |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [metadata4Ing] | [18](/mapping/AFO_metadata4Ing.md) | [2](/mapping/BAO_metadata4Ing.md) | [3](/mapping/BFO_metadata4Ing.md) | [7](/mapping/CAO_metadata4Ing.md) | [1](/mapping/ChEBI_metadata4Ing.md) | [3](/mapping/CHMO_metadata4Ing.md) | [1](/mapping/EDAM_metadata4Ing.md) | [4](/mapping/ENVO_metadata4Ing.md) | 32                                    |                              |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [MOP]          | [6](/mapping/AFO_MOP.md)           | [6](/mapping/BAO_MOP.md)          | [3](/mapping/BFO_MOP.md)          | [8](/mapping/CAO_MOP.md)          | [58](/mapping/ChEBI_MOP.md)         | [3](/mapping/CHMO_MOP.md)          | [0](/mapping/EDAM_MOP.md)          | [25](/mapping/ENVO_MOP.md)         | [1](/mapping/metadata4Ing_MOP.md)     | 3686                         |                             |                              |                              |                               |                                 |                            |                             |                            |           |
| [MS]           | [139](/mapping/AFO_MS.md)          | [45](/mapping/BAO_MS.md)          | [0](/mapping/BFO_MS.md)           | [26](/mapping/CAO_MS.md)          | [20](/mapping/ChEBI_MS.md)          | [30](/mapping/CHMO_MS.md)          | [26](/mapping/EDAM_MS.md)          | [32](/mapping/ENVO_MS.md)          | [1](/mapping/metadata4Ing_MS.md)      | [1](/mapping/MOP_MS.md)      | 14989                       |                              |                              |                               |                                 |                            |                             |                            |           |
| [OBI]          | [204](/mapping/AFO_OBI.md)         | [152](/mapping/BAO_OBI.md)        | [35](/mapping/BFO_OBI.md)         | [73](/mapping/CAO_OBI.md)         | [129](/mapping/ChEBI_OBI.md)        | [78](/mapping/CHMO_OBI.md)         | [32](/mapping/EDAM_OBI.md)         | [182](/mapping/ENVO_OBI.md)        | [4](/mapping/metadata4Ing_OBI.md)     | [6](/mapping/MOP_OBI.md)     | [35](/mapping/MS_OBI.md)    | 4866                         |                              |                               |                                 |                            |                             |                            |           |
| [OFM]          | [20](/mapping/AFO_OFM.md)          | [2](/mapping/BAO_OFM.md)          | [0](/mapping/BFO_OFM.md)          | [4](/mapping/CAO_OFM.md)          | [0](/mapping/ChEBI_OFM.md)          | [2](/mapping/CHMO_OFM.md)          | [3](/mapping/EDAM_OFM.md)          | [3](/mapping/ENVO_OFM.md)          | [1](/mapping/metadata4Ing_OFM.md)     | [0](/mapping/MOP_OFM.md)     | [0](/mapping/MS_OFM.md)     | [5](/mapping/OBI_OFM.md)     | 109                          |                               |                                 |                            |                             |                            |           |
| [OSMO]         | [8](/mapping/AFO_OSMO.md)          | [1](/mapping/BAO_OSMO.md)         | [0](/mapping/BFO_OSMO.md)         | [2](/mapping/CAO_OSMO.md)         | [0](/mapping/ChEBI_OSMO.md)         | [0](/mapping/CHMO_OSMO.md)         | [4](/mapping/EDAM_OSMO.md)         | [0](/mapping/ENVO_OSMO.md)         | [1](/mapping/metadata4Ing_OSMO.md)    | [0](/mapping/MOP_OSMO.md)    | [3](/mapping/MS_OSMO.md)    | [2](/mapping/OBI_OSMO.md)    | [2](/mapping/OFM_OSMO.md)    | 173                           |                                 |                            |                             |                            |           |
| [PIMS-II]      | [21](/mapping/AFO_PIMS-II.md)      | [1](/mapping/BAO_PIMS-II.md)      | [2](/mapping/BFO_PIMS-II.md)      | [4](/mapping/CAO_PIMS-II.md)      | [0](/mapping/ChEBI_PIMS-II.md)      | [1](/mapping/CHMO_PIMS-II.md)      | [4](/mapping/EDAM_PIMS-II.md)      | [5](/mapping/ENVO_PIMS-II.md)      | [9](/mapping/metadata4Ing_PIMS-II.md) | [1](/mapping/MOP_PIMS-II.md) | [1](/mapping/MS_PIMS-II.md) | [6](/mapping/OBI_PIMS-II.md) | [0](/mapping/OFM_PIMS-II.md) | [2](/mapping/OSMO_PIMS-II.md) | 135                             |                            |                             |                            |           |
| [REX]          | [9](/mapping/AFO_REX.md)           | [7](/mapping/BAO_REX.md)          | [0](/mapping/BFO_REX.md)          | [2](/mapping/CAO_REX.md)          | [0](/mapping/ChEBI_REX.md)          | [18](/mapping/CHMO_REX.md)         | [0](/mapping/EDAM_REX.md)          | [6](/mapping/ENVO_REX.md)          | [1](/mapping/metadata4Ing_REX.md)     | [23](/mapping/MOP_REX.md)    | [2](/mapping/MS_REX.md)     | [3](/mapping/OBI_REX.md)     | [0](/mapping/OFM_REX.md)     | [0](/mapping/OSMO_REX.md)     | [0](/mapping/PIMS-II_REX.md)    | 552                        |                             |                            |           |
| [RXNO]         | [14](/mapping/AFO_RXNO.md)         | [6](/mapping/BAO_RXNO.md)         | [2](/mapping/BFO_RXNO.md)         | [17](/mapping/CAO_RXNO.md)        | [228](/mapping/ChEBI_RXNO.md)       | [10](/mapping/CHMO_RXNO.md)        | [0](/mapping/EDAM_RXNO.md)         | [94](/mapping/ENVO_RXNO.md)        | [1](/mapping/metadata4Ing_RXNO.md)    | [122](/mapping/MOP_RXNO.md)  | [3](/mapping/MS_RXNO.md)    | [12](/mapping/OBI_RXNO.md)   | [0](/mapping/OFM_RXNO.md)    | [0](/mapping/OSMO_RXNO.md)    | [1](/mapping/PIMS-II_RXNO.md)   | [12](/mapping/REX_RXNO.md) | 1019                        |                            |           |
| [SBO]          | [41](/mapping/AFO_SBO.md)          | [27](/mapping/BAO_SBO.md)         | [2](/mapping/BFO_SBO.md)          | [7](/mapping/CAO_SBO.md)          | [13](/mapping/ChEBI_SBO.md)         | [3](/mapping/CHMO_SBO.md)          | [7](/mapping/EDAM_SBO.md)          | [16](/mapping/ENVO_SBO.md)         | [1](/mapping/metadata4Ing_SBO.md)     | [19](/mapping/MOP_SBO.md)    | [9](/mapping/MS_SBO.md)     | [13](/mapping/OBI_SBO.md)    | [3](/mapping/OFM_SBO.md)     | [1](/mapping/OSMO_SBO.md)     | [2](/mapping/PIMS-II_SBO.md)    | [11](/mapping/REX_SBO.md)  | [7](/mapping/RXNO_SBO.md)   | 694                        |           |
| [VIMMP]        | [83](/mapping/AFO_VIMMP.md)        | [12](/mapping/BAO_VIMMP.md)       | [3](/mapping/BFO_VIMMP.md)        | [19](/mapping/CAO_VIMMP.md)       | [3](/mapping/ChEBI_VIMMP.md)        | [5](/mapping/CHMO_VIMMP.md)        | [15](/mapping/EDAM_VIMMP.md)       | [21](/mapping/ENVO_VIMMP.md)       | [6](/mapping/metadata4Ing_VIMMP.md)   | [1](/mapping/MOP_VIMMP.md)   | [12](/mapping/MS_VIMMP.md)  | [24](/mapping/OBI_VIMMP.md)  | [8](/mapping/OFM_VIMMP.md)   | [172](/mapping/OSMO_VIMMP.md) | [18](/mapping/PIMS-II_VIMMP.md) | [0](/mapping/REX_VIMMP.md) | [2](/mapping/RXNO_VIMMP.md) | [9](/mapping/SBO_VIMMP.md) | 1082      |

## Ontologies considered in NFDI4Cat
| Ontology Name | Considered in NFDI4Cat? |
|:---------------:|:-------------------------:|
| [AFO]           | yes                       |
| [BAO]           | yes                        |
| [BFO]           | yes                       |
| [CAO]           | yes                       |
| [ChEBI]         | yes                       |
| [CHEMINF]       | yes                       |
| [CHMO]          | yes                       |
| [CIF]  		  | yes        					|                
| [DOLCE]         | no                       |
| [EDAM]          | yes                        |
| [EMMO]          | yes                       |
| [ENVO]          | yes                       |
| [ISO 15926]     | no                       |
| [ISO 15926-14]  | no                       |
| [M3]            | yes                        |
| [MOP]           | yes						|
| [MS]            | yes                        |
| [metadata4ing]      | yes                        |
| [OBI] | yes |
| [OFM]           | no                        |
| [OM]            | yes                       |
| [OntoCAPE]      | yes                       |
| [OntoCompChem]  | no                       |
| [OntoKin]       | no                       |
| [OSMO]          | yes                       |
| [PIMS-II]       | no                        |
| [REX]           | yes                       |
| [RXNO]          | yes                        |
| [SBO]           | yes                       |
| [VIMMP]         | yes                       |


[AFO]: ./ontology_metadata/AFO.md
[BAO]: ./ontology_metadata/BAO.md
[BFO]: ./ontology_metadata/BFO.md
[CAO]: ./ontology_metadata/CAO.md
[ChEBI]: ./ontology_metadata/ChEBI.md
[CHEMINF]: ./ontology_metadata/CHEMINF.md
[CHMO]: ./ontology_metadata/CHMO.md
[CIF]: ./ontology_metadata/CIF.md
[DOLCE]: http://www.loa.istc.cnr.it/dolce/overview.html
[EDAM]: ./ontology_metadata/EDAM.md
[EMMO]: ./ontology_metadata/EMMO.md
[ENVO]: ./ontology_metadata/ENVO.md
[ISO 15926]: https://en.wikipedia.org/wiki/ISO_15926
[ISO 15926-14]: https://en.wikipedia.org/wiki/ISO_15926
[M3]: ./ontology_metadata/M3.md
[metadata4ing]: ./ontology_metadata/metadata4ing.md
[MOP]: ./ontology_metadata/MOP.md
[MS]: ./ontology_metadata/MS.md
[OBI]: ./ontology_metadata/OBI.md
[OFM]: ./ontology_metadata/OFM.md
[OM]: ./ontology_metadata/OM.md
[OntoCAPE]: ./ontology_metadata/OntoCAPE.md
[OntoCompChem]: http://www.theworldavatar.com/ontology/ontocompchem/ontocompchem.owl
[OntoKin]: https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00960
[OSMO]: ./ontology_metadata/OSMO.md
[PIMS-II]: ./ontology_metadata/PIMS-II.md
[REX]: ./ontology_metadata/REX.md
[RXNO]: ./ontology_metadata/RXNO.md
[SBO]: ./ontology_metadata/SBO.md
[VIMMP]: ./ontology_metadata/VIMMP.md



[General Template]: ./General_Template.md
