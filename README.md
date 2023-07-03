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
|              |  AFO |  BAO | BFO | CAO |  ChEBI | CHMO | EDAM | ENVO | metadata4Ing |  MOP |   MS  |  OBI | OFM | OSMO | PIMS-II | REX | RXNO | SBO | VIMMP |
|--------------|:----:|:----:|:---:|:---:|:------:|:----:|:----:|:----:|:------------:|:----:|:-----:|:----:|:---:|:----:|:-------:|:---:|:----:|:---:|:-----:|
|      AFO     | 2876 |      |     |     |        |      |      |      |              |      |       |      |     |      |         |     |      |     |       |
|      BAO     | [104](/mapping/BAO_AFO.xlsx)  | 7512 |     |     |        |      |      |      |              |      |       |      |     |      |         |     |      |     |       |
|      BFO     | 36   | 4    | 35  |     |        |      |      |      |              |      |       |      |     |      |         |     |      |     |       |
|      CAO     | 121  | 24   | 14  | 445 |        |      |      |      |              |      |       |      |     |      |         |     |      |     |       |
|     ChEBI    | 58   | 1489 | 1   | 45  | 176873 |      |      |      |              |      |       |      |     |      |         |     |      |     |       |
|     CHMO     | 249  | 37   | 12  | 69  | 23     | 3101 |      |      |              |      |       |      |     |      |         |     |      |     |       |
|     EDAM     | 50   | 35   | 0   | 12  | 3      | 9    | 3473 |      |              |      |       |      |     |      |         |     |      |     |       |
|     ENVO     | 207  | 192  | 26  | 78  | 938    | 32   | 9    | 6566 |              |      |       |      |     |      |         |     |      |     |       |
| metadata4Ing | 18   | 2    | 3   | 7   | 1      | 3    | 1    | 4    | 32           |      |       |      |     |      |         |     |      |     |       |
|      MOP     | 6    | 6    | 3   | 8   | 58     | 3    | 0    | 25   | 1            | 3686 |       |      |     |      |         |     |      |     |       |
|      MS      | 139  | 45   | 0   | 26  | 20     | 30   | 26   | 32   | 1            | 1    | 14989 |      |     |      |         |     |      |     |       |
|      OBI     | 204  | 152  | 35  | 73  | 129    | 78   | 32   | 182  | 4            | 6    | 35    | 4866 |     |      |         |     |      |     |       |
|      OFM     | 20   | 2    | 0   | 4   | 0      | 2    | 3    | 3    | 1            | 0    | 0     | 5    | 109 |      |         |     |      |     |       |
|     OSMO     | 8    | 1    | 0   | 2   | 0      | 0    | 4    | 0    | 1            | 0    | 3     | 2    | 2   | 173  |         |     |      |     |       |
|    PIMS-II   | 21   | 1    | 2   | 4   | 0      | 1    | 4    | 5    | 9            | 1    | 1     | 6    | 0   | 2    | 135     |     |      |     |       |
|      REX     | 9    | 7    | 0   | 2   | 0      | 18   | 0    | 6    | 1            | 23   | 2     | 3    | 0   | 0    | 0       | 552 |      |     |       |
|     RXNO     | 14   | 6    | 2   | 17  | 228    | 10   | 0    | 94   | 1            | 122  | 3     | 12   | 0   | 0    | 1       | 12  | 1019 |     |       |
|      SBO     | 41   | 27   | 2   | 7   | 13     | 3    | 7    | 16   | 1            | 19   | 9     | 13   | 3   | 1    | 2       | 11  | 7    | 694 |       |
|     VIMMP    | 83   | 12   | 3   | 19  | 3      | 5    | 15   | 21   | 6            | 1    | 12    | 24   | 8   | 172  | 18      | 0   | 2    | 9   | 1082  |


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
