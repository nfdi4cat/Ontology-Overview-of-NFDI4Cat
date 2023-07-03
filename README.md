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
|                | [AFO]                                | [BAO]                               | [BFO]                               | [CAO]                               | [ChEBI]                               | [CHMO]                               | [EDAM]                               | [ENVO]                               | [metadata4Ing]                          | [MOP]                          | [MS]                          | [OBI]                          | [OFM]                          | [OSMO]                          | [PIMS-II]                         | [REX]                        | [RXNO]                        | [SBO]                        | [VIMMP]   |
|:---------------|:-------------------------------------|:------------------------------------|:------------------------------------|:------------------------------------|:--------------------------------------|:-------------------------------------|:-------------------------------------|:-------------------------------------|:----------------------------------------|:-------------------------------|:------------------------------|:-------------------------------|:-------------------------------|:--------------------------------|:----------------------------------|:-----------------------------|:------------------------------|:-----------------------------|:----------|
| [AFO]          | 2876                                 |                                     |                                     |                                     |                                       |                                      |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [BAO]          | [104](/mapping/AFO_BAO.xlsx)         | 7512                                |                                     |                                     |                                       |                                      |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [BFO]          | [36](/mapping/AFO_BFO.xlsx)          | [4](/mapping/BAO_BFO.xlsx)          | 35                                  |                                     |                                       |                                      |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [CAO]          | [121](/mapping/AFO_CAO.xlsx)         | [24](/mapping/BAO_CAO.xlsx)         | [14](/mapping/BFO_CAO.xlsx)         | 445                                 |                                       |                                      |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [ChEBI]        | [58](/mapping/AFO_ChEBI.xlsx)        | [1489](/mapping/BAO_ChEBI.xlsx)     | [1](/mapping/BFO_ChEBI.xlsx)        | [45](/mapping/CAO_ChEBI.xlsx)       | 176873                                |                                      |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [CHMO]         | [249](/mapping/AFO_CHMO.xlsx)        | [37](/mapping/BAO_CHMO.xlsx)        | [12](/mapping/BFO_CHMO.xlsx)        | [69](/mapping/CAO_CHMO.xlsx)        | [23](/mapping/ChEBI_CHMO.xlsx)        | 3101                                 |                                      |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [EDAM]         | [50](/mapping/AFO_EDAM.xlsx)         | [35](/mapping/BAO_EDAM.xlsx)        | [0](/mapping/BFO_EDAM.xlsx)         | [12](/mapping/CAO_EDAM.xlsx)        | [3](/mapping/ChEBI_EDAM.xlsx)         | [9](/mapping/CHMO_EDAM.xlsx)         | 3473                                 |                                      |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [ENVO]         | [207](/mapping/AFO_ENVO.xlsx)        | [192](/mapping/BAO_ENVO.xlsx)       | [26](/mapping/BFO_ENVO.xlsx)        | [78](/mapping/CAO_ENVO.xlsx)        | [938](/mapping/ChEBI_ENVO.xlsx)       | [32](/mapping/CHMO_ENVO.xlsx)        | [9](/mapping/EDAM_ENVO.xlsx)         | 6566                                 |                                         |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [metadata4Ing] | [18](/mapping/AFO_metadata4Ing.xlsx) | [2](/mapping/BAO_metadata4Ing.xlsx) | [3](/mapping/BFO_metadata4Ing.xlsx) | [7](/mapping/CAO_metadata4Ing.xlsx) | [1](/mapping/ChEBI_metadata4Ing.xlsx) | [3](/mapping/CHMO_metadata4Ing.xlsx) | [1](/mapping/EDAM_metadata4Ing.xlsx) | [4](/mapping/ENVO_metadata4Ing.xlsx) | 32                                      |                                |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [MOP]          | [6](/mapping/AFO_MOP.xlsx)           | [6](/mapping/BAO_MOP.xlsx)          | [3](/mapping/BFO_MOP.xlsx)          | [8](/mapping/CAO_MOP.xlsx)          | [58](/mapping/ChEBI_MOP.xlsx)         | [3](/mapping/CHMO_MOP.xlsx)          | [0](/mapping/EDAM_MOP.xlsx)          | [25](/mapping/ENVO_MOP.xlsx)         | [1](/mapping/metadata4Ing_MOP.xlsx)     | 3686                           |                               |                                |                                |                                 |                                   |                              |                               |                              |           |
| [MS]           | [139](/mapping/AFO_MS.xlsx)          | [45](/mapping/BAO_MS.xlsx)          | [0](/mapping/BFO_MS.xlsx)           | [26](/mapping/CAO_MS.xlsx)          | [20](/mapping/ChEBI_MS.xlsx)          | [30](/mapping/CHMO_MS.xlsx)          | [26](/mapping/EDAM_MS.xlsx)          | [32](/mapping/ENVO_MS.xlsx)          | [1](/mapping/metadata4Ing_MS.xlsx)      | [1](/mapping/MOP_MS.xlsx)      | 14989                         |                                |                                |                                 |                                   |                              |                               |                              |           |
| [OBI]          | [204](/mapping/AFO_OBI.xlsx)         | [152](/mapping/BAO_OBI.xlsx)        | [35](/mapping/BFO_OBI.xlsx)         | [73](/mapping/CAO_OBI.xlsx)         | [129](/mapping/ChEBI_OBI.xlsx)        | [78](/mapping/CHMO_OBI.xlsx)         | [32](/mapping/EDAM_OBI.xlsx)         | [182](/mapping/ENVO_OBI.xlsx)        | [4](/mapping/metadata4Ing_OBI.xlsx)     | [6](/mapping/MOP_OBI.xlsx)     | [35](/mapping/MS_OBI.xlsx)    | 4866                           |                                |                                 |                                   |                              |                               |                              |           |
| [OFM]          | [20](/mapping/AFO_OFM.xlsx)          | [2](/mapping/BAO_OFM.xlsx)          | [0](/mapping/BFO_OFM.xlsx)          | [4](/mapping/CAO_OFM.xlsx)          | [0](/mapping/ChEBI_OFM.xlsx)          | [2](/mapping/CHMO_OFM.xlsx)          | [3](/mapping/EDAM_OFM.xlsx)          | [3](/mapping/ENVO_OFM.xlsx)          | [1](/mapping/metadata4Ing_OFM.xlsx)     | [0](/mapping/MOP_OFM.xlsx)     | [0](/mapping/MS_OFM.xlsx)     | [5](/mapping/OBI_OFM.xlsx)     | 109                            |                                 |                                   |                              |                               |                              |           |
| [OSMO]         | [8](/mapping/AFO_OSMO.xlsx)          | [1](/mapping/BAO_OSMO.xlsx)         | [0](/mapping/BFO_OSMO.xlsx)         | [2](/mapping/CAO_OSMO.xlsx)         | [0](/mapping/ChEBI_OSMO.xlsx)         | [0](/mapping/CHMO_OSMO.xlsx)         | [4](/mapping/EDAM_OSMO.xlsx)         | [0](/mapping/ENVO_OSMO.xlsx)         | [1](/mapping/metadata4Ing_OSMO.xlsx)    | [0](/mapping/MOP_OSMO.xlsx)    | [3](/mapping/MS_OSMO.xlsx)    | [2](/mapping/OBI_OSMO.xlsx)    | [2](/mapping/OFM_OSMO.xlsx)    | 173                             |                                   |                              |                               |                              |           |
| [PIMS-II]      | [21](/mapping/AFO_PIMS-II.xlsx)      | [1](/mapping/BAO_PIMS-II.xlsx)      | [2](/mapping/BFO_PIMS-II.xlsx)      | [4](/mapping/CAO_PIMS-II.xlsx)      | [0](/mapping/ChEBI_PIMS-II.xlsx)      | [1](/mapping/CHMO_PIMS-II.xlsx)      | [4](/mapping/EDAM_PIMS-II.xlsx)      | [5](/mapping/ENVO_PIMS-II.xlsx)      | [9](/mapping/metadata4Ing_PIMS-II.xlsx) | [1](/mapping/MOP_PIMS-II.xlsx) | [1](/mapping/MS_PIMS-II.xlsx) | [6](/mapping/OBI_PIMS-II.xlsx) | [0](/mapping/OFM_PIMS-II.xlsx) | [2](/mapping/OSMO_PIMS-II.xlsx) | 135                               |                              |                               |                              |           |
| [REX]          | [9](/mapping/AFO_REX.xlsx)           | [7](/mapping/BAO_REX.xlsx)          | [0](/mapping/BFO_REX.xlsx)          | [2](/mapping/CAO_REX.xlsx)          | [0](/mapping/ChEBI_REX.xlsx)          | [18](/mapping/CHMO_REX.xlsx)         | [0](/mapping/EDAM_REX.xlsx)          | [6](/mapping/ENVO_REX.xlsx)          | [1](/mapping/metadata4Ing_REX.xlsx)     | [23](/mapping/MOP_REX.xlsx)    | [2](/mapping/MS_REX.xlsx)     | [3](/mapping/OBI_REX.xlsx)     | [0](/mapping/OFM_REX.xlsx)     | [0](/mapping/OSMO_REX.xlsx)     | [0](/mapping/PIMS-II_REX.xlsx)    | 552                          |                               |                              |           |
| [RXNO]         | [14](/mapping/AFO_RXNO.xlsx)         | [6](/mapping/BAO_RXNO.xlsx)         | [2](/mapping/BFO_RXNO.xlsx)         | [17](/mapping/CAO_RXNO.xlsx)        | [228](/mapping/ChEBI_RXNO.xlsx)       | [10](/mapping/CHMO_RXNO.xlsx)        | [0](/mapping/EDAM_RXNO.xlsx)         | [94](/mapping/ENVO_RXNO.xlsx)        | [1](/mapping/metadata4Ing_RXNO.xlsx)    | [122](/mapping/MOP_RXNO.xlsx)  | [3](/mapping/MS_RXNO.xlsx)    | [12](/mapping/OBI_RXNO.xlsx)   | [0](/mapping/OFM_RXNO.xlsx)    | [0](/mapping/OSMO_RXNO.xlsx)    | [1](/mapping/PIMS-II_RXNO.xlsx)   | [12](/mapping/REX_RXNO.xlsx) | 1019                          |                              |           |
| [SBO]          | [41](/mapping/AFO_SBO.xlsx)          | [27](/mapping/BAO_SBO.xlsx)         | [2](/mapping/BFO_SBO.xlsx)          | [7](/mapping/CAO_SBO.xlsx)          | [13](/mapping/ChEBI_SBO.xlsx)         | [3](/mapping/CHMO_SBO.xlsx)          | [7](/mapping/EDAM_SBO.xlsx)          | [16](/mapping/ENVO_SBO.xlsx)         | [1](/mapping/metadata4Ing_SBO.xlsx)     | [19](/mapping/MOP_SBO.xlsx)    | [9](/mapping/MS_SBO.xlsx)     | [13](/mapping/OBI_SBO.xlsx)    | [3](/mapping/OFM_SBO.xlsx)     | [1](/mapping/OSMO_SBO.xlsx)     | [2](/mapping/PIMS-II_SBO.xlsx)    | [11](/mapping/REX_SBO.xlsx)  | [7](/mapping/RXNO_SBO.xlsx)   | 694                          |           |
| [VIMMP]        | [83](/mapping/AFO_VIMMP.xlsx)        | [12](/mapping/BAO_VIMMP.xlsx)       | [3](/mapping/BFO_VIMMP.xlsx)        | [19](/mapping/CAO_VIMMP.xlsx)       | [3](/mapping/ChEBI_VIMMP.xlsx)        | [5](/mapping/CHMO_VIMMP.xlsx)        | [15](/mapping/EDAM_VIMMP.xlsx)       | [21](/mapping/ENVO_VIMMP.xlsx)       | [6](/mapping/metadata4Ing_VIMMP.xlsx)   | [1](/mapping/MOP_VIMMP.xlsx)   | [12](/mapping/MS_VIMMP.xlsx)  | [24](/mapping/OBI_VIMMP.xlsx)  | [8](/mapping/OFM_VIMMP.xlsx)   | [172](/mapping/OSMO_VIMMP.xlsx) | [18](/mapping/PIMS-II_VIMMP.xlsx) | [0](/mapping/REX_VIMMP.xlsx) | [2](/mapping/RXNO_VIMMP.xlsx) | [9](/mapping/SBO_VIMMP.xlsx) | 1082      |

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
