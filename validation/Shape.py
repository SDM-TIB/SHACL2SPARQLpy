# -*- coding: utf-8 -*-
__author__ = "Philipp D. Rohde and Monica Figuera"

import re
from validation.sparql.ASKQuery import ASKQuery
from validation.VariableGenerator import VariableGenerator
from validation.core.Literal import Literal
from validation.core.RulePattern import RulePattern


class Shape:

    def __init__(self, id, targetDef, targetQuery, constraints):
        self.id = id
        self.targetDef = targetDef
        self.targetQuery = targetQuery  # Might be None
        self.constraints = constraints
        self.rulePatterns = ()
        self.predicates = ()
        self.satisfied = None
        self.inDegree = None
        self.outDegree = None
        print("Shape refs:", self.getShapeRefs())
#        self.computePredicateSet()
        # e.g., [ActorShape, ActorShape_d1, ActorShape_d1_pos]
        # e.g., [MovieShape, MovieShape_d1, MovieShape_d1_pos, MovieShape_d1_max_1]

    def getId(self):
        return self.id

    def setDegree(self, inDegree, outDegree):
        self.inDegree = inDegree
        self.outDegree = outDegree

#    def computePredicateSet(self):
#        disjuncts = [d.getPredicates() for d in self.disjuncts]
#        predicates = [self.id] + disjuncts[0]
#        return predicates

#    def getPosShapeRefs(self):
#        return [d.getPosShapeRefs() for d in self.disjuncts]

#    def getNegShapeRefs(self):
#        return [d.getNegShapeRefs() for d in self.disjuncts]

#    def askViolations(self):
#        if self.targetDef is not None:  # not checking violations on shapes without target definitions
#            triple = re.findall(r'{.*}', self.targetDef)[0]  # *** considering only one target def
#            triple = triple[1:len(triple)-1]  # removed curly braces
#            triple = triple.strip().split()
#            target = triple[2]
#
#            minConstraints = self.disjuncts[0].minConstraints
#            for c in minConstraints:
#                c.violated = ASKQuery(c.path, target).evaluate("min", c.min)
#
#            maxConstraints = self.disjuncts[0].maxConstraints
#            for c in maxConstraints:
#                c.violated = ASKQuery(c.path, target).evaluate("max", c.max)

    def getTargetQuery(self):
        return self.targetQuery

    def getConstraints(self):
        return self.constraints

    def getShapeRefs(self):
        return [c.getShapeRef() for c in self.constraints if c.getShapeRef() is not None]

    def isSatisfied(self):
        if self.satisfied is None:
            for c in self.constraints:  # TODO: heuristics for the constraints within a shape?
                if not c.isSatisfied():
                    self.satisfied = False
                    return self.satisfied
            self.satisfied = True
        return self.satisfied

    def getValidInstances(self):
        return  # TODO

    def getViolations(self):
        return  # TODO

#    def computeConstraintQueries(self, schema, graph):
#        for c in self.disjuncts:
#            c.computeQueries(graph)
#
#        self.rulePatterns = self.computeRulePatterns()

#    def computeRulePatterns(self):
#        focusNodeVar = VariableGenerator.getFocusNodeVar()
#        head = Literal(self.id, focusNodeVar, True)
#
#        return [RulePattern(head, self.getDisjunctRPBody(d)) for d in self.disjuncts]

#    def getDisjunctRPBody(self, d):
#        focusNodeVar = VariableGenerator.getFocusNodeVar()
#        maxQueries = [Literal(s, focusNodeVar, False) for s in [q.getId() for q in d.getMaxQueries()]]
#
#        return [Literal(d.getMinQuery().getId(),
#                        focusNodeVar,
#                        True
#                        )] + \
#            maxQueries