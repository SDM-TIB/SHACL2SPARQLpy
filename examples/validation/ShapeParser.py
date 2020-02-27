# -*- coding: utf-8 -*-
import os
import json
from validation.SPARQLPrefixHandler import getPrefixString
from validation.VariableGenerator import VariableGenerator
from validation.MinOnlyConstraintImpl import MinOnlyConstraintImpl
from validation.MaxOnlyConstraintImpl import MaxOnlyConstraintImpl
from validation.ConstraintConjunctionImpl import ConstraintConjunctionImpl
from validation.ShapeImpl import ShapeImpl
from validation.SchemaImpl import SchemaImpl

class ShapeParser:

    def __init__(self):
        return

    def parseSchemaFromDir(self, path, shapeFormat):
        fileExtension = self.getFileExtension(shapeFormat)
        filesAbsPaths = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if fileExtension in file:
                    filesAbsPaths.append(os.path.join(r, file))

        if shapeFormat == "JSON":
            shapes = [self.parseJson(p) for p in filesAbsPaths]
            return SchemaImpl(shapes)
        else:
            print("Unexpected format: " + shapeFormat)

    def getFileExtension(self, shapeFormat):
        if shapeFormat == "SHACL":
            return ".ttl"
        else:
            return ".json" # dot added for convenience

    def parseJson(self, path):
        targetQuery = None

        file = open(path, "r")
        obj = json.load(file)
        targetDef = obj.get("targetDef")

        if targetDef != None:
            query = targetDef["query"]
            if query != None:
                targetQuery = getPrefixString() + query

        name = obj["name"]
        constraintsConjunctions = self.parseConstraints(name, obj["constraintDef"]["conjunctions"])

        return ShapeImpl(
                name,
                targetQuery,
                constraintsConjunctions
        )

    def parseConstraints(self, shapeName, array):
        return [self.parseDisjunct(array[i], shapeName + "_d" + str(i + 1)) for i in range(len(array))]

    def parseDisjunct(self, array, id):
        varGenerator = VariableGenerator()
        constraints = [self.parseConstraint(varGenerator, array[i], id + "_c" + str(i + 1)) for i in range(len(array))]

        minConstraints = [inst for inst in constraints if isinstance(inst, MinOnlyConstraintImpl)]
        maxConstraints = [inst for inst in constraints if isinstance(inst, MaxOnlyConstraintImpl)]
        localConstraints = [] # *** hardcoded

        return ConstraintConjunctionImpl(
                id,
                minConstraints,
                maxConstraints,
                localConstraints
        )

    def parseConstraint(self, varGenerator, obj, id):
        min = obj.get("min")
        max = obj.get("max")
        shapeRef = obj.get("shape")
        datatype = obj.get("datatype")
        value = obj.get("value")
        path = obj.get("path")
        negated = obj.get("negated")

        oMin = None if (min == None) else int(min)
        oMax = None if (max == None) else int(max)
        oShapeRef = None if (shapeRef == None) else str(shapeRef)
        oDatatype = None if (datatype == None) else str(datatype)
        oValue = None if (value == None) else str(value)
        oPath = None if (path == None) else str(path)
        oNeg = True if (negated == None) else not negated # True means is a positive constraint

        if oPath != None:
            if oMin != None:
                if oMax != None:
                    pass # TODO
                return MinOnlyConstraintImpl(varGenerator, id, oPath, oMin, oDatatype, oValue, oShapeRef, oNeg)
            if oMax != None:
                return MaxOnlyConstraintImpl(varGenerator, id, oPath, oMax, oDatatype, oValue, oShapeRef, oNeg)

        # TODO
        #return new LocalConstraintImpl(id, oDatatype, oValue, oShapeRef, oNeg);