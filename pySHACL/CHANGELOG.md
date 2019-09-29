# Changelog  
All notable changes to this project will be documented in this file.  

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Python PEP 440 Versioning](https://www.python.org/dev/peps/pep-0440/).  

## [0.10.0] - 2019-08-08

### Added
- New features from SHACL Advanced Features spec:
  - SHACL Triple Rules
  - SHACL SPARQL Rules
- New option in the cli application to enable advanced features with `--advanced`.
  - Changed the `-a` shortcut to mean `--advanced` rather than `--abort`.
- New tests for the advanced features

### Changed
- Changed usage of setup.py scripts, to proper cli entrypoints. [#23](https://github.com/RDFLib/pySHACL/pull/23)
  - This should not affect end user usability of the pyshacl script.
- Updated README.md to reflect changes including Advanced Features, and cli `--advanced` arg.
- Updated feature matrix to add section for SHACL Advanced Features.
- Fix owl:import typo [#27](https://github.com/RDFLib/pySHACL/pull/27)


## [0.9.11] - 2019-05-01

### Changed
- When using the pySHACL `Validator` class directly, the `target_graph` property will now be correctly updated to always
  refer to the fully expanded graph if inferencing is enabled, and will be the mixed graph if the ontology-mixin option 
  is enabled.
- Fixed a bug in the commandline tool when the validator throws a ValidationError, the `validator()` helper would catch 
  and format the error, so the commandline tool would output the wrong text and return the wrong exit code.


## [0.9.10.post2] - 2019-03-28

### Added
- New ability for the RDF source loader to directly load a bytes string (for example, from a HTTP request body)
  - To use, just put the bytes dump as the source parameter to the rdf load function


## [0.9.10.post1] - 2019-03-11

### Changed
- More refinements to the RDF Source loader. Fixes some minor bugs.
- Moved some of the SHACL-specific RDF Utility functions (into the RDF Source loader) into a submodule.
  - This will one day be pulled out into its own RDF Utilities python module.
- Listed some additional Trove Classifiers in the setup.py file.


## [0.9.10] - 2019-03-07 

### Added
- Added the ability to for the graph loader to load multiple source files into a single graph.
- This gives the ability follow `owl:imports` statements. We currently go (base+3) levels of imports deep maximum.
- Added `--imports` switch to the cmdline script, that turns on the owl:imports feature.
- Added the ability for the web rdf retriever to inspect the HTTP headers for 'Content-Type' for the RDF format
- Added documentation to the readme about `--imports` option.
- Add more coverage tests. Bumped coverage to 86%.

### Changed
- More potential Windows fixes
- Fixed a bug where the graph_id and base_uri was calculated incorrectly in some cases.
- Fix an issue when extracting base uri and prefix from comments in turtle when it was formatted in Windows line endings.
- Hitting a HTTP error when importing a subgraph is no longer an issue, we just ignore that import statement.


## [0.9.9.post1] - 2019-02-28 

### Changed
- Fixed an issue with loading RDF files on Windows
- Fixed an issue running the test suite on Windows
- Main pyshacl module now exports the Validator class by default


## [0.9.9] - 2019-01-09 
- This is a big release, building up to the major 1.0 release.
- Expect some issues, there will be 0.9.9.postX releases with just bug fixes between now and 1.0

### Added
- Major new feature. Added the ability to pass in an extra ontology document which gets parsed and mixed with the 
data graph before pre-inferencing. This helps in the cases where the target data graph contains a data snippet which 
can only be fully expanded with the help of an external ontology document containing RDFS and OWL axioms.
  - Use `ont_graph=path_to_graph` in the python module or
  - Use `-e` or `--ont-graph` on the command line utility to take advantage of this feature.
- SHACL graph or ONT graph can now be a Web URL, rather than a file path.
  - This works from the module validator entrypoint or the commandline tool.
- Added built in tests for issue#14 and for the commandline tool.  
- Added new details to the README about the above new features.
- Added coverage statistics to the README.
- Started adding some hopefully-informative debugging output messages when debug mode is turned on. More to come.

### Changed
- Pre-inferencing can now only ever be run once per Validator instance, this is an attempt to prevent running 
pre-inferencing multiple times unnecessarily.
- Internal shapes lookup cache is now stored in the `ShapesGraph` instance, rather than in a global static class 
variable on the `Shape` class
- Fixed some bugs in the examples code, thanks @johannesloetzsch!
- Lots of code coverage specific changes, and comments where we can improve coverage.
 
 
## [0.9.8.post1] - 2018-12-05    
### Changed
- Fixed a bug where files passed in to the command-line utility would get closed after being parsed, but sometimes 
they would need to be reopened again, like in the case of doing metashacl. The fix detects when this is the case and 
just leaves the files open. Now it is up to the command-line client to close the files.

## [0.9.8] - 2018-11-30   
### Changed
- Fixed a bug in 0.9.7 where some references to the RDFClosure module were still in use in the code.
  - So v0.9.7 only worked if you had installed 0.9.6 and upgraded to 0.9.7. New installs didn't work.
  - All references to RDFClosure are now changed to owlrl.
- Bumped required owlrl version to the new 5.2 release, which is faster (doesn't use LiteralProxy anymore).

## [0.9.7] - 2018-11-23   
### Added
- A new tests directory for testing reported github issues, and ensuring they pass even in future versions of this tool
### Changed
- RDFClosure is now named `owlrl`, and is now published on PyPI.
  - Use the new package name
  - Use the version from pypi
  - No longer need dependency_links when installing
  - Resume issuing binary builds
  - Remove dependency_links instructions from readme.md


## [0.9.6] - 2018-11-18   
### Added
- CLI tool got two new options, `--shacl_file_format` (`-sf`) and `--data_file_format` (`-df`), for when the auto file format detection doesn't work for you.
### Changed
- The `validate` entrypoint, renamed `target_graph` to `data_graph`, and `target_graph_format` to `data_graph_format`
  - Updated example files to match
- Fixed a bug in sh:closed rule. It was incorrectly checking the rule against the shacl shapes graph, instead of the target graph


## [0.9.5] - 2018-09-25  
### Added  
- Added the missed 'proposed' test in the SHT conformance suite

### Changed  
- EARL namespace https->http
- No longer publishing Binary Wheels for now, this is to force pip to run setup.py when installing the module, in order to process dependency links.


## [0.9.4.post1] - 2018-09-24  
### Added  
- Post-Release fixed a setup.py issue where it was not installing all of the required pySHACL modules.
  - This has actually been a severe bug since 0.8.3, sorry!


## [0.9.4] - 2018-09-24  
### Added  
- Additional required check that all potentially pre-bound variables are SELECTED from a nested SELECT statement in a SPARQL subquery.  
- Better Literal less-than-or-equal and greater-than-or-equal comparison  
  - fixes date-time comparisons with timezones, and other small issues  
- Formal EARL validation report generator  
- Submitted EARL validation report  

### Changed
- Graph cleaner now works in a much more agressive manner, to remove all rdfs:Resource added triples  
- Fixed SPARQL-based Constraint Component validator now outputs a default sh:value item if it is validating with a sourceShape that is a SHACL NodeShape  
- Fixed a tiny bug in the list-compare subsection of the blank-node deep-compare utility  
- Changed OWL-RL dependency from @py3 to @master, because master branch is now on Py3.  
- One test from the SHT test suite was changed by Holger, so it passes now.  
- Two timezone-based datetime comparison tests now pass  


## [0.9.3] - 2018-09-22  
### Added  
- A new deep-compare feature to check actual validation-result blank-nodes against expected validation-result blank nodes
- Added a validation-report graph cleaner, to remove all unwanted triples from a validation report graph.  
- A new RDF Node deep-clone feature to properly clone nodes into the Validation Report graph, rather than copying them. 

### Changed
- Removed old test suite directory accidentally left in  
- Fixed some bugs identified by the new expected-result deep-compare feature
- Changed incorrectly named constraint components (mislead by typo in the SHACL spec)
  - PropertyShapeComponent -> PropertyConstraintComponent
  - NodeShapeComponent -> NodeConstraintComponent
- Fixed some bugs identified by the [data-shapes-test-suite](https://w3c.github.io/data-shapes/data-shapes-test-suite)
- Bumped version number


## [0.9.2] - 2018-09-20  
### Added  
- A feature to patch RDFLib Literal conversion functions, to fix some RDFLib bugs
- A new exception ConstrainLoadWarning, for when a constraint is invalid but we want to ignore it
- Additional rules are now applied to the SPARQL queries in SPARQL-based constraints, as per the SHACL spec
- Currently failing [data-shapes-test-suite](https://w3c.github.io/data-shapes/data-shapes-test-suite) documented in the FEATURES file

### Changed  
- Fixed some bugs identified by the [data-shapes-test-suite](https://w3c.github.io/data-shapes/data-shapes-test-suite)
- Bumped version number
- 206 of 212 tests are now passing  


## [0.9.1] - 2018-09-19  
### Added  
- A second testing framework is in place  
  - this one tests against the [data-shapes-test-suite](https://w3c.github.io/data-shapes/data-shapes-test-suite).  

### Changed  
- Changed the layout and structure of the tests folder  
- Fixed a bug in the XOne constraint, discovered indicated by the new tests  
- 199 of 212 tests are now passing   


## [0.9.0] - 2018-09-19  
### Added
- Sparql Based Constraint Components  
- Sparql Constraint Component Validators  
  - AskConstraintValidator  
  - SelectConstraintValidator  
- New meta-shacl mode!  
  -  You can now validate your SHACL Shapes Graph against the built-in SHACL-SHACL Shapes graph, as an added step before validating the Data Graph.
- Updated README with Command-Line tool instructions
- Updated README with Meta-SHACL instructions
- Added new sections to the FEATURES matrix

### Changed
- Internally, a SHACL Shapes graph is now represented as a python object with type `SHACLGraph`, rather than simply an `rdflib.Graph`.
  - This allows more SHACL-specific functionality and properties that are of the SHACL graph itself.
- Updated FEATURES matrix
- Bumped version to show magnitude of progress
- 92 tests now pass


## [0.8.3] - 2018-09-17  
### Added
- Another example, this one with separate SHACL and Target files.

### Changed  
- Fixed an issue where the content of a separate SHACL graph was ignored by the validator  
- Fixed a crash caused by the result generator receiving a value node that was a string but not an RDF literal.
- Refactored constraint file layouts, in preparation for the new SPARQL constraint component functionality
- Bumped version number


## [0.8.2] - 2018-09-16  
### Added   
- Added a CONTRIBUTORS file  
- Minor fixes for PyPI upload compatibility  


## [0.8.1] - 2018-09-14  
### Added  
- Basic SPARQL Query functionality.
- SPARQL Prefix support capability

### Changed  
- Changed make_v_report function name to make_v_result, because it actually makes individual validation results, not reports.
- Changed one of the SPARQL prefix tests to better test the SPARQL uri shortening functionality
- Bumped version number
- 88 Tests now passing


## [0.8.0] - 2018-09-12  
### Added  
- Added the CLI script. pySHACL can now be easily run from the command-line.
- Added the ability for the `validate` function to work on already-open file descriptors for target data file, and for shacl file.

### Changed  
- Main `validation` function now outputs a three-item-tuple: `(conformance: bool, validation_report_graph: rdflib.Graph, validation_report_text: str)`
- Level for seeing runtime output is now DEBUG
- Changed the way a single logging interface is used across the whole application
- Bumped version number way up to show project maturity


## [0.1.0b1.dev20180912] - 2018-09-12  
### Added  
- The SHACL Core functionality is Feature-Complete!
- Added languageIn and uniqueLang constraint components!
- Added the rest of the SHACL Property Path functionality
- Added a new error type, ReportableRuntimeError, which is a RuntimeError which is desgned to pass information back to the user (via commandline, or web interface).

### Changed  
- Changed most RuntimeErrors to ReportableRuntimeErrors
- Adding the new property path rules required refactoring the way shapes generate their targets. It is much more complicated now.
- Updated Features Matrix
- Bumped Version, changed Alpha to Beta
- All 84 Core tests now passing!


## [0.1.0a10.dev20180911] - 2018-09-11  
### Added  
- Added 3 more new constraint components!
  - sh:qualifiedValueShape - QualifiedValueShapeConstraintComponent
  - sh:qualifiedMinCount - QualifiedMinCountConstraintComponent
  - sh:qualifiedMaxCount - QualifiedMaxCountConstraintComponent

### Changed  
- the make_v_result function can now take an argument to overwrite the target failing component with a custom value.
  - this is required to allow QualifiedValueShapeConstraintComponent to output the correct type of failure
- Bumped version number
- 73 tests now passing!


## [0.1.0a9.dev20180911] - 2018-09-11  
### Added  
- Added 5 more new constraint components!
  - sh:equals - EqualsConstraintComponenet
  - sh:disjoint - DisjointConstraintComponent
  - sh:lessThan - LessThanConstraintComponent
  - sh:lessThanOrEqual - LessThanOrEqualConstraintComponent
  - sh:hasValue - HasValueConstraintComponent
### Changed  
- Bumped version number
- 70 tests now passing!


## [0.1.0a8.dev20180910] - 2018-09-10  
### Changed  
- Bug: Fixed setup.py to also install the pyshacl submodules
- Bug: Use the correct parse parameters when parsing plain-text RDF as a graph input source


## [0.1.0a7.dev20180910] - 2018-09-10   
### Added  
- Added the ability to specify a rdf_format string (for the target graph and/or the shacl graph) on the main `validate` callable.  
- Added the ability to ingest and validate RDF n-triples .nt files (as the target graph, or the shacl graph)  
- Added the option to serialize the output ValidationReport graph  
- Added an example script to show a full working example of how to use the validator  

### Changed  
- Bug: Fixed the main validate function so that it actually returns the results to the caller


## [0.1.0a6.dev20180909] - 2018-09-09  
### Added
- Added a benchmark file, run it on your computer to see how fast you can do a validation.

### Changed
- Changed the default inferencing method to 'none' to make the validator both faster and more predictable
- Bug: Fixed the default_options function, it no longer incorrectly overwrites a passed in option.
- Removed the stray main.py file which served no purpose anymore.
- Bumped version number


## [0.1.0a5.dev20180907] - 2018-09-07  
### Added  
- Added new ConstraintComponent:  
  - Closed Constraint  
- Added a new custom RDFS semantic closure for the OWL-RL reasoner.  
- Added new properties to Shape objects as per the SHACL spec:  
  - `sh:deactivated` to turn off a shape  
  - `sh:name` to name/title a shape when represented in a form  
  - `sh:description` to describe a shape when represented in a form  
  - `sh:message` a shape's message to include in the shape report output  
- Added new Shape Target types:  
  - `sh:targetSubjectsOf` and `sh:targetObjectsOf`  
- Added the Shape's message to the message output of the ValidationReport  
- Added a link to a correctly rendered view of the FEATURES table  

### Changed  
- Changed the default pre-inferencing type. Now only do RDFS by default, not RDFS+OWLRL  
  - The SHACL validator run approx 10-15x faster when the target graph is inferenced using RDFS rather than RDFS+OWLRL.  
  - And all the the tests still pass, so OWL-RL inferencing is not required for normal SHACL validation.  
- Changed the RDFS Semantic closure for inferencing to our new custom one which ignores the 'hidden' rules.  
- 61 tests now passing  
- Updated FEATURES list.  
- Bumped version number  


## [0.1.0a4.dev20180906] - 2018-09-06  
### Added  
- Added 4 value-range constraint
  - MinExclusive, MinInclusive
  - MaxExclusive, MaxInclusive
- Added a misc constraint: InComponentConstraint
### Changed  
- Fixed some other edge cases so that more tests pass
- 52 tests now passing
- Bumped version number


## [0.1.0a3.dev20180906] - 2018-09-06  
### Added  
- Added string-based min-length and max-length constraints  
- Added logic-shape constraints (not, or, and, xone)  
- Fixed the or-datatype.test.ttl file, which would never pass due to the nature of how RDFLib parses boolean literals.  
### Changed  
- Fixed a bug in the string-based pattern-match constraint  
- Changed the variable naming convention to more closely match the SHACL spec  
  - Renamed `fails`, `failures`, `f`, etc to "Reports", because failures in SHACL are a different thing, reports are their correct name.  
- Fixed some minor issues to get more tests passing  
- 40 Tests now passing


## [0.1.0a2.dev20180906] - 2018-09-06  
### Added  
- Added full pattern matching ConstraintComponent, with working flags.  
- Result reporting and report generation is implemented  
- Two types of shapes are now implemented (NodeShapes and PropertyShapes)  
- Implicit class targeting on target-less is implemented  
- Basic path traversal on PropertyShapes is implemented  
- Seven key types of ConstraintComponents are added and working  
### Changed  
- Fixed bug in datatype matcher that would cause some tests to fail.  
- Switched to running all tests in the directory, rather than running individual tests.  
- Fixed textual report output to format Literals better (to see how they are wrong).  
- Bug fixes since previous version  
- 10+ tests are passing.  


## 0.1.0a1.dev20180904 - 2018-09-04  
### Added  

- Initial version, limited functionality  

[Unreleased]: https://github.com/RDFLib/pySHACL/compare/v0.10.0...HEAD 
[0.10.0]: https://github.com/RDFLib/pySHACL/compare/v0.9.11...v0.10.0
[0.9.11]: https://github.com/RDFLib/pySHACL/compare/v0.9.10.post2...v0.9.11
[0.9.10.post2]: https://github.com/RDFLib/pySHACL/compare/v0.9.10.post1...v0.9.10.post2
[0.9.10.post1]: https://github.com/RDFLib/pySHACL/compare/v0.9.10...v0.9.10.post1
[0.9.10]: https://github.com/RDFLib/pySHACL/compare/v0.9.9.post1...v0.9.10
[0.9.9.post1]: https://github.com/RDFLib/pySHACL/compare/v0.9.9...v0.9.9.post1
[0.9.9]: https://github.com/RDFLib/pySHACL/compare/v0.9.8.post1...v0.9.9
[0.9.8.post1]: https://github.com/RDFLib/pySHACL/compare/v0.9.8...v0.9.8.post1
[0.9.8]: https://github.com/RDFLib/pySHACL/compare/v0.9.7...v0.9.8
[0.9.7]: https://github.com/RDFLib/pySHACL/compare/v0.9.6...v0.9.7
[0.9.6]: https://github.com/RDFLib/pySHACL/compare/v0.9.5...v0.9.6
[0.9.5]: https://github.com/RDFLib/pySHACL/compare/v0.9.4.post1...v0.9.5
[0.9.4.post1]: https://github.com/RDFLib/pySHACL/compare/v0.9.4...v0.9.4.post1
[0.9.4]: https://github.com/RDFLib/pySHACL/compare/v0.9.3...v0.9.4
[0.9.3]: https://github.com/RDFLib/pySHACL/compare/v0.9.2...v0.9.3
[0.9.2]: https://github.com/RDFLib/pySHACL/compare/v0.9.1...v0.9.2
[0.9.1]: https://github.com/RDFLib/pySHACL/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/RDFLib/pySHACL/compare/v0.8.3...v0.9.0
[0.8.3]: https://github.com/RDFLib/pySHACL/compare/v0.8.2...v0.8.3
[0.8.2]: https://github.com/RDFLib/pySHACL/compare/v0.8.1...v0.8.2
[0.8.1]: https://github.com/RDFLib/pySHACL/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/RDFLib/pySHACL/compare/v0.1.0b1.dev20180912...v0.8.0
[0.1.0b1.dev20180912]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a10.dev20180911...v0.1.0b1.dev20180912
[0.1.0a10.dev20180911]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a9.dev20180911...v0.1.0a10.dev20180911
[0.1.0a9.dev20180911]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a8.dev20180910...v0.1.0a9.dev20180911
[0.1.0a8.dev20180910]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a7.dev20180910...v0.1.0a8.dev20180910
[0.1.0a7.dev20180910]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a6.dev20180909...v0.1.0a7.dev20180910
[0.1.0a6.dev20180909]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a5.dev20180907...v0.1.0a6.dev20180909
[0.1.0a5.dev20180907]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a4.dev20180906...v0.1.0a5.dev20180907
[0.1.0a4.dev20180906]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a3.dev20180906...v0.1.0a4.dev20180906 
[0.1.0a3.dev20180906]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a2.dev20180906...v0.1.0a3.dev20180906 
[0.1.0a2.dev20180906]: https://github.com/RDFLib/pySHACL/compare/v0.1.0a1.dev20180904...v0.1.0a2.dev20180906  
