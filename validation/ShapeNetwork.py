# -*- coding: utf-8 -*-
__author__ = "Philipp D. Rohde"

from validation.core.ValidationTask import ValidationTask
from validation.ShapeParser import ShapeParser
from validation.sparql.SPARQLEndpoint import SPARQLEndpoint


class ShapeNetwork:

    def __init__(self, schemaDir, schemaFormat, endpointURL, graphTraversal, validationTask, workInParallel=False):
        self.shapes = ShapeParser().parseShapesFromDir(schemaDir, schemaFormat)
        self.endpoint = SPARQLEndpoint(endpointURL)
        self.graphTraversal = graphTraversal
        self.validationTask = validationTask
        self.parallel = workInParallel
        # TODO: compute edges; in- and outdegree; dependencies

    def getStartingPoint(self):
        """Use heuristics to determine the first shape for evaluation of the constraints."""
        # TODO
        return

    def validate(self, validationTask):
        """Execute one of the validation tasks in validation.core.ValidationTask."""
        # TODO: if the task can be set here; then it does not need to be stored during initialization
        start = self.getStartingPoint()
        if validationTask == ValidationTask.GRAPH_VALIDATION:
            # TODO
            return
        elif validationTask == ValidationTask.SHAPE_VALIDATION:
            # TODO
            return
        elif validationTask == ValidationTask.INSTANCES_VALID:
            # TODO
            return
        elif validationTask == ValidationTask.INSTACES_VIOLATION:
            # TODO
            return
        else:
            raise TypeError("Invalid validation task: " + validationTask)

    def computeInAndOutDegree(self):
        """Computes the in- and outdegree of each shape."""
        # TODO
        return

    def computeEdges(self):
        """Computes the edges in the network."""
        # TODO
        return

    def isSatisfied(self):
        """Checks whether the graph is satisfiable or not."""
        # TODO
        return

    def getValidInstances(self):
        """Reports all instances that validate the constraints of the graph."""
        # TODO
        return

    def getViolations(self):
        """Reports all instances that violate the constraints of the graph."""
        # TODO
        return
