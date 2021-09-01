# Word counter for word processor files
A simple word counter for more complex text processor files.

## Functionality
On command (be it manual or croned):

1. Retrieve list of known files from a database
1. Crawl the directory structure from a given starting point
1. Count words in all supported files found in the directory
1. Update (or create) records in a database, keep history
1. Display list of changed files and sum of the words

## Input
* Directory name (MVP)
* Specific files (optional)

## Output
* Changed database records
* Summary of changes on console

## Assumptions
* Content is irrelevant, only the numbers count; if a file lost 50 words but gained 150, the final result is to be 100

## Supported files
* txt
* md
* docx (planned)
* odt (planned)
