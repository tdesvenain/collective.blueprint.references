# -*- coding: utf-8 -*-
from zope.interface import implements, classProvides
from collective.transmogrifier.interfaces import ISectionBlueprint, ISection

from logging import getLogger
logger = getLogger("collective.blueprint.references")

class ReferenceSetter(object):
    """Take _path and _references"
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.context = transmogrifier.context

    def __iter__(self):
        for item in self.previous:
            if not ('_path' in item and '_references' in item):
                yield item; continue

            path = item['_path']
            obj = self.context.unrestrictedTraverse(path.lstrip('/'))

            for reference_attr in item['_references']:
                ref_objects = []
                ref_paths = item['_references'][reference_attr]
                if isinstance(ref_paths, basestring):
                    ref_paths = [ref_paths]
                for ref_path in ref_paths:
                    try:
                        ref_obj = self.context.unrestrictedTraverse(ref_path.lstrip('/'))
                    except AttributeError:
                        LOG.error("Error trying to set %s reference between %s and %s",
                                  reference_attr, path, ref_path)
                        continue

                    ref_objects.append(ref_obj)

                field = obj.getField(reference_attr)
                if not field:
                    logger.error("Error trying to get %s target field",
                                 reference_attr)
                    import pdb;pdb.set_trace()

                field.set(obj, ref_objects)

            yield item
