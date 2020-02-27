# -*- coding: utf-8 -*-
import os
from validation.ShapeParser import ShapeParser

class Eval(object):

    def __init__(self, args):
        """
        :type args: ...
        """

        self.parseArguments(args)
        self.schema = None
        self.endpoint = None
        self.outputDir = None
        self.shapeFormat = "JSON"

        self.parseArguments(args)
        #schema.getShapes()
        #        .forEach(sh -> sh.computeConstraintQueries(schema, graph))
        self.createOutputDir()

    def createOutputDir(self):
        path = os.getcwd()
        os.makedirs(path + '/' + self.outputDir, exist_ok=True)

    # to do: schemaFile and schemaString
    def parseArguments(self, args):
        # E.g.: -d. ../examples/shapes/nonRec/2/ "http://dbpedia.org/sparql". /output/

        self.schema = args.d
        self.endpoint = args.endpoint
        self.outputDir = args.outputDir
        self.shapeFormat = "JSON"

        schema = self.getSchema(args.d)

        #log.info("endPoint: |" + endpoint.getURL() + "|");
        #schemaDir.ifPresent(d -> log.info("shape directory: |" + d + "|"));
        #log.info("output directory: |" + outputDir + "|");


    def getSchema(self, schemaDir):
        shapeParser = ShapeParser() # instantiate before calling its functions
        return shapeParser.parseSchemaFromDir(schemaDir, self.shapeFormat)