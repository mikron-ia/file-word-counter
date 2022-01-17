# Word counter for word processor files

A simple word counter for more complex text processor files.

## Functionality

On command (be it manual or croned):

1. Retrieve list of known files from a database - _waiting for database support_
2. Crawl the directory structure from a given starting point - _in progress_
3. Count words in all supported files found in the directory - _in progress_
4. Update (or create) records in a database, keep history - _waiting for database support_
5. Display list of changed files and sum of the words - _in progress_

## Input

* Directory name - _todo_
* Specific files

## Output

* Changed database records
* Summary of changes on console

## Assumptions

* The content is irrelevant; if a file lost 50 words but gained 150, the final result is to be increase by 100

## Supported files

* txt
* md
* docx
* odt
