# BibTeX and MS Office Bibliography XML Mapping

This reference defines practical mapping rules for exporting bibliography data to Microsoft Word bibliography XML while preserving ISO 690:2022 normalization decisions.

## Source Reference
- JabRef MS Office bibliography mapping: https://docs.jabref.org/advanced/knowledge/msofficebibfieldmapping

## Entry Type Mapping
| BibTeX or BibLaTeX | XML SourceType |
| :--- | :--- |
| book | Book |
| inbook | BookSection |
| booklet | BookSection |
| incollection | BookSection |
| article | JournalArticle |
| inproceedings | ConferenceProceedings |
| conference | ConferenceProceedings |
| proceedings | ConferenceProceedings |
| collection | ConferenceProceedings |
| techreport | Report |
| manual | Report |
| mastersthesis | Report |
| phdthesis | Report |
| unpublished | Report |
| patent | Patent |
| misc | Misc |
| electronic | ElectronicSource |
| online | InternetSite |
| periodical | ArticleInAPeriodical |

## Core Field Mapping
| Canonical or BibTeX field | XML field |
| :--- | :--- |
| bibtexkey | Tag |
| title | Title |
| year | Year |
| note | Comments |
| volume | Volume |
| edition | Edition |
| publisher | Publisher |
| booktitle | BookTitle |
| chapter | ChapterNumber |
| issue | Issue |
| number | Issue |
| isbn | StandardNumber |
| school | Department |
| institution | Institution |
| doi | DOI |
| url | URL |
| shorttitle | ShortTitle |
| pages | Pages |
| author | Authors |
| editor | Editors |
| translator | Translator |
| bookauthor | BookAuthor |
| urldate | YearAccessed, MonthAccessed, DayAccessed |

## Special Export Rules
- booktitle maps to ConferenceName for conference-centric entries.
- journal or journaltitle maps to JournalName.
- date in ISO 8601 form may be split into Year, Month, Day.
- address or location handling:
  - with comma: map to City.
  - without comma: map to City, StateProvince, CountryRegion.
- For patent entries, number maps to PatentNumber.
- For journal articles, number maps to Issue.
- For other non-patent entries, number maps to Number.
- Corporate author forms may map to Corporate.
- For patent entries, author may map to Inventor.

## Non-Equivalent Fields
### BibTeX-only fields
Fields with no native XML equivalent should be preserved with BIBTEX_ prefix where possible, for example BIBTEX_Abstract, BIBTEX_KeyWords, BIBTEX_Series.

### MS-Bib-only fields
XML-specific fields imported into bib data can be represented with msbib- prefix where needed, for example msbib-periodical, msbib-accessed.

## Mapping Warning Policy
- Never silently drop data.
- If no direct mapping exists, emit warning with one of the following categories:
  - unmapped-field
  - lossy-transformation
  - inferred-value
  - missing-required-field
